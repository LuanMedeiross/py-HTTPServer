import socket

class TCPServer:

    def __init__(self, host, port):
        self.port = port
        self.host = host

    def start(self):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.host, self.port))
        sock.listen(5)
        
        print("Listening at", sock.getsockname())

        while True:
           
            conn, addr = sock.accept()

            print("Connected by", addr)

            data = conn.recv(2048)

            response = self.handle_request(data)

            conn.sendall(response)
            conn.close()

    def handle_request(self, data):
        # Do whatever with the data
        return data
    


if __name__ == "__main__":

    http = TCPServer('192.168.0.13', 3000)
    http.start()
