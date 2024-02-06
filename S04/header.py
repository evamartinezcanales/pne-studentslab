from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "sequences/RNU6_269P.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console


file_contents = file_contents.split("\n")
print(file_contents[0])