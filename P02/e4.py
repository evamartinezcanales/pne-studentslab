from client0 import Client
from Seq1 import Seq
import os

p = Client("127.0.0.1", 8081)
print(p)


genes = ["U5", "FRAT1", "ADA"]
for g in genes:
    filename = os.path.join(g + ".txt") #esta instrucción nunc falla, no genera ninguna excepción por eso no la metemos en el try
    try:
        s = Seq()
        s.read_fasta(filename) #cargas la secuencia nula con el contenido del fichero

        msg = f"sending {g} Gene to the server"
        print(f"To server: {msg}")
        response = p.talk(msg)
        print(f"From server: {response}")

        msg = str(s) #fuerza a llamar a __str__, msg s.__str__(), msg = f"{s}"
        print(f"To server: {msg}")
        response = p.talk(msg)
        print(f"From server: {response}")
    except FileNotFoundError:
        print(f"[ERROR]: file '{filename}' not found")  #para que no muera el programa


