#!/usr/bin/env python3
# sliding_window_fasta.py

import sys
import re
import os
from Bio import SeqIO

def sliding_window(k, fasta):
    fasta_seq = []
    end = len(fasta) - k + 1
    for start in range(0, end):
        fasta_seq.append(fasta[start:start + k])

    return fasta_seq

def gc_content(dna):
    dna = dna.lower()

    # count g's and c's
    gc = 0
    for nucs in dna:
        if nucs in ['g', 'c']:
            gc += 1

    return gc/len(dna)

if __name__ == "__main__":

    arg_count = len(sys.argv) - 1
    if arg_count < 2:
        raise Exception("This script requires 2 arguments")
    
    # program paramaters
    k = int(sys.argv[1])
    fasta_file = sys.argv[2]

    # open file and read
    # use SeqIO method
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
        # program function result
        kmers = sliding_window(k, seq_record.seq)
        # loop through dna to find kmers and gc content
    for kmer in kmers:
        print("{}\t{:.2}".format(kmer, gc_content(kmer)))
