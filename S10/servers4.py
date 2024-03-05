import socket
connections = 0
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8084
IP = "127.0.0.1"

ls.bind((IP, PORT))
connections += 1
ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    # -- Execute this part if there are no errors
    else:
        connections += 1
        print("A client has connected to the server!")
        print(f"CONECTION {connections} IP, PORT: {client_ip_port}")
        msg_raw = cs.recv(2048)

        msg = msg_raw.decode()

        print(f"Message received: {msg}")

        count = 0
        correct = True
        while correct:
            count += 1
            response = "ECHO. Test" + str(count)

            cs.send(response.encode())

            if count >= 3:
                correct = False
        cs.close()
