from tcp import TCPServer

import os
import json

class HTTPServer(TCPServer):

    status = {
        200: 'OK',
        404: 'Not Found',
        403: 'Forbidden',
    }

    headers = {
        "Server": "WebSecure",
        "Content-Type": "text/html", 
    }

    def handle_request(self, data):

        data = self.request_headers(data)

        print(json.dumps(data, sort_keys=True, indent=4))

        status = self.process_headers(data)

        print("\nStatus code:", status)

        response_content = self.response_content(data, status_code=status)
        response_line = self.response_line(status_code=status)
        response_headers = self.response_headers()

        response = response_line + response_headers + response_content

        return response
    
    def response_line(self, status_code):
        reason = HTTPServer.status[status_code]
        line = f'HTTP/1.1 {status_code} {reason}\n\r'

        return line.encode()
    
    def response_headers(self, extra_headers = None):
        
        response_headers = ''

        headers = HTTPServer.headers.copy()

        if extra_headers:
            headers.update(extra_headers)

        for h in headers:
            response_headers += '%s: %s\n\r' % (h, headers[h])

        response_headers += '\n\r'

        return response_headers.encode()
          
    def request_headers(self, data):

        request = data.decode().split("\r\n")

        request_line = request[0].split()
        headers = request[1:]

        data = {
            "REQUEST": {
                "METHOD": request_line[0],
                "PATH": request_line[1],
                "HTTP_V": request_line[2],
            }, 

            "headers": {

            }
        }

        for header in headers:
            if not header:
                continue

            key, value = header.split(': ')
            data["headers"][key] = value

        return data

    def response_content(self, data, status_code):

        path = '.' + data["REQUEST"]["PATH"]

        if status_code == 404:
            return '<h1>Not found 404<h1>'.encode()

        file = open(path, 'r')    
        
        return file.read().encode()

    def process_headers(self, data):
        
        path = '.' + data["REQUEST"]["PATH"]

        if not os.path.isfile(path):
            return 404 
        
        return 200


if __name__ == "__main__":

    http = HTTPServer('192.168.0.13', 3000)
    http.start()
