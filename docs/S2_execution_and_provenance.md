# Supplementary File S2 Execution and provenance

The clinical submission notebook was run from start to finish in this workspace on 2026-10-03. Cohort invariants, held-out child separation, probability coverage, forbidden predictor exclusion, metric agreement, proportional marker area, lower-incisor placement and native raster dimensions passed.

The runtime used Python 3.12.14. Exact package versions are in requirements.txt and results/runtime_versions.json. Source SHA-256 and group-split policy are recorded in results/clinical_internal_validation.json. Primary AUROC and average precision matched the existing Colab outputs; minor floating-point differences did not change manuscript rounding. Bootstrap intervals reproduced the reported values.

Intervals condition on fixed out-of-fold predictions; models are not refitted within the bootstrap. Selected C is held fixed when generating inner cross-fitted probabilities for recalibration, so the full held-out outer evaluation remains the relevant performance evidence. Historical 1.6.1/1.9.0 cross-version execution and earlier notebook audit claims are not independently reverified in this package.

The distributable source data are aggregate only. Raw third-party data remain downloadable from the original source rather than being rehosted without confirmed redistribution rights.
