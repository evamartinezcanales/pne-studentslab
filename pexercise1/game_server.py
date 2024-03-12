import socket
from secretnumber import secret_number
import os
import termcolor
import random

g = secret_number(random.randint(1, 100), [])
IP = "127.0.0.1"
PORT = 8081

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #para reutilizar el puerto si se ha pillado
try:
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print(f"Seq server configured")

    while True:
        (client_socket, client_address) = server_socket.accept()

        client_guess = client_socket.recv(2048).decode("utf-8")
        print(client_guess)

        response = g.guess(int(client_guess))

        client_socket.send(response.encode())
        print(response)

        client_socket.close()

except socket.error: #cualquier error respecto al socket
    print(f"Problems using port {PORT}. Do you have permission?")
except KeyboardInterrupt:   #cuando salimos del bucle cerrando la terminal
    print("Server stopped by the admin")
    server_socket.close()