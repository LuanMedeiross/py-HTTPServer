from tcp import TCPServer
from http import HTTP

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

        response_line = self.response_line(status_code=200)
        response_headers = self.response_headers()

        response = response_line + response_headers

        return response
    
    def response_line(self, status_code):
        reason = HTTP.status[status_code]
        line = f'HTTP/1.1 {status_code} {reason}\n\r'

        return line.encode()
    
    def response_headers(self, extra_headers = None):
        
        response_headers = ''

        headers = self.headers.copy()

        if extra_headers:
            headers.update(extra_headers)

        for header in headers.items():
            print(header)

            response_headers += header[0] + ': ' + header[1] + '\n\r'

        return response_headers.encode()
          

if __name__ == "__main__":

    http = HTTPServer('192.168.0.13', 3000)
    http.start()
