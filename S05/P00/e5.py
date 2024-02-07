from Seq0 import *
seq_u5 = seq_read_fasta("U5.txt")
print("Gene U5: " + str(seq_count(seq_u5)))

seq_ada = seq_read_fasta("ADA.txt")
print("Gene ADA: " + str(seq_count(seq_ada)))

seq_frat = seq_read_fasta("FRAT1.txt")
print("Gene FRAT1: " + str(seq_count(seq_frat)))

seq_fxn = seq_read_fasta("FXN.txt")
print("Gene FNX: " + str(seq_count(seq_fxn)))
