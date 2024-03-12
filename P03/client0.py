class Client:
    def __init__(self, ip_server, server_port):
        self.ip = ip_server
        self.port = server_port

    def __str__(self):
         return (f"Connection to SERVER at {self.ip}, PORT: {self.port}")

    def talk(self, msg):
        import socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.ip, self.port))
        client_socket.send(str.encode(msg))
        print("Sending a message to the server...")
        response = client_socket.recv(5000).decode()
        client_socket.close()  #para cortar la comunicación
        return response


    def ping(self):
        print("ok")




