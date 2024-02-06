
from pathlib import Path
FILENAME = "sequences/RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()
count = 0

contents = file_contents.split("\n")
contents = contents.replace("\n", "")
header = contents[0]
file = contents[1:]
for e in file:
    count += 1
list_contents = file_contents