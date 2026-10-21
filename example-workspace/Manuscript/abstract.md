<!-- This file is invented for illustration and describes a fictional study. Copied from skills/scientific-writing/examples/abstract-variants.md (Lancet version). -->

# Abstract

**Background** Echocardiography reports are the main source of valvular heart disease (VHD) severity for registries, but severity is recorded as free text and abstracted by hand. We assessed whether an open-weight large language model (LLM) deployed inside a hospital network can extract VHD severity accurately across two centres.

**Methods** In this retrospective study, we included consecutive transthoracic echocardiography reports from two university hospitals in Switzerland between Jan 1, 2022, and Dec 31, 2023. Two cardiologists labelled each report for the severity of aortic, mitral, tricuspid and pulmonary lesions, with consensus adjudication. A 70-billion-parameter open-weight LLM was prompted without fine-tuning and compared with a rule-based system. Prompts were developed on 200 reports from centre A and tested on 1,000 reports from both centres. The primary outcome was per-lesion accuracy, with 95% CIs obtained by bootstrap. The study followed TRIPOD-LLM.

**Findings** Of 1,200 reports, 1,000 formed the test set. Median patient age was 71 years (IQR 62 to 79) and 418 (41.8%) were women. The LLM achieved an accuracy of 96.3% (95% CI 95.1 to 97.4) compared with 88.7% (87.0 to 90.4) for the rule-based system (difference 7.6 percentage points, 5.8 to 9.4). Accuracy at centre B, not used for prompt development, was 95.8% (93.9 to 97.5). Mean processing time was 4.1 s per report. 24 (64.9%) of 37 LLM errors occurred in reports that graded a lesion between two categories.

**Interpretation** An open-weight LLM run within hospital infrastructure extracted VHD severity from echocardiography reports more accurately than a rule-based system, including at an external centre, and could support registry completion if validated prospectively.

**Funding** [Funder].


## Research in context

*Evidence before this study* We searched PubMed and Embase on March 1, 2024, for "large language model" AND "echocardiography" AND ("extraction" OR "classification") without language restriction and found nine studies. All used single-centre data, six used proprietary models that require sending reports outside the hospital, and none reported external evaluation.

*Added value of this study* We show that an open-weight model deployed locally reaches 96.3% accuracy and holds its performance at a second centre, with errors concentrated in ambiguous grading language.

*Implications of all the available evidence* Locally deployed LLMs can populate VHD registries from existing reports without data leaving the hospital. Prospective validation and report standardisation should precede routine use.
