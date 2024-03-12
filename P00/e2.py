import os
from Seq0 import *

N = 20

dna_file = input("DNA file: ")
try:
    filename = os.path.join(dna_file + ".txt")
    dna_sequence = seq_read_fasta(filename)
    print(f"The first {N} bases are:")
    print(dna_sequence[:N])
except IndexError:
    print(f"[ERROR]: DNA sequence has not almost {N} bases")
