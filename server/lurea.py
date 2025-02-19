from server.http import HTTPServer

class Lurea(HTTPServer):

    def run(self):
        self.start()

    def route(path = None):
        if not path:
            raise Exception("Null route")
        
        def decorator(handle):
            def wrapper():
                teste = handle()
                return teste
            return wrapper
        return decorator
