#!/usr/bin/env python3
# BioPython_seq.py

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

seq = Seq("aaaatgggggggggggccccgtt", generic_dna)

seq_r = SeqRecord(
        seq, id = "#12345", description = "example 1")

print(seq_r)

SeqIO.write(seq_r, "BioPython_seq.gb", "genbank")
