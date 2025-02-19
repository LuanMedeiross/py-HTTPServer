from server.http import HTTPServer

class Lurea(HTTPServer):

    routes = {}

    def run(self):
        self.start()

    def route(self, path = None):
        if not path:
            raise Exception("Null route")
        
        def wrapper(handle):
            self.routes[path] = handle
            print(self.routes)

        return wrapper
