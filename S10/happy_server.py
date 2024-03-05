import socket

# Configure the Server's IP and PORT
servers_PORT = 8083
servers_IP = "127.0.0.1" # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.connect((servers_IP, servers_PORT))
# -- Step 2: Bind the socket to server's IP and PORT
#ls.bind((servers_IP, servers_PORT)) #it returns a tuple

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    (rs, address) = ls.accept()
    print(f"Client{address}")
    msg = rs.recv(2028).decode()

    print("The client says..." + str(msg))

    rs.close()

# -- Close the socket
ls.close()
