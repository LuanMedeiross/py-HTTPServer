from server.http import HTTPServer

class Daddy(HTTPServer):

    def __init__(self):
        self.routes = {}
        self.debug = False

    def run_bitch_run(self, 
            host = "127.0.0.1", 
            port = 3000, 
            debug = False
        ):

        self.debug = debug

        print("Daddy's comming!")
        print(host + ':' + str(port))

        super().__init__(host, port)
        self.start()

    def right_here(self, path):
        def wrapper(func, methods = ["GET"]):
            self.routes[path] = {"func": func, "methods": methods}

            if self.debug:
                print(self.routes)

        return wrapper
    
    def handle_request(self, request):

        req = self.parse_headers(request)        
        status = self.process_request(req)

        response_content = self.response_content(req, status)
        response_line = self.response_line(status_code=status)
        response_headers = self.response_headers()

        response = response_line + response_headers + response_content

        self.log(req, status)

        return response
    
    def response_content(self, request = {}, status = 200):
        
        if status in STATUS_PAGES:
            return STATUS_PAGES[status].encode()
        
        path = request["PATH"]

        content = self.routes[path]["func"]()

        # if self.debug:
        #     print(self.routes)
        #     print(path)

        return content.encode()
    
    def process_request(self, request):

        path = request["PATH"]
        method = request["METHOD"]

        if not path in self.routes:
            return 404
        
        if not method in self.routes[path]["methods"]:
            return 405

        return 200
    
def gimme_that_damn_page(file_path):
    with open(file_path, 'r') as file:
        return file.read()

STATUS_PAGES = {
    400: "Bad request",
    401: "Unauthorized",
    403: gimme_that_damn_page('./server/response_templates/forbidden.html'),
    404: gimme_that_damn_page('./server/response_templates/notfound.html'),
    405: "Method not allowed",
    500: gimme_that_damn_page('./server/response_templates/internalservererror.html'),
}
