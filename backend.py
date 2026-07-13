from http.server import BaseHTTPRequestHandler, HTTPServer 
from urllib.parse import urlparse, parse_qs
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == "/health":
            data = {"status": "ok"}
            self.send_response(200)
        elif path == "/hello":
            name = query.get("name", ["world"])[0]
            data = {"message": f"Hello, {name}!"}
            self.send_response(200)
        else:
            data = {"error": "Not found"}
            self.send_response(404)

        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

server = HTTPServer(("127.0.0.1", 8000), Handler)
print("Server running on http://127.0.0.1:8000")
server.serve_forever()