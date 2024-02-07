from Seq0 import *

seq_u5 = seq_read_fasta("U5.txt")
print("Gene U5 -> Length: " + str(seq_len(seq_u5)))

seq_ada = seq_read_fasta("ADA.txt")
print("Gene ADA -> Length: " + str(seq_len(seq_ada)))

seq_frat = seq_read_fasta("FRAT1.txt")
print("Gene FART1 -> Length: " + str(seq_len(seq_frat)))

seq_fxn = seq_read_fasta("FXN.txt")
print("Gene FXN -> Length: " + str(seq_len(seq_fxn)))

