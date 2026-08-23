# Pipeline mapping

Eleven notebooks, copied from the working directory and renumbered in pipeline
order. The working copies are untouched and remain the historical record.
Version information lives in git history, not in the file name.

Notebooks 01 through 09 run in the order of their numbers. Notebooks 10 and 11
are a side branch: 10 depends on nothing else, 11 needs 02, 03 and 10, and 08
needs 11.

| Step | Notebook | Copied from | Section | Flow | Source code sha256 | Cells |
|---|---|---|---|---|---|---|
| 1 | `01_pkl_to_parquet.ipynb` | `NB03_pkl_to_parquet_v2.ipynb` | - | raw -> processed | `6d651d2ebdd1d51c` | 11 |
| 2 | `02_corner_segmentation.ipynb` | `NB08_corner_segmentation_v4.ipynb` | 3.2 | processed -> features | `db58a7e1a37c3501` | 10 |
| 3 | `03_fingerprint.ipynb` | `NB09_fingerprint_v3.ipynb` | 3.3 | features -> fingerprints | `abfb15180b1305ab` | 12 |
| 4 | `04_corner_type_profile.ipynb` | `NB7A7_corner_type_profile_v2_2026-07-19.ipynb` | 4.2 | features -> corner_type_profiles | `6bd35669a9c8d3f8` | 7 |
| 5 | `05_corner_type_clustering.ipynb` | `NB7A7b_corner_type_viz_v2_2026-07-19.ipynb` | 4.2 | corner_type_profiles -> nb7a7b_info | `48ad05e08db38097` | 16 |
| 6 | `06_tier_ladder.ipynb` | `NB11_tier_pipeline_v3_2_2026-07-22_2100.ipynb` | 4.3 | processed -> t<n>_info | `53467326dd3e1e39` | 16 |
| 7 | `07_cross_car.ipynb` | `NB16_cross_car_identifiability_v5_3_2026-07-22.ipynb` | 4.4 | features -> cross_car | `8587035a1b1b7e76` | 18 |
| 8 | `08_reference_gap.ipynb` | `NB15_sac_gap_analysis_v3_2_2026-07-22_2150.ipynb` | 4.5 | features -> gap_analysis | `4a567dd816b738ca` | 13 |
| 9 | `09_robustness.ipynb` | `NB17_robustness_v1_2026-07-23_1500.ipynb` | 4.2, 4.3 | audit layer | `2fc1faf1ea32c649` | 10 |
| 10 | `10_user_import.ipynb` | `NB13_user_data_csv_to_parquet_v2.ipynb` | 4.5 | MoTeC csv -> user_data | `9f0de653edab7cfc` | 15 |
| 11 | `11_user_portability.ipynb` | `NB14_user_pipeline_v1.ipynb` | 4.5 | user_data -> features | `d17ed752585c64d4` | 16 |

## What was changed in the copy

Two things, and nothing else.

The identity card, which is a markdown cell, and the bootstrap cell that follows
it were inserted at the front of every notebook.

Every hard-coded path was replaced with an expression rooted at the value the
bootstrap cell resolves. The difference between each copy and the file it came
from is confined to lines that carried a path. No other line of code differs.

## The hash column

`Source code sha256` is the SHA-256 of the source notebook's code cells,
concatenated with a NUL separator and truncated to sixteen characters. It names
the working file the copy was taken from. It is not the hash of the copy, and
the two do not agree, because the copy carries the path substitution described
above.

## Verification by re-running

Notebooks 10 and 11 were checked by running them from this repository against
the analysis data, with every write redirected to a scratch directory and every
delete blocked, then comparing the result with the stored outputs. All nineteen
files came back identical, so the path substitution changed no value.

## Provenance

The `notebook` field written into the output JSON records a lineage stem, not a
file name, and it was not updated when a notebook was forked. In the cross-car
notebook all seven v5 forks carry the identical literal, so that field alone
cannot identify which file produced a given output. The canonical assignment in
the table above was established from the output schema instead: the presence of
the `fdr_rej` field, which only the final revision writes.
