import os
from Seq1 import Seq


GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]


for gene in GENES:
    filename = os.path.join(gene + ".txt")
    try:
        s = Seq()
        s.read_fasta(filename)
        print(f"Gene {gene}: {s.max_base()}")
    except FileNotFoundError:
        print(f"[ERROR]: file '{filename}' not found")
