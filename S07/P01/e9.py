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
            count = {"A": 0, "T": 0, "G": 0, "C": 0}
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
        new_seq = ""
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

    def read_fasta(self, filename):
        seq = ""
        with open(filename, 'r') as file:
            for line in file:
                for e in line:
                    seq += str(e)
        self.strbases = seq
        return self.strbases





s = Seq("")
seq = str(s.read_fasta("U5.txt"))
print("seq: ", "(length:", seq.len(), ")", seq.strbases)
print(seq.count_bases())
print(seq.get_reverse())
print(seq.get_complement())
