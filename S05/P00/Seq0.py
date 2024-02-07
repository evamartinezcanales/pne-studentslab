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