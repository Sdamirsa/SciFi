<!-- This file is invented for illustration and describes a fictional study. -->

# Methods

## Study design and ethics

This was a retrospective two-centre study of consecutive transthoracic echocardiography reports. The cantonal ethics committee approved the study (approval number 042/21, invented) and waived individual consent because only routinely collected, de-identified reports were used. The study was conducted in accordance with the Declaration of Helsinki. We report the study according to TRIPOD-LLM, and the completed checklist is given in the Supplementary Material, section 1.

## Data source and population

We included consecutive reports written at two Swiss university hospitals (centre A and centre B) between Jan 1, 2022, and Dec 31, 2023 (Figure 1). Reports without a valve assessment, duplicate reports and reports of transoesophageal studies were excluded (Figure 2). Prompts were developed on 200 reports from centre A. The test set comprised 1,000 further reports from both centres, and reports from centre B were not seen before testing.

## Reference standard

Two cardiologists independently labelled every report for the severity of aortic, mitral, tricuspid and pulmonary lesions. Each lesion was graded as none, mild, moderate or severe, following the wording of the report rather than the images. Disagreements between the two cardiologists were resolved by consensus discussion. Agreement before consensus was measured as percentage agreement and as Cohen's kappa with a bootstrap 95% CI.

## Model and comparator

The LLM was an open-weight instruction-tuned model with 70 billion parameters, run without fine-tuning on two graphics processors inside the hospital network. Decoding used temperature 0 with one run per report, and the exact version string and software versions are listed in the Supplementary Material, section 2. The prompt contained a system instruction, the grading definitions and the report, and asked for a structured output with one grade per lesion. The comparator was the rule-based system in clinical use at centre A, applied unchanged to both centres.

## Outcomes and metrics

The primary outcome was per-lesion accuracy, defined as the number of lesions graded identically to the consensus label divided by the number of lesions assessed. The main secondary outcome was accuracy at centre B. Processing time per report was measured from submission of the report to receipt of the structured output. Every error was classified by two authors into predefined categories, including reports that graded a lesion between two categories.

## Statistical analysis

Continuous variables are reported as median with IQR and categorical variables as n with percentage. Accuracy and the difference in accuracy between the LLM and the rule-based system were estimated with 95% CIs from 2,000 bootstrap resamples, clustered by report. No formal sample size calculation was made, and the test set size was fixed by the number of reports available. Analyses used Python with the library versions listed in the Supplementary Material, section 2.

## Role of the funding source

The funder of the study had no role in study design, data collection, data analysis, data interpretation or writing of the report.
