# Microbiome Analysis: qiime2

## Overview

Qiime2 (Bolyen et al. 2019) (pronounced “chime”) is a powerful
bioinformatic tool designed for microbiome data analysis. It provides
end to end data analysis, from sequence import through scientific paper
quality data visualization.

Running qiime2 creates qiime artifacts and visualizations. Qiime
artifacts are denoted by .gza file extension. Qiime visualizations are
denoted by .gzv file extension. Qiime artifacts are used in downstream
processing, usually for further analysis, while visualizations are
terminal and are designed to be viewed as output. Qiime artifacts
contain semantics. This dictate what a particular artifact can do. This
can be very useful for controlling what analysis is done with what
artifacts, minimizing errors and erroneous results. Lastly, plugins
(software packages) allow for data analysis of qiime artifacts and
visualization through the use of methods and visualizers found in the
plugin.

## Methods

Qiime2 provides documentation guiding new users through tutorials that
walk you though the process of microbiome data analysis.

The first tutorial uses data from (Caporaso et al. 2011) that looks at
two individuals whom swab four body sites, at five time-points, with and
without antibiotics. This tutorial walks through each step of qiime2
microbiome data analysis and can be found
[here](https://docs.qiime2.org/2020.8/tutorials/moving-pictures/#sample-metadata).
Two more tutorials, (Kang et al. 2017) and (Neilson et al. 2017) build
on the “Moving Pictures” tutorial but cover additional functionalityof
qiime2. These can be found
[here](https://docs.qiime2.org/2020.8/tutorials/fmt/) and
[here](https://docs.qiime2.org/2020.8/tutorials/atacama-soils/).

### References

<div id="refs" class="references">

<div id="ref-qiime2">

Bolyen, Evan, Jai Ram Rideout, Matthew R. Dillon, Nicholas A. Bokulich,
Christian C. Abnet, Gabriel A. Al-Ghalith, Harriet Alexander, et al.
2019. “Reproducible, Interactive, Scalable and Extensible Microbiome
Data Science Using QIIME 2.” *Nature Biotechnology* 37 (8): 852–57.
<https://doi.org/10.1038/s41587-019-0209-9>.

</div>

<div id="ref-pictures">

Caporaso, J. Gregory, Christian L. Lauber, Elizabeth K. Costello, Donna
Berg-Lyons, Antonio Gonzalez, Jesse Stombaugh, Dan Knights, et al. 2011.
“Moving Pictures of the Human Microbiome.” *Genome Biology* 12 (5): R50.
<https://doi.org/10.1186/gb-2011-12-5-r50>.

</div>

<div id="ref-fmt">

Kang, Dae-Wook, James B. Adams, Ann C. Gregory, Thomas Borody, Lauren
Chittick, Alessio Fasano, Alexander Khoruts, et al. 2017. “Microbiota
Transfer Therapy Alters Gut Ecosystem and Improves Gastrointestinal and
Autism Symptoms: An Open-Label Study.” *Microbiome* 5 (1): 10.
<https://doi.org/10.1186/s40168-016-0225-7>.

</div>

<div id="ref-atacama">

Neilson, Julia W., Katy Califf, Cesar Cardona, Audrey Copeland, Will van
Treuren, Karen L. Josephson, Rob Knight, et al. 2017. “Significant
Impacts of Increasing Aridity on the Arid Soil Microbiome.” *mSystems* 2
(3): e00195–16. <https://doi.org/10.1128/mSystems.00195-16>.

</div>

</div>
