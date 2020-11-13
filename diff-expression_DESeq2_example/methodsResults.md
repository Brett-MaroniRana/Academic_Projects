# Differential Gene Expression using salmon and DESeq2

## Overview

The two main steps in performing differential expression analysis are to
estimate the relative abundance of transcripts, and to apply statistical
models to test for differential expression between treatment groups.
Estimating relative abundance is basically determining how many NGS
reads match a given gene within a genome. In this module you’ll use
Salmon (Patro et al. 2017) to estimate relative abundance, tximport
(Soneson, Love, and Robinson 2015) to import the Salmon abundance
estimates, and DESeq2 (Love, Huber, and Anders 2014) to perform
statistical tests to identify differentially expressed genes.

## Method

Three main steps took place to produce the results below. First, salmon
was used to perform abundance of gene expression estimations on a
previously sequenced transcriptome. To do this an index of the de-novo
transcriptome was first created. Once the index was created, the left
and right reads are aligned to the index. This was all done using
salmon. Second, transcripts were mapped to genes. This was accomplished
by merging annotation tables together in R. The transcript BLAST file
was merged with a file containing kegg elements, then that BLAST and
kegg merged file was merged with a ko file. The end result is a file
with transcripts, kegg and ko elements, all mapped to each other by use
of merge functionality in R. Finally, we are ready to process the salmon
alignments with DESeq2 to perform differential expression. This utilizes
DESeq2
algorithm.

## Results

``` r
knitr::kable(filtered_res, caption = "results")
```

|            | log2FoldChange |      padj | Factor                        |
| ---------- | -------------: | --------: | :---------------------------- |
| ko:K04354  |    \-2.0688144 | 0.0273004 | Menthol\_Menthol\_vs\_Control |
| ko:K13785  |    \-2.6725894 | 0.0000154 | Menthol\_Menthol\_vs\_Control |
| ko:K14965  |    \-6.1770315 | 0.0000000 | Menthol\_Menthol\_vs\_Control |
| ko:K17920  |      1.1188285 | 0.0000011 | Menthol\_Menthol\_vs\_Control |
| ko:K20369  |      0.6055154 | 0.0163337 | Menthol\_Menthol\_vs\_Control |
| ko:K004691 |    \-0.5532535 | 0.0493894 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K006431 |      1.4399936 | 0.0000286 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K012061 |      3.2300925 | 0.0000163 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K012511 |      1.9685457 | 0.0007990 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K015961 |      2.9552312 | 0.0000000 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K016811 |      1.4075102 | 0.0026161 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K021831 |    \-0.5741213 | 0.0186218 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K028721 |    \-2.4633854 | 0.0272584 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K028731 |    \-1.6212250 | 0.0002488 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K030071 |    \-3.4483643 | 0.0003189 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K036261 |      2.3913357 | 0.0000163 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K057541 |      1.1688075 | 0.0014172 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K089571 |      2.1818883 | 0.0206200 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K095691 |      2.4814138 | 0.0116372 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K107041 |      1.2504437 | 0.0152969 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K147531 |      0.7922773 | 0.0012900 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K161861 |      2.3335409 | 0.0014612 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K197651 |    \-0.4823249 | 0.0000838 | Vibrio\_Vibrio\_vs\_Control   |
| ko:K203691 |    \-0.6191226 | 0.0026161 | Vibrio\_Vibrio\_vs\_Control   |

results

### References

<div id="refs" class="references">

<div id="ref-Love">

Love, Michael I., Wolfgang Huber, and Simon Anders. 2014. “Moderated
Estimation of Fold Change and Dispersion for RNA-Seq Data with DESeq2.”
*Genome Biol* 15 (12): 550–50.
<https://doi.org/10.1186/s13059-014-0550-8>.

</div>

<div id="ref-Patro">

Patro, Rob, Geet Duggal, Michael I. Love, Rafael A. Irizarry, and Carl
Kingsford. 2017. “Salmon Provides Fast and Bias-Aware Quantification of
Transcript Expression.” *Nat Methods* 14 (4): 417–19.
<https://doi.org/10.1038/nmeth.4197>.

</div>

<div id="ref-Soneson">

Soneson, Charlotte, Michael I. Love, and Mark D. Robinson. 2015.
“Differential Analyses for RNA-Seq: Transcript-Level Estimates Improve
Gene-Level Inferences.” *F1000Res* 4 (December): 1521–1.
<https://pubmed.ncbi.nlm.nih.gov/26925227>.

</div>

</div>
