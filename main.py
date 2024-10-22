from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/ball.html"

        try:
            # Open and read the requested file
            with open(self.path[1:], 'rb') as file:
                content = file.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, 'File Not Found: %s' % self.path)

if __name__ == '__main__':
    hostName = '10.120.90.104'
    serverPort = 8000

    webServer = HTTPServer((hostName, serverPort), MyHandler)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")