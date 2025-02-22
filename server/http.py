from server.tcp import TCPServer

import json

class HTTPServer(TCPServer):

    def __init__(self, host, port):

        super().__init__(host, port)

        self.headers = {
            "Server": "Lurea",
            "Content-Type": "text/html", 
        }

        self.status_handlers = {
            range(100, 200): "Informational",
            range(200, 300): "Success",
            range(300, 400): "Redirection",
            range(400, 500): "Client Error",
            range(500, 600): "Server Error",
        }

    def response_line(self, status_code):
        reason = self.get_status(status_code)
        line = f'HTTP/1.1 {status_code} {reason}\n\r'.encode()
        
        return line

    def response_headers(self, extra_headers = None):

        response_headers = ''

        headers = self.headers.copy()

        if extra_headers:
            headers.update(extra_headers)

        for h in headers:
            response_headers += '%s: %s\n\r' % (h, headers[h])
        response_headers += '\n\r'

        return response_headers.encode()

    def parse_headers(self, request):

        request = request.decode().split("\r\n")
        request_line = request[0].split()
        headers = request[1:]

        request = {
            "METHOD": request_line[0],
            "PATH": request_line[1],
            "HTTP_V": request_line[2],
        }

        for header in headers:
            if not header:
                continue

            key, value = header.split(': ')
            request[key] = value

        # if self.debug:
        #     print(json.dumps(request, indent=4))

        return request
    
    def get_status(self, code):
        for status_range, category in self.status_handlers.items():
            if code in status_range:
                return category
        return "Unknown status code"
    
    def log(self, request, status):
        print(request["METHOD"], '->', 'http://' + self.host + ':' + str(self.port) + request["PATH"], '-', status)

