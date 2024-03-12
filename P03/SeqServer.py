import socket
from Seq1 import Seq
import os
import termcolor

IP = "127.0.0.1"
PORT = 8081
sequences = ["ACGTACAGTA", "ACGTACTA", "CGCTGATCGA", "CGTGACA", "GGTAGATA"]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #para reutilizar el puerto si se ha pillado
try:
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print(f"Seq server configured")

    while True:
        print(f"Waiting for connections at ({IP}:{PORT})...")
        (client_socket, client_address) = server_socket.accept()

        request_bytes = client_socket.recv(2048)
        request = request_bytes.decode("utf-8")

        lines = request.splitlines()
        slices = lines[0].split(" ")
        command = slices[0]
        command.upper()
        termcolor.cprint(command, "green")
        if command == "PING":
            response = "OK! \n"
        elif command == "GET":
            n = int(slices[1])
            bases = sequences[n]
            s = Seq(bases)
            response = str(s)
        elif command == "INFO":
            bases = slices[1]
            s = Seq(bases)
            response = s.info()

        elif command == "COMP":
            bases = slices[1]
            s = Seq(bases)
            response = f"{s.complement()}"

        elif command == "REV":
            bases = slices[1]
            s = Seq(bases)
            response = s.reverse()

        elif command == "GENE":
            gene = slices[1]
            s = Seq()
            filename = os.path.join(gene + ".txt")
            s.read_fasta(filename)
            response = str(s)


        client_socket.send(response.encode())
        print(response)

        client_socket.close()

except socket.error: #cualquier error respecto al socket
    print(f"Problems using port {PORT}. Do you have permission?")
except KeyboardInterrupt:   #cuando salimos del bucle cerrando la terminal
    print("Server stopped by the admin")
    server_socket.close()
