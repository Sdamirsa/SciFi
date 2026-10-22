// Test harness for workflows/*.js: runs a script with mock agent(), pipeline(), parallel(),
// phase() and log() so the files it asks the scribe to write really land on disk.
// Usage: node _workflow_harness.js <script.js> <args.json>   (prints the script's return value as JSON)
// The mock agent returns a schema-shaped envelope for every brief it receives and, for a scribe
// prompt, writes the listed files. It is not a model; it only checks the plumbing.
const fs = require('fs');
const path = require('path');

const [scriptPath, argsPath] = process.argv.slice(2);
const src = fs.readFileSync(scriptPath, 'utf8').replace(/^export const meta/m, 'const meta');
const args = JSON.parse(fs.readFileSync(argsPath, 'utf8'));
const calls = [];

function writeScribeFiles(prompt) {
  const written = [];
  const start = prompt.indexOf('\n--- /');
  if (start < 0) return { written, invalid: [] };
  const parts = prompt.slice(start + 1).split(/\n\n--- (?=\/)/);
  parts.forEach((part, i) => {
    const block = i === 0 ? part.slice(4) : part;
    const nl = block.indexOf('\n');
    const file = block.slice(0, nl);
    fs.mkdirSync(path.dirname(file), { recursive: true });
    fs.writeFileSync(file, block.slice(nl + 1));
    written.push(file);
  });
  return { written, invalid: [] };
}

const harness = args.__harness || {};   // fail: labels whose agent returns null; block: labels whose envelope is status blocked
async function agent(prompt, opts) {
  opts = opts || {};
  calls.push({ label: opts.label || null, phase: opts.phase || null, agentType: opts.agentType || null, model: opts.model || null, effort: opts.effort || null, hasSchema: !!opts.schema });
  if ((harness.fail || []).includes(opts.label)) return null;
  if (prompt.startsWith('You are the SciFi scribe')) return writeScribeFiles(prompt);
  const brief = JSON.parse(prompt.slice(prompt.indexOf('\n') + 1));
  if ((harness.block || []).includes(opts.label)) {
    return { task_id: brief.task_id, agent_id: brief.agent, status: 'blocked', result: 'input missing', evidence: [], findings: [], needs: ['NEED: ' + brief.inputs[0]] };
  }
  if (opts.schema && (!opts.schema.properties || opts.schema.type !== 'object')) throw new Error('bad schema root');
  const env = {
    task_id: brief.task_id, agent_id: brief.agent, status: 'done',
    result: 'mock result for ' + brief.task_id, evidence: ['mock'],
    findings: [{ id: brief.task_id + '.f1', axis: 'other', severity: 'minor', issue: 'mock issue', solution: 'mock fix', location: brief.task_id.split('.')[0] + ':s1', rule: 'checklist C1' }],
    needs: [],
  };
  if (brief.agent === 'standards-gate') { env.verdict = 'PASS'; env.manuscript_verdict = 'minor'; }
  if (brief.agent === 'noter' || brief.agent === 'labeler') env.artifacts = [brief.output_contract.file];
  return env;
}

async function pipeline(items, ...stages) {
  return Promise.all(items.map(async (item, i) => {
    let prev = item;
    try {
      for (const stage of stages) prev = await stage(prev, item, i);
      return prev;
    } catch (e) { process.stderr.write('pipeline item ' + i + ' failed: ' + e.message + '\n'); return null; }
  }));
}

async function parallel(thunks) {
  if (!Array.isArray(thunks) || thunks.some(t => typeof t !== 'function')) throw new Error('parallel() expects an array of functions');
  return Promise.all(thunks.map(t => t().catch(e => { process.stderr.write('parallel thunk failed: ' + e.message + '\n'); return null; })));
}

const phases = [];
function phase(title) { phases.push(title); }
function log(message) { process.stderr.write('[log] ' + message + '\n'); }
const budget = { total: null, spent: () => 0, remaining: () => Infinity };
async function workflow() { throw new Error('nested workflow not supported in harness'); }

const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
const fn = new AsyncFunction('args', 'agent', 'pipeline', 'parallel', 'phase', 'log', 'budget', 'workflow', src);
fn(args, agent, pipeline, parallel, phase, log, budget, workflow)
  .then(result => { process.stdout.write(JSON.stringify({ result, calls, phases }, null, 2)); })
  .catch(e => { process.stderr.write('script failed: ' + (e.stack || e.message) + '\n'); process.exit(1); });
