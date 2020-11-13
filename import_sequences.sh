#!/usr/bin/env bash
# import_sequences.sh

wget \
  -O "emp-single-end-sequences/barcodes.fastq.gz" \
  "https://data.qiime2.org/2020.8/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz"

wget \
  -O "emp-single-end-sequences/sequences.fastq.gz" \
  "https://data.qiime2.org/2020.8/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz"

qiime tools import \
  --type EMPSingleEndSequences \
  --input-path emp-single-end-sequences \
  --output-path emp-single-end-sequences.qza
