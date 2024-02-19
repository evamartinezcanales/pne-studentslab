from Seq0 import *

class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
            self.strbases = strbases

    def print_seqs(seq_list):
        count = 0
        for e in seq_list:
            index = seq_list.index(e)
            seq = str(e)
            length = len(seq)
            print("sequence", index, "(lenght", length, ")", seq)

        return index, length, seq


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
index, length, seq = Seq.print_seqs(seq_list)







