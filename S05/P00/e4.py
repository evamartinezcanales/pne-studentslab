from Seq0 import *

seq_u5 = seq_read_fasta("U5.txt")
a_count = seq_count_base(seq_u5, "A")
c_count = seq_count_base(seq_u5, "C")
t_count = seq_count_base(seq_u5, "T")
g_count = seq_count_base(seq_u5, "G")
print("Gene U5")
print(" A: ", a_count)
print(" C: ", c_count)
print(" T: ", t_count)
print(" G: ", g_count)


seq = seq_read_fasta("ADA.txt")
a_count = seq_count_base(seq, "A")
c_count = seq_count_base(seq, "C")
t_count = seq_count_base(seq, "T")
g_count = seq_count_base(seq, "G")
print("Gene ADA")
print(" A: ", a_count)
print(" C: ", c_count)
print(" T: ", t_count)
print(" G: ", g_count)


seq = seq_read_fasta("FRAT1.txt")
a_count = seq_count_base(seq, "A")
c_count = seq_count_base(seq, "C")
t_count = seq_count_base(seq, "T")
g_count = seq_count_base(seq, "G")
print("Gene FRAT1")
print(" A: ", a_count)
print(" C: ", c_count)
print(" T: ", t_count)
print(" G: ", g_count)

seq = seq_read_fasta("FXN.txt")
a_count = seq_count_base(seq, "A")
c_count = seq_count_base(seq, "C")
t_count = seq_count_base(seq, "T")
g_count = seq_count_base(seq, "G")
print("Gene FXN")
print(" A: ", a_count)
print(" C: ", c_count)
print(" T: ", t_count)
print(" G: ", g_count)



