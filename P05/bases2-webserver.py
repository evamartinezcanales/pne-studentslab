import http.server
import socketserver
import termcolor
from pathlib import Path
import os


PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        resources = self.path
        if resources == "/" or resources == "/index.html":
            file_name = os.path.join("html", "index.html")
            body = Path(file_name).read_text()
            self.send_response(200)
        elif resources == "/info/A.html":
            file_name = os.path.join("html", "info", "A.html")
            body = Path(file_name).read_text()
            self.send_response(200)
        elif resources == "/info/C.html":
            file_name = os.path.join("html", "info", "C.html")
            body = Path(file_name).read_text()
            self.send_response(200)
        elif resources == "/info/T.html":
            file_name = os.path.join("html", "info", "T.html")
            body = Path(file_name).read_text()
            self.send_response(200)
        elif resources == "/info/G.html":
            file_name = os.path.join("html", "info", "G.html")
            body = Path(file_name).read_text()
            self.send_response(200)
        else:
            resource = self.path[1:]
            try:
                file_name = os.path.join("html", resource)
                body = Path(file_name).read_text()
                self.send_response(200)
            except FileNotFoundError:
                file_name = os.path.join("html", "error.html")
                body = Path(file_name).read_text()
                self.send_response(404)

        body_bytes = body.encode()
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(body_bytes)))
        self.end_headers()

        self.wfile.write(body_bytes)

        return

with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT...", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Stopped by the user")
        httpd.server_close()