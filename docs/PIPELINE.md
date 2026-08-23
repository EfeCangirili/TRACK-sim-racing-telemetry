# Pipeline mapping

Nine notebooks, copied verbatim from the working directory and renamed in
pipeline order. The working copies under `notebooks/` are untouched and remain
the historical record. Version information lives in git history, not in the
file name.

| Step | Notebook | Copied from | Section | Flow | Code sha256 | Cells |
|---|---|---|---|---|---|---|
| 1 | `01_pkl_to_parquet.ipynb` | `NB03_pkl_to_parquet_v2.ipynb` | - | raw -> processed | `6d651d2ebdd1d51c` | 11 |
| 2 | `02_corner_segmentation.ipynb` | `NB08_corner_segmentation_v4.ipynb` | 3.2 | processed -> features | `db58a7e1a37c3501` | 10 |
| 3 | `03_fingerprint.ipynb` | `NB09_fingerprint_v3.ipynb` | 3.3 | features -> fingerprints | `abfb15180b1305ab` | 12 |
| 4 | `04_corner_type_profile.ipynb` | `NB7A7_corner_type_profile_v2_2026-07-19.ipynb` | 4.2 | features -> corner_type_profiles | `6bd35669a9c8d3f8` | 7 |
| 5 | `05_corner_type_clustering.ipynb` | `NB7A7b_corner_type_viz_v2_2026-07-19.ipynb` | 4.2 | corner_type_profiles -> nb7a7b_info | `48ad05e08db38097` | 16 |
| 6 | `06_tier_ladder.ipynb` | `NB11_tier_pipeline_v3_2_2026-07-22_2100.ipynb` | 4.3 | processed -> t<n>_info | `53467326dd3e1e39` | 16 |
| 7 | `07_cross_car.ipynb` | `NB16_cross_car_identifiability_v5_3_2026-07-22.ipynb` | 4.4 | features -> cross_car | `8587035a1b1b7e76` | 18 |
| 8 | `08_reference_gap.ipynb` | `NB15_sac_gap_analysis_v3_2_2026-07-22_2150.ipynb` | 4.5 | features -> gap_analysis | `4a567dd816b738ca` | 13 |
| 9 | `09_robustness.ipynb` | `NB17_robustness_v1_2026-07-23_1500.ipynb` | 4.3 | denetim katmani | `2fc1faf1ea32c649` | 10 |

## Verification

The `Code sha256` column is the SHA-256 of the concatenated code cells, joined
with a NUL separator. It is identical in the copy and in the source, which is
the evidence that no code cell was modified during the copy. The only addition
to each copy is a markdown identity card inserted as the first cell.

## Provenance

The `notebook` field written into the output JSON records a lineage stem, not a
file name, and it was not updated when a notebook was forked. In the cross-car
notebook all seven v5 forks carry the identical literal, so that field alone
cannot identify which file produced a given output. The canonical assignment in
the table above was established from the output schema instead: the presence of
the `fdr_rej` field, which only the final revision writes.