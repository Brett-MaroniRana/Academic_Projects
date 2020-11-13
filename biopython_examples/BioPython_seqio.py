#!/usr/bin/env python3
# BioPython_seqio.py

import sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

def rev_complement(fasta, name):
    for record in SeqIO.parse(fasta, "fasta"):
        sequence = record.seq
        rev_comp = sequence.reverse_complement()
        rev_comp_r = SeqRecord(rev_comp, id = "rev")

    return SeqIO.write(rev_comp_r, name, "fasta")

if __name__ == "__main__":
    fasta = sys.argv[1]
    name = sys.argv[2]
    rev_complement(fasta, name)

