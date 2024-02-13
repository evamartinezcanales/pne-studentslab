from Seq0 import *

class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        check = check_seq(strbases)
        if check == True:
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("ERROR")


# Main program
# Create objects of the class Seq
s1 = Seq("AGTACACTGGT")
s2 = Seq("ABDUYW")

print("s1: ", s1.strbases)
print("s2: ", s2.strbases)
