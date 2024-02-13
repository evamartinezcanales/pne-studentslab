from Seq0 import *

class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
            self.strbases = strbases

def print_seqs(seq_list):
    for e in seq_list:
        index = seq_list[e]
        seq = e
        for i in e:
            length = len()

        print(index, length, seq)



seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
p = print_seqs(seq_list)
print(p)






