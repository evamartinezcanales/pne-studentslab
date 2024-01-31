file = open("dna.txt", "r")
dict = {}
len = 0
with open("dna.txt", "r") as file:
    for e in file:
        seq = e.replace("\n", "")
        for i in seq:
            if not i in dict:
                dict[i] = 1
            dict[i] += 1

length = int(dict["A"]) + int(dict["T"]) + int(dict["G"]) + int(dict["C"])
print("A: " + str(dict["A"]))
print("C: " + str(dict["C"]))
print("T: " + str(dict["T"]))
print("G: " + str(dict["G"]))
print("The length is", length)




