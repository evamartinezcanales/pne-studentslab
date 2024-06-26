import os
from Seq0 import *

GENES = ["U5", "ADA", "FRAT1", "FXN"]

for gene in GENES:
    filename = os.path.join(gene + ".txt")
    try:
        dna_sequence = seq_read_fasta(filename)
        print(f"Gene {gene}: {seq_count(dna_sequence)}")
    except FileNotFoundError:
        print(f"[ERROR]: file '{filename}' not found")
