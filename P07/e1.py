import http.client
import json
from http import HTTPStatus

SERVER = 'rest.ensembl.org'
RESOURCE = '/info/ping'
PARAMS = '?content-type=application/json'
URL = SERVER + RESOURCE + PARAMS

print()
print(f"SERVER: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER) # utiliza el puerto por defecto del http

try:
    conn.request("GET", RESOURCE + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

response = conn.getresponse()
print(f"Response received!: {response.status} {response.reason}\n")
if response.status == HTTPStatus.OK:
    data_str = response.read().decode("utf-8")
    data = json.loads(data_str) # hay que hacer un print de lo que vale data
    ping = data['ping']
    if ping == 1:
        print("PING OK! The database is running!")
    else:
        print("...")