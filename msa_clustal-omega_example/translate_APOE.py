#!/usr/bin/env python3
# translate_APOE.py

from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# grab headers and sequences using BioPython
# will create Seq() object
headers = []
sequences = []
for seq_record in SeqIO.parse("APOE_refseq_transcript.fasta", "fasta"):
    header = seq_record.description
    headers_list = headers.append(header)
    seq = seq_record.seq
    sequences_list = sequences.append(seq)
#print(headers)
#print(sequences)

# transcribe Seq() object to RNA
# uses .transcribe() "method"
rnas = []
for i in range(len(sequences)):
    rna = sequences[i].transcribe()
    rna_list = rnas.append(rna)
#print(rnas)

# translate RNAs (still Seq() object) to Protein
# use .translate() method
proteins = []
for i in range(len(rnas)):
    protein = rnas[i].translate()
    protein_list = proteins.append(protein)
#print(proteins)

# make each protein Seq() object a SeqRecord() object
# use headers as id
pro_seq_records = []
for i in range(len(proteins)):
    seq_record = SeqRecord(proteins[i], headers[i])
    seq_record_list = pro_seq_records.append(seq_record)
#print(pro_seq_records[0])

# write to file in .fasta format
for i in range(len(pro_seq_records)):
    SeqIO.write(pro_seq_records, "apoe_aa.fasta", "fasta")
print("\nTranslation Complete!\n")
