#!/usr/bin/env bash
# alignAll.sh

# initialize var to contain dir of fastq files
fastqPath="/scratch/SampleDataFiles/Paired/"

# initialize var to contain left (R1) and right (R2) suffix
leftSuffix=".R1.paired.fastq"
rightSuffix=".R2.paired.fastq"


outDir='quant/'
sample=$sampleName

# align all function
function align {
    for file in $fastqPath*$leftSuffix
    do
        # remove path from file -  pathRemoved; ex aip02.R1.paired.fastq
        pathRemoved="${file/$fastqPath/}"

        # remove suffix from $pathRemoved, assign to $sampleName
        sampleName="${pathRemoved/$leftSuffix/}"
        echo $sampleName
        
        # run salmon with variables
        salmon quant -l IU is \
        -1 $fastqPath$sampleName$leftSuffix \
        -2 $fastqPath$sampleName$rightSuffix  \
        -i AipIndex \
        --validateMappings \
        -o $outDir$sampleName
    done
}

align 1>align.log 2>align.err &


