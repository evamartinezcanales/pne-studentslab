class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence executed")

    def __len__(self):
        return len(self.strbases)

    def __str__(self):
        return self.strbases


    def generate_pattern(self, pattern, number):
        for i in range(1, number + 1):
            seq = pattern * i
            print("sequence", str(i) + ":", "(Length: " + str(len(seq)) + ")", seq)




sequence1 = Seq("A").generate_pattern("A", 5)

sequence2 = Seq("AC").generate_pattern("AC", 5)

