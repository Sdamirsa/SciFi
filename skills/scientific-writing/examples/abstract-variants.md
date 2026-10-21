# One study, four abstracts

The same invented study written for four journal formats, so the moves and the differences are visible. The study, data and numbers are fictional and exist only to show the form. Do not reuse the numbers.

The invented study evaluates an open-weight language model that extracts valvular disease severity from 1,200 echocardiography reports at two hospitals, compared with a rule-based system and labelled by two cardiologists. The four abstracts are separate documents, so running the checker over this file as one manuscript will report abbreviations defined four times.

---

## JAMIA (structured, 250 words)

**Objective** Manual abstraction of valvular heart disease (VHD) severity from echocardiography reports limits registry completeness. We evaluated whether an open-weight large language model (LLM) run on hospital hardware can extract VHD severity with accuracy comparable to cardiologist labelling.

**Materials and Methods** In this retrospective two-centre study, 1,200 consecutive transthoracic echocardiography reports (2022 to 2023) were labelled independently by two cardiologists for the severity of four valvular lesions, with disagreements resolved by consensus. A 70-billion-parameter open-weight LLM, prompted without fine-tuning, was compared with a rule-based system. Prompts were developed on 200 reports from one centre and evaluated on 1,000 held-out reports from both centres. The primary outcome was per-lesion accuracy with 95% confidence intervals (CI) from 2,000 bootstrap resamples.

**Results** Cardiologist agreement before consensus was 94.1% (Cohen's kappa 0.89, 95% CI 0.86 to 0.92). The LLM reached a mean accuracy of 96.3% (95% CI 95.1 to 97.4) versus 88.7% (87.0 to 90.4) for the rule-based system, a difference of 7.6 percentage points (95% CI 5.8 to 9.4). Accuracy was 95.8% (93.9 to 97.5) at the external centre. Processing took 4.1 seconds per report. Of 37 LLM errors, 24 (64.9%) involved reports that described a lesion as between two grades.

**Discussion and Conclusion** An open-weight LLM extracted VHD severity from echocardiography reports more accurately than a rule-based system, with performance maintained at a second centre. Residual errors concentrated on ambiguous grading language, which suggests that report standardisation would help more than further prompt tuning. Prospective evaluation within a registry workflow is the next step.

## The Lancet Digital Health (structured, 280 words, with Research in context)

**Background** Echocardiography reports are the main source of valvular heart disease (VHD) severity for registries, but severity is recorded as free text and abstracted by hand. We assessed whether an open-weight large language model (LLM) deployed inside a hospital network can extract VHD severity accurately across two centres.

**Methods** In this retrospective study, we included consecutive transthoracic echocardiography reports from two university hospitals in Switzerland between Jan 1, 2022, and Dec 31, 2023. Two cardiologists labelled each report for the severity of aortic, mitral, tricuspid and pulmonary lesions, with consensus adjudication. A 70-billion-parameter open-weight LLM was prompted without fine-tuning and compared with a rule-based system. Prompts were developed on 200 reports from centre A and tested on 1,000 reports from both centres. The primary outcome was per-lesion accuracy, with 95% CIs obtained by bootstrap. The study followed TRIPOD-LLM.

**Findings** Of 1,200 reports, 1,000 formed the test set. Median patient age was 71 years (IQR 62 to 79) and 418 (41.8%) were women. The LLM achieved an accuracy of 96.3% (95% CI 95.1 to 97.4) compared with 88.7% (87.0 to 90.4) for the rule-based system (difference 7.6 percentage points, 5.8 to 9.4). Accuracy at centre B, not used for prompt development, was 95.8% (93.9 to 97.5). Mean processing time was 4.1 s per report. 24 (64.9%) of 37 LLM errors occurred in reports that graded a lesion between two categories.

**Interpretation** An open-weight LLM run within hospital infrastructure extracted VHD severity from echocardiography reports more accurately than a rule-based system, including at an external centre, and could support registry completion if validated prospectively.

**Funding** [Funder].

**Research in context.** *Evidence before this study* We searched PubMed and Embase on March 1, 2024, for "large language model" AND "echocardiography" AND ("extraction" OR "classification") without language restriction and found nine studies. All used single-centre data, six used proprietary models that require sending reports outside the hospital, and none reported external evaluation. *Added value of this study* We show that an open-weight model deployed locally reaches 96.3% accuracy and holds its performance at a second centre, with errors concentrated in ambiguous grading language. *Implications of all the available evidence* Locally deployed LLMs can populate VHD registries from existing reports without data leaving the hospital. Prospective validation and report standardisation should precede routine use.

## npj Digital Medicine (unstructured, 180 words)

Registries of valvular heart disease (VHD) depend on manual abstraction of echocardiography reports, which is slow and incomplete. Large language models (LLMs) could automate extraction, but most evaluations have used proprietary models that require reports to leave the hospital, and none has tested performance at a second centre. Here we evaluated a 70-billion-parameter open-weight LLM, run on hospital hardware without fine-tuning, on 1,200 consecutive echocardiography reports from two centres labelled by two cardiologists. Prompts were developed on 200 reports from one centre and tested on 1,000 held-out reports. The LLM reached an accuracy of 96.3% (95% confidence interval 95.1 to 97.4) versus 88.7% (87.0 to 90.4) for a rule-based comparator, and 95.8% (93.9 to 97.5) at the centre not used for development, at 4.1 s per report. Two thirds of the remaining errors involved reports that graded a lesion between two categories. These results show that locally deployed open-weight LLMs can extract VHD severity with accuracy close to cardiologist agreement. Prospective evaluation in a registry workflow is needed before routine use.

## European Heart Journal (structured, with Translational perspective)

**Aims** To determine whether an open-weight large language model (LLM) deployed within hospital infrastructure can extract valvular heart disease (VHD) severity from echocardiography reports with accuracy comparable to cardiologist labelling.

**Methods and results** In a retrospective two-centre study, 1,200 consecutive transthoracic echocardiography reports (2022 to 2023) were labelled by two cardiologists with consensus adjudication (pre-consensus agreement 94.1%, kappa 0.89, 95% CI 0.86 to 0.92). A 70-billion-parameter open-weight LLM, prompted without fine-tuning, was compared with a rule-based system. Prompts were developed on 200 reports from centre A and tested on 1,000 reports from both centres. The LLM achieved an accuracy of 96.3% (95% CI 95.1 to 97.4) versus 88.7% (87.0 to 90.4) for the rule-based system (difference 7.6 percentage points, 95% CI 5.8 to 9.4, P < 0.001), with 95.8% (93.9 to 97.5) at centre B. Processing took 4.1 s per report. Of 37 errors, 24 (64.9%) involved reports grading a lesion between two categories.

**Conclusion** A locally deployed open-weight LLM extracted VHD severity from echocardiography reports more accurately than a rule-based system and maintained accuracy at a second centre. Residual errors reflect ambiguous grading language rather than model failure.

**Translational perspective** VHD registries are only as complete as the manual abstraction that feeds them. We show that an open-weight language model running inside the hospital network can extract lesion severity from existing reports with near-cardiologist accuracy and without data leaving the institution. The errors that remain arise from reports that hedge between grades, which standardised reporting would remove. If confirmed prospectively, this approach could keep registries current at negligible cost and free cardiologist time for interpretation rather than transcription.

---

## What changes between versions, and what does not

The headings change, and so does the companion panel (Research in context or a Translational perspective). The case of P changes. EHJ expects both a p value and a CI for the difference, whereas Lancet is satisfied with the CI. Lancet names the design and the reporting guideline in the abstract and npj does not. The clinical implication sits in one sentence in Lancet and in the perspective box in EHJ.

Every number keeps its precision and CI across versions. The claim strength, the abbreviations defined at first use, the absence of citations and promotional words, and the pairing of the headline result with its comparator in one sentence are all unchanged.
