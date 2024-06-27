import http.client
import json
from http import HTTPStatus

SERVER = 'localhost'
PORT = 8080

connection = http.client.HTTPConnection(SERVER, port=PORT)

try:
    connection.request("GET", "/karyotype?species=mouse&json=1")
except ConnectionRefusedError:
    print("We cannot connect to the server")
    exit()
response = connection.getresponse()
print(f"Response received!: {response.status} {response.reason}\n")
if response.status == HTTPStatus.OK:
    data_str = response.read().decode()
    data = json.loads(data_str)
    print(data)
    specie = data['specie']
    karyotype = data['karyotype']
    print(specie, karyotype)


try:
    connection.request("GET", "/listSpecies?limit=10&json=1")
except ConnectionRefusedError:
    print("Cannot connect to the Server")
    exit()
response = connection.getresponse()
print(f"Response received!: {response.status} {response.reason}\n")
if response.status == HTTPStatus.OK:
    data_str = response.read().decode()
    data = json.loads(data_str)
    print(data)
    limit = int(data["limit"])
    number_species = data['number_of_species']
    name_species = data['name_species']
    species = ""
    for i in name_species:
        species += i
    print(number_species, species)


try:
    connection.request("GET", "/chromosomeLength?species=mouse&chromo=18&json=1")
except ConnectionRefusedError:
    print("Cannot connect to the Server")
    exit()
response = connection.getresponse()
print(f"Response received!: {response.status} {response.reason}\n")
if response.status == HTTPStatus.OK:
    data_str = response.read().decode()
    data = json.loads(data_str)
    print(data)
    chromosome = data['number_chromosome']
    length = data['length']
    print(chromosome, length)


try:
    connection.request("GET", "/geneSeq?gene=FRAT1&json=1")
except ConnectionRefusedError:
    print("Cannot connect to the Server")
    exit()
response = connection.getresponse()
print(f"Response received!: {response.status} {response.reason}\n")
if response.status == HTTPStatus.OK:
    data_str = response.read().decode("utf-8")
    data = json.loads(data_str)
    #  print(data)
    gene = data['gene']
    bases = data['seq']
    print(gene, bases)

try:
    connection.request("GET", "/geneSeq?gene=TEST&json=1")
except ConnectionRefusedError:
    print("Cannot connect to the Server")
    exit()
response = connection.getresponse()
print(f"Response received!: {response.status} {response.reason}\n")
if response.status != HTTPStatus.OK:
    data_str = response.read().decode()
    print(data_str)
