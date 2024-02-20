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
        if self.strbases == "":
            self.strbases = "Null"
        else:
            if check == True:
                self.strbases = strbases
                print("New sequence created!")
            else:
                self.strbases = "ERROR"
                print("INVALID SEQ")

    def __str__(self):
        return self.strbases

s1 = Seq("AGTACACTGGT")
s2 = Seq("ABDUYW")
s3 = Seq("")
print("s1: ", s1.strbases)
print("s2: ", s2.strbases)
