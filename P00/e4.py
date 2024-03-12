import os
from Seq0 import *

GENES = ["U5", "ADA", "FRAT1", "FXN"]
BASES = ["A", "C", "T", "G"]

for gene in GENES:
    filename = os.path.join(gene + ".txt")
    try:
        dna_sequence = seq_read_fasta(filename)
        print(f"Gene {gene}:")
        for base in BASES:
            print(f"\t{base}: {seq_count_base(dna_sequence, base)}")
    except FileNotFoundError:
        print(f"[ERROR]: file '{filename}' not found")
