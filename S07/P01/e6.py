from Seq1 import Seq

s1 = Seq("AGTACACTGGT")
s2 = Seq("ABDUYW")
s3 = Seq("")
print("s1: ", "(length:", s1.len(), ")", s1.strbases)
print(s1.count())
print("s2: ", "(length:", s2.len(), ")", s2.strbases)
print(s2.count())
print("s3: ", "(length:", s3.len(), ")", s3.strbases)
print(s3.count())