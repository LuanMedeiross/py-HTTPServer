from tcp import TCPServer
    
class HTTPServer(TCPServer):

    def handle_request(self, data):
        return data

if __name__ == "__main__":

    http = HTTPServer('192.168.0.13', 3000)
    http.start()
