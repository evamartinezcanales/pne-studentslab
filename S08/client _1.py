import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
server_PORT = 8081
server_IP = "127.0.0.1"# it depends on the machine the server is running, el IP del que te vas a conectar


# First, create the socket
# We will always use these parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((server_IP, server_PORT))

# Send data. No strings can be sent, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!,"))

# Close the socket
s.close()

