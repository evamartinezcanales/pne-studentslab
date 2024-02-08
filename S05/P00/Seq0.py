def seq_ping():
    print("Ok")

def seq_read_fasta(filename):
    with open(filename, "r") as f:
        components = f.read()
        index = components.find("\n")
        contents = components[index: ]
    return contents

def seq_len(seq):
    count = 0
    for e in seq:
        count += 1
    return count

def seq_count(seq):
    count = {}
    for e in seq:
        if e == "\n":
            pass
        else:
            if e not in count:
                count[e] = 1
            else:
                count[e] += 1
    return count

def seq_count_base(seq, base):
    count = seq.count(base)
    return count


def seq_reverse(seq):
    seq = seq[::-1]
    return seq

def seq_complement(seq):
    new_seq = ""
    for e in seq:
        if e == "A":
            new_seq += "T"
        elif e == "T":
            new_seq += "A"
        elif e == "G":
            new_seq += "C"
        elif e == "C":
            new_seq += "G"
    return new_seq

def most_common_base(dict):
    list = []
    a_count = int(dict["A"])
    c_count = int(dict["C"])
    t_count = int(dict["T"])
    g_count = int(dict["G"])
    list.append(a_count)
    list.append(c_count)
    list.append(t_count)
    list.append(g_count)
    max_base = max(list)
    base = ""
    if max_base == a_count:
        base = "A"
    elif max_base == c_count:
        base = "C"
    elif max_base == t_count:
        base = "T"
    elif max_base == g_count:
        base = "G"
    return base































