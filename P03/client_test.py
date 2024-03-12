from client0 import Client
c = Client("127.0.0.1", 8080)
print(c.talk("PING"))
print(c.talk("GET 3"))
print(c.talk("INFO AACGATA"))
print(c.talk("COMP ACGTCAG"))
print(c.talk("REV ACGTGCA"))
print(c.talk("GENE U5"))
