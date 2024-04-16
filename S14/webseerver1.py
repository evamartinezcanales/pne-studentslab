import http.server  #para poder programas sencillamente un servidor http
import socketserver

PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# -- Use the http.server Handler
handler = http.server.SimpleHTTPRequestHandler

# -- Open the socket server
with socketserver.TCPServer(("127.0.0.1", PORT), handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server Stopped!")
        httpd.server_close()
