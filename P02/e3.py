from client0 import Client
p = Client("127.0.0.1", 8081)
print(p)
response = p.talk("Testing!!!")
print(f"Response: {response}")
