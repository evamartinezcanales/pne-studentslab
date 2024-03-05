import socket

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8083
IP = "127.0.0.1"

ls.bind((IP, PORT))

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

        print("A client has connected to the server!")
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
