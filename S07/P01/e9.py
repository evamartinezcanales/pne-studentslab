from Seq1 import Seq
import os
s = Seq()

gene = "U5"


filename = "U5.txt"

try:
    s.read_fasta(filename)
    print(f"Sequence: (length: {s.len()} {s} \n Bases: {s.count()} \n Rev: {s.reverse()} \n Comp: {s.complement()}")
except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")
