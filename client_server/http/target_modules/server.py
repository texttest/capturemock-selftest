#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging, socket, time, os

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        if self.path.endswith("terminate"):
            self.wfile.write(b"Terminating!")
            # Not supposed to know about this variable, implementation detail of SocketServer
            # But seems like the only way to shutdown the server from within a request
            # Otherwise we have to start using ForkingMixin, ThreadingMixin etc which seems like overkill just to access a variable
            self.server._BaseServer__shutdown_request = True
        else:
            self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length).decode('utf-8') # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data)

        if self.path.endswith("strings"):
            self._set_response()
            self.wfile.write(str(len(post_data)).encode("utf-8"))
        else:
            self.send_error(400, explain="Path must end with strings")

def run(server_class=HTTPServer, handler_class=S, port=0):
    logging.basicConfig(level=logging.INFO)
    server_address = ('localhost', port)
    with server_class(server_address, handler_class) as httpd:
        host, port = httpd.socket.getsockname()
        address = host + ":" + str(port)
        message = "Started string-length server at http://" + address
        print(message, flush=True)
        httpd.serve_forever()
        logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
