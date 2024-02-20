
def print_blue(seq):
    print("\033[34m" + str(seq) + "\033[0m")
class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence executed")

    def __len__(self):
        return len(self.strbases)

    def __str__(self):
        return self.strbases


    def generate_pattern_blue(self, number):
        for i in range(1, number + 1):
            seq = self.strbases * i
            print("\033[34m" + "sequence", str(i) + ":", "(Length: " + str(len(seq)) + ")", seq + "\033[0m")


    def generate_pattern_green(self, number):
        for i in range(1, number + 1):
            seq = self.strbases * i
            print("\033[32m" + "sequence", str(i) + ":", "(Length: " + str(len(seq)) + ")", seq + "\033[0m")



seq1 = Seq("A")
seq1 =seq1.generate_pattern_blue(3)

sequence2 = Seq("AC")
seq2 = sequence2.generate_pattern_green(2)

