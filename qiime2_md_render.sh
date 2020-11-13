#!/usr/bin/env bash
# qiime2_md_render.sh

R -e "rmarkdown::render('qiime2_md_methods.Rmd', output_format ='all')"


