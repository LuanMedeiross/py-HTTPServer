from server.http import HTTPServer

server = HTTPServer("127.0.0.1", 3000)
server.start()
