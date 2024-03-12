from client0 import Client
practice = 3
exercise = 7
N = 5
bases = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
print(f"-----|PRACTICE {practice}, EXERCISE {exercise}-----|")
c = Client("127.0.0.1", 8080)

print("*Testing PING...")
response = c.talk("PING")

print("* Testing GET...")
for n in range(N):
    response = c.talk(f"GET {n}")
    print(f"GET {n}: {response} ")
print("")

print("*Testing INFO...")
response = c.talk(f"INFO {bases}")
print(response)
print("")

print("*Testing COMP...")
print(f"COMP {bases}")
response = c.talk(f"COMP {bases}")
print(response)
print("")

print("*Testing REV...")
print(f"REV {bases}")
response = c.talk(f"REV {bases}")
print(response)
print("")

print("*Testing GENE...")
genes = ["U5", "ADA", "FRAT1","FXN", "RNU6_269P"]
for g in genes:
    print(f"GENE {g}")
    response = c.talk(f"GENE {g}")
    print(response)
