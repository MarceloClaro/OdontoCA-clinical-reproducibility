# OdontoCA manuscript reproduction

Research-only clinical secondary analysis: 996 eligible tooth transitions, 83 events and 81 children. No external validation or patient-level decision support is established.

## Reproduce

Open `notebooks/OdontoCA_SUBMISSION.ipynb` in Colab and run all cells, or install `requirements.txt` and run `python code/run_submission.py` from this directory. Source Table_S1 is fetched from a fixed source commit and checked with SHA-256. Set LOCAL_TABLE_S1_UI to use an authorized local copy.

The notebook isolates the manuscript analysis from experimental microbiome, image, synthetic and FHIR branches. It uses five outer and three inner child-grouped folds, seed 20260930 and 1,000 child-cluster bootstrap samples. Calibration is fitted within outer-training data. Bootstrap intervals condition on existing out-of-fold predictions and do not include full model-development variability.

## Data provenance

Source: HuangShiLab/Single-tooth-ECC, commit e5868fe5664460c7aac1c5b6d7980776ad26b29c, Figures_and_Tables_in_Manuscript/Table_S1.xlsx. SHA-256: b7819fee81efbe2e227b7700c3cd86ce8bc6f7fe6f49da6214f4107d099184fa. Source publication: https://doi.org/10.1016/j.chom.2025.05.006.

Participant-level third-party source data are not redistributed in this package. Consult source permissions before redistribution. Aggregate tooth counts, aggregate performance and vector/raster figures are included. No patient identifiers or row-level predictions are exported.

## Submission status

Author identities, affiliations, correspondence, CRediT, funding, ethical basis and conflicts remain author-verification items. References and source-derived predictor timing require final scientific verification. Private review repositories: https://github.com/MarceloClaro/OdontoCA-clinical-reproducibility and https://osf.io/edcf9/overview. Access is restricted during preparation. No DOI or prospective registration is asserted.

## Restored manuscript Figure 5
The manuscript uses `manuscript/Figure_5_restored_illustration.png`, restored from the earlier version at the author’s request. Its panel (b) is schematic, not a verified participant-level scatter plot. The data-derived native Figure 5 remains in `figures/` and is reproduced by the notebook.
