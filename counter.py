import http.server
import socketserver

PORT = 8082

class CounterHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/count":
            with open("count.txt", "r+") as f:
                count = int(f.read().strip())
                count += 1
                f.seek(0)
                f.write(str(count))
                f.truncate()
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(f'{{"count": {count}}}', "utf-8"))
        else:
            self.send_error(404)

with socketserver.TCPServer(("", PORT), CounterHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
