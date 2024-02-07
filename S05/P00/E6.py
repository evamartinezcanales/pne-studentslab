from Seq0 import *
seq_u5 = seq_read_fasta("U5.txt")
seq = seq_u5[0:21]
print(seq_reverse(seq))
