def seq_reverse(seq):
    seq = seq[::-1]
    return seq
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

    def count_bases(self):
        check = check_seq(self.strbases)
        count = {}
        if check == True:
            for e in self.strbases:
                if e not in count:
                    count[e] = 1
                else:
                    count[e] += 1
        else:
            count = {"A":0, "T": 0, "G":0, "C":0}
        return count

    def len(self):
        check = check_seq(self.strbases)
        if check == True:
            return len(self.strbases)
        else:
            return 0

    def get_reverse(self):
        check = check_seq(self.strbases)
        if check == True:
            reverse = self.strbases[::-1]
        else:
            reverse = "ERROR"
        return reverse

    def get_complement(self):
        check = check_seq(self.strbases)
        new_seq =""
        if self.strbases == "":
            new_seq = "NULL"
        else:
            if check == True:
                for e in self.strbases:
                    if e == "A":
                        new_seq += "T"
                    elif e == "T":
                        new_seq += "A"
                    elif e == "C":
                        new_seq += "G"
                    elif e == "G":
                        new_seq += "C"
            else:
                new_seq = "ERROR"
        return new_seq


s1 = Seq("AGTACACTGGT")
s2 = Seq("ABDUYW")
s3 = Seq("")
print("s1: ", "(length:", s1.len(), ")", s1.strbases)
print(s1.count_bases())
print(s1.get_reverse())
print(s1.get_complement())
print("s2: ", "(length:", s2.len(), ")", s2.strbases)
print(s2.count_bases())
print(s2.get_reverse())
print(s2.get_complement())
print("s3: ", "(length:", s3.len(), ")", s3.strbases)
print(s3.count_bases())
print(s3.get_reverse())
print(s3.get_complement())