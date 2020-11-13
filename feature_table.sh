#!/usr/bin/env/ bash
# feature_table.sh
# creates feature table that includes multiple statistics

qiime metadata tabulate \
  --m-input-file stats-dada2.qza \
  --o-visualization stats-dada2.qzv
