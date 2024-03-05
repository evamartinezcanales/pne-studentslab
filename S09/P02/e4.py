from client0 import Client
from Seq1 import Seq

p = Client("127.0.0.1", 8081)


s = Seq()
gene = "U5"
filename = "U5.txt"
try:
    text = s.read_fasta(filename)
    response = str(p.talk(text))
    print(f"Response: {response}")
except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")
