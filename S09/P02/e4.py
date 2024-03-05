from client0 import Client
p = Client("127.0.0.1", 8081)
with open ("U5.txt") as f:
    text = ""
    for e in f:
        text += e

response = p.talk(text)
print(f"Response: {response}")