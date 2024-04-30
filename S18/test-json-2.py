import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-2.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'
firstname = person['Firstname']
lastname = person['Lastname']
age = person['age']
phoneNumber = person["phoneNumber"]
# Print the information on the console, in colors

print()
termcolor.cprint("Name: ", 'green', end="")
print(firstname, lastname)
termcolor.cprint("Age: ", 'green', end="")
print(age)

# Get the phoneNumber list
phoneNumbers = person['phoneNumber']

# Print the number of elements int the list
termcolor.cprint("Phone numbers: ", 'green', end='')
print(len(phoneNumbers))

# Print all the phone numbers
for i, num in enumerate(phoneNumbers):  # genera una lista de tuplas con la posición y su valor correcpondiente
    termcolor.cprint("  Phone " + str(i) + ": ", 'blue', end='')
    print(num)
