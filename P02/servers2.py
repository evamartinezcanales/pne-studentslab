import socket

# Configure the Server's IP and PORT
server_PORT = 8081
server_IP = "127.0.0.1" #it depends on the machine the server is running
MAX_OPEN_REQUESTS = 5

number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #creamos el socket del servidor
try:
    serversocket.bind((server_IP, server_PORT))
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(server_IP, server_PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!e
        number_con += 1

        # Print the connection number
        print(f"CONNECTION: {number_con}. From the IP: {address}")

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8")
        print(f"Message from client: {msg}")

        # Send the message
        message = "response"
        send_bytes = str.encode(message)
        # We must write bytes, not a string
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(server_IP, server_PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()

