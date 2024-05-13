def valid_bases(strbases):
    valid = True
    for b in strbases:
        if b not in Seq.bases_list:
            valid = False
            break
    return valid

class Seq:
    bases_list = ["A", "C", "T", "G"]
    def __init__(self, strbases=None):
        if strbases is None or len(strbases) == 0:
            self.strbases = "NULL"
            print("Null sequence created")
        elif valid_bases(strbases):
            self.strbases = strbases
        else:
            self.strbases = "ERROR"
            print("INVALID sequence!")

    def __str__(self):
        return self.strbases #--> para poder print bien

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            length = 0
        else:
            length = len(self.strbases)
        return length

    def count_bases(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            count = 0
        else:
            count = self.strbases.count(base)
        return count

    def count(self):
        bases_dict = {}
        for b in Seq.bases_list:
            bases_dict[b] = self.count_bases(b)
        return bases_dict

    def reverse(self):
        if self.strbases == "NULL":
            reverse = "NULL"
        elif self.strbases == "ERROR":
            reverse = "ERROR"
        else:
            reverse = self.strbases[::-1]
        return reverse

    def complement(self):
        complements_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
        complementary_seq = ""
        if self.strbases == "NULL":
            complementary_seq = "NULL"
        elif self.strbases == "ERROR":
            complementary_seq = "ERROR"
        else:
            for b in self.strbases:
                complementary_seq += complements_dict[b]
        return complementary_seq

    def read_fasta(self, filename):
        from pathlib import Path

        file_content = Path(filename).read_text()
        lines = file_content.splitlines()
        body = lines[1:]

        dna_seq = ""
        for line in body:
            dna_seq += line
        self.strbases = dna_seq

    def max_base(self):
        bases_dict = {}
        for b in Seq.bases_list:
            bases_dict[b] = self.count_bases(b)

        most_frequent_base = max(bases_dict, key=bases_dict.get)

        return most_frequent_base

    def info(self):
        s = f"Sequence: {self.strbases} \n" #tambien se puede poner self solo
        s += f"Total length: {self.len()}\n"
        n = ""
        for base, count in self.count().items():
            try:
                percentage = (count * 100) / self.len()
                s += f"{base}: {count} ({percentage:.1f} %)\n" #redondea un decimal al hacer un print
                n += f"{base}: {count} ({percentage:.1f} %)\n"
            except ZeroDivisionError:
                print("null sequence or length 0")
        return s, n





