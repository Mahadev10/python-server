from http.server import SimpleHTTPRequestHandler, HTTPServer

HOST = "localhost"
PORT = 8000

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print(f"Server running at http://{HOST}:{PORT}")
server.serve_forever()