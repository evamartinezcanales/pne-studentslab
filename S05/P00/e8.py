from Seq0 import *

seq = seq_read_fasta("U5.txt")
dict = seq_count(seq)
max_base = most_common_base(dict)
print("Gene U5: Most frequent Base:", max_base)

seq = seq_read_fasta("ADA.txt")
dict = seq_count(seq)
max_base = most_common_base(dict)
print("Gene ADA: Most frequent Base:", max_base)


seq = seq_read_fasta("FRAT1.txt")
dict = seq_count(seq)
max_base = most_common_base(dict)
print("Gene FRAT1: Most frequent Base:", max_base)


seq = seq_read_fasta("FXN.txt")
dict = seq_count(seq)
max_base = most_common_base(dict)
print("Gene FXN: Most frequent Base:", max_base)
