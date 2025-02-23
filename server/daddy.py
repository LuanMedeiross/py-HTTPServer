from server.http import HTTPServer
from server.config import DaddyConfig

class Daddy(HTTPServer, DaddyConfig):

    def __init__(self, _name_):
        self.routes = {}
        self.debug = False
        self._name_ = _name_

    def run_bitch_run(
            self, 
            host = "127.0.0.1", 
            port = 3000, 
            debug = False
        ):

        self.debug = debug

        HTTPServer.__init__(self, host, port)
        DaddyConfig.__init__(self, self._name_)

        self.start()

    def right_here(self, path):
        def wrapper(func, methods = ["GET"]):
            self.routes[path] = {"func": func, "methods": methods}
            if self.debug:
                print(self.routes)
            return func
        return wrapper
    
    def handle_request(self, request):

        req = self.parse_headers(request)        
        status = self.process_request(req)

        content = self.response_content(req, status)
        response_line = self.response_line(status_code=status)
        headers = self.build_response_headers(content)

        response = response_line + headers + content

        self.log(req, status)

        return response.encode("utf-8")
    
    def response_content(self, request = {}, status = 200):
        
        if status in self.STATUS_PAGES:
            return self.STATUS_PAGES[status]
        
        path = request["PATH"]
        content = self.routes[path]["func"]()

        return content
    
    def process_request(self, request):

        path = request["PATH"]
        method = request["METHOD"]

        if not path in self.routes:
            return 404
        
        if not method in self.routes[path]["methods"]:
            return 405

        return 200
    
    def gimme_that_damn_page(self, file_path):

        file_path = self.template_path / file_path

        with open(file_path, 'r') as file:
            return file.read()

