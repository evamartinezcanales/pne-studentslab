import socket

server_PORT = 8080
server_IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5

number_con = 0

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((server_IP, server_PORT))
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        print("Waiting for connections at {}, {} ".format(server_IP, server_PORT))
        (clientsocket, address) = serversocket.accept()

        number_con += 1


        print(f"CONNECTION: {number_con}. From the IP: {address}")


        msg = clientsocket.recv(2048).decode("utf-8")
        print(f"Message from client: {msg}")
        message = "response"
        send_bytes = str.encode(message)

        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(server_IP, server_PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()

