from client0 import Client
p = Client("127.0.0.1", 8081)
with open ("FRAT1.txt") as f:
    text = ""
    for e in f:
        if e <= 10:
            text += e
