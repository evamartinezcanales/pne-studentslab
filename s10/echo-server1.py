import socket
import termcolor

IP = "localhost"
PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #para reutilizar el puerto si se ha pillado
try:
    server_socket.bind((IP, PORT))
    server_socket.listen()

    while True:
        print(f"Waiting for connections at ({IP}:{PORT})...")
        (client_socket, client_address) = server_socket.accept()

        request_bytes = client_socket.recv(2048)
        request = request_bytes.decode("utf-8")
        print("Message from client: ", end="")
        termcolor.cprint(request, 'green')

        response = f"ECHO: {request}\n" #este es el mensaje que el cliente ha mandado
        response_bytes = str.encode(response)
        client_socket.send(response_bytes)

        client_socket.close()

except socket.error: #cualquier error respecto al socket
    print(f"Problems using port {PORT}. Do you have permission?")
except KeyboardInterrupt:   #cuando salimos del bucle cerrando la terminal
    print("Server stopped by the admin")
    server_socket.close()
