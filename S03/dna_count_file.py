file = open("dna.txt", "r")
dict = {}
len = 0
for e in file:
    seq = e.replace("\n", "")
    for i in seq:
        if not i in dict:
            dict[i] = 1
        dict[i] += 1

length = int(dict["A"]) + int(dict["T"]) + int(dict["G"]) + int(dict["C"])
print(dict)
print("The length is", length)
file.close()



