// Renders scifi-system.svg to scifi-system.png with headless Chromium (needs playwright installed).
// Usage: node docs/render_figure.js
const path = require('path');
let chromium;
try { chromium = require('playwright').chromium; }
catch (e) { chromium = require('/opt/npm-tools/node_modules/playwright').chromium; }
(async () => {
  const dir = __dirname;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1700, height: 1180 }, deviceScaleFactor: 1.5 });
  await p.goto('file://' + path.join(dir, 'scifi-system.svg'));
  await p.screenshot({ path: path.join(dir, 'scifi-system.png'), timeout: 90000 });
  await b.close();
  console.log('rendered scifi-system.png');
})().catch(e => { console.error(e.message); process.exit(1); });
