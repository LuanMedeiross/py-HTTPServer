from tcp import TCPServer

class HTTPServer(TCPServer):

    status = {
        200: 'OK',
        404: 'Not Found',
        403: 'Forbidden',
    }

    headers = {
        "Server": "Servidor da mariana linda",
        "Content-Type": "text/html", 
    }

    def handle_request(self, data):

        request = self.request_headers(data)
        print(request)

        response_line = self.response_line(status_code=200)
        response_headers = self.response_headers()

        response = response_line + response_headers

        return response
    
    def response_line(self, status_code):
        reason = HTTPServer.status[status_code]
        line = f'HTTP/1.1 {status_code} {reason}\n\r'

        return line.encode()
    
    def response_headers(self, extra_headers = None):
        
        response_headers = ''

        headers = self.headers.copy()

        if extra_headers:
            headers.update(extra_headers)

        for h in headers:
            response_headers += '%s: %s\n\r' % (h, headers[h])

        return response_headers.encode()
          
    def request_headers(self, data):

        request = data.decode().split("\r\n")

        print(request)

        request_line = request[0].split()

        data = {
            "REQUEST": {
                "METHOD": request_line[0],
                "PATH": request_line[1],
                "HTTP_V": request_line[2],
            }, 

            "headers": {

            }
        }

        for req in request[1::]:
            
            if len(req) > 1:
                req = req.split(': ')
                data["headers"][req[0]] = req[1]

        return data

if __name__ == "__main__":

    http = HTTPServer('192.168.0.13', 3000)
    http.start()
