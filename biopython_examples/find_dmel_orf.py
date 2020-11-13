#!/usr/bin/env python3
# find_dmel_orf.py

# import Seq, SeqRecord and SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# import regular expression (re)
import re

# read Drosophila gene sequences. Exclude scaffolding sequences
# for loop. all methods must be within for loop 
for record in SeqIO.parse("/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta", "fasta"):
    if re.match("^\d{1}\D*$", record.id):
        dros_seq = record.seq

        # transcribe genes from dna to rna
        dna = dros_seq
        rna = dna.transcribe()
        
        # find open reading frame
        # find start codon AUG first
        # find first (non-greedy) end codon UAA, UAG, UGA
        # make sure codons are multiples of 3, starting from the first AUG codon
        orf = re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)', str(rna)).group()
               
        # translate open reading frame (orf) to protein
        orf_seq = Seq(orf)
        protein = orf_seq.translate()

        # print each protein in loop
        print(protein)
