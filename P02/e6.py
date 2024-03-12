from client0 import Client
from Seq1 import Seq
import os
number_of_fragments = 10
number_of_bases = 10
last_base = 0

p = Client("192.168.0.30", 8081)
print(p)
c = Client("192.168.0.30", 8080)
print(c)

gene = ["FRAT1"]
for g in gene:
    filename = os.path.join(str(g) + (".txt"))
    try:
        s = Seq()
        s.read_fasta(filename)  # cargas la secuencia nula con el contenido del fichero
        p.talk(f"Sending gene {gene} to server, in fragments of {number_of_bases}")
        c.talk(f"Sending gene{gene} to server, in fragments of {number_of_bases}")
        print(f"Gene {gene}: {s}")
        s = str(s)

        for i in range (1, number_of_fragments + 1): #range(0,3) el 3 no está incluido
            #si ponemos range_of_fragments habrá 5 interacciones porque empieza a contar desde el 0
            if i % 2 != 0:
                msg = (f"Fragment {i}: {s[last_base:number_of_bases]} ")
                print(msg)
                c.talk(msg)
            elif i % 2 == 0:
                msg = (f"Fragment {i}: {s[last_base:number_of_bases]} ")
                print(msg)
                p.talk(msg)
            number_of_bases += 10
            last_base += 10

    except FileNotFoundError:
        print(f"[ERROR]: file '{filename}' not found")