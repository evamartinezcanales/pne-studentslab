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

    # Function to print a sequence list in blue
def print_blue(seq):
    seq = "\033[34m" + str(seq) + "\033[0m"
    print(seq)
    return seq

# Function to print a sequence list in green
def print_green(seq):
    print("\033[32m" + str(seq) + "\033[0m")


# Usage of the code
seq1 = print_blue(Seq("AT").generate_pattern("AT", 5))
seq_2 = print_green(Seq("GC").generate_pattern("GC", 5))


