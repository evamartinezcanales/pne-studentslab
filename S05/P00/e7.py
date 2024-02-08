from Seq0 import *

seq_u5 = seq_read_fasta("U5.txt")
new_seq = seq_complement(seq_u5)
print(new_seq[0:21])