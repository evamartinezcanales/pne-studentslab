
correct = True
while correct:
    sequence = input("Enter a sequence")
    sequence = sequence.upper()
    if len(sequence) == (sequence.count("A") + sequence.count("T") + sequence.count("G") + sequence.count("C")):
        print("Total length:", len(sequence))
        correct = False
    else:
        print("Please enter a valid sequence")
dict = {}
for i in sequence:
        if not i in dict:
            dict[i] = 1
        dict[i] += 1

print(dict)