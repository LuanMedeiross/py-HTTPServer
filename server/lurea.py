from server.http import HTTPServer

class Lurea(HTTPServer):

    def __init__(self, host, port, debug=False):
        super().__init__(host, port, debug)

        self.routes = {}
        

    def run(self):

        print("Iniciando servidor Lurea")
        print(f"\t{self.host}:{self.port}")

        self.start()

    def route(self, path = None):
        if not path:
            raise Exception("Null route")
        
        def wrapper(handle):
            self.routes[path] = handle

            if self.debug:
                print(self.routes)

        return wrapper
