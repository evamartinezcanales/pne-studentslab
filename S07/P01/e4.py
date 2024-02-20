def check_seq(seq):
    if len(seq) == seq.count("A") + seq.count("T") + seq.count("G") + seq.count("C"):
        seq = True
    else:
        seq = False
    return seq

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        check = check_seq(strbases)
        if strbases == "":
            self.strbases = "NULL"
        else:
            if check == True:
                self.strbases = strbases
                print("New sequence created!")
            else:
                self.strbases = "ERROR"
                print("INVALID SEQ")

    def __str__(self):
        return self.strbases

    def len(self):
        check = check_seq(self.strbases)
        if check == True:
            return len(self.strbases)
        else:
            return 0


s1 = Seq("AGTACACTGGT")
s2 = Seq("ABDUYW")
s3 = Seq("")
print("s1: ", "(length:", s1.len(), ")", s1.strbases)
print("s2: ", "(length:", s2.len(), ")", s2.strbases)
print("s3: ", "(length:", s3.len(), ")", s3.strbases)