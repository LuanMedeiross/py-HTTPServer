from server.http import HTTPServer

class Lurea(HTTPServer):

    def __init__(self, host, port, debug=False):
        super().__init__(host, port)

        self.routes = {}
        self.debug = debug

    def run(self):
        self.start()

    def route(self, path = None):
        if not path:
            raise Exception("Null route")
        
        def wrapper(handle):
            self.routes[path] = handle
            print(self.routes)

        return wrapper

