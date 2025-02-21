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
    
    def handle_request(self, data):

        data = self.parse_headers(data)        
        status = self.process_headers(data)

        response_content = self.response_content(data, status_code=status)
        response_line = self.response_line(status_code=status)
        response_headers = self.response_headers()

        response = response_line + response_headers + response_content

        return response
    
    def response_content(self, data, status_code, content=None):
        if content:
            return content.encode()

        path = data["REQUEST"]["PATH"]
        
        if path in self.routes:
            content = self.routes[path]().encode()            
        else:
            content = "<h1>Não encontrado 404</h1>".encode()

        if self.debug:
            print(self.routes)
            print(path)

        return content
    
def just_show_me_this(file_path):
    with open(file_path, 'r') as file:
        return file.read()
