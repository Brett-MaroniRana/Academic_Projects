#!/usr/bin/env bash
# feature_table_summarize.sh
# summarize the feature table with info on number of sequences associated with each sample
# and with each feature
# will also map feature IDs to sequences with a link to blast to compare

qiime feature-table summarize \
  --i-table table.qza \
  --o-visualization table.qzv \
  --m-sample-metadata-file sample-metadata.tsv
qiime feature-table tabulate-seqs \
  --i-data rep-seqs.qza \
  --o-visualization rep-seqs.qzv
