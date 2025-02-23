from server.tcp import TCPServer

class HTTPServer(TCPServer):

    def __init__(self, host, port):

        super().__init__(host, port)

        self.host = host
        self.port = port

    def response_line(self, status_code):
        reason = REASONS[status_code]
        line = f'HTTP/1.1 {status_code} {reason}\n\r'
        
        return line

    def build_response_headers(self, content, content_type = "text/html"):

        headers = {
            "Content-Type": f"{content_type}; charset=UTF-8",
            "Content-Length": str(len(content)),
            "Connection": "close",
            "Server": "Daddy/1.0"
        }

        response_headers = ''
        for h in headers:
            response_headers += '%s: %s\r\n' % (h, headers[h])
        response_headers += '\r\n'

        return response_headers

    def parse_headers(self, request):

        request = request.decode().split("\r\n")
        request_line = request[0].split()
        headers = request[1:]

        request = {
            "METHOD": request_line[0],
            "PATH": request_line[1],
            "HTTP_V": request_line[2],
        }

        for header in headers:
            if not header:
                continue

            key, value = header.split(': ')
            request[key] = value

        return request

    def log(self, request, status):
        print(request["METHOD"], '->', 'http://' + self.host + ':' + str(self.port) + request["PATH"], '-', status)

REASONS = {
    100: "Continue",
    101: "Switching Protocols",
    102: "Processing",  # WebDAV
    200: "OK",
    201: "Created",
    202: "Accepted",
    203: "Non-Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    207: "Multi-Status",  # WebDAV
    208: "Already Reported",  # WebDAV
    226: "IM Used",  # HTTP Delta encoding
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    305: "Use Proxy",
    306: "Switch Proxy",
    307: "Temporary Redirect",
    308: "Permanent Redirect",  # RFC 7538
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Payload Too Large",
    414: "URI Too Long",
    415: "Unsupported Media Type",
    416: "Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a teapot",  # RFC 2324
    421: "Misdirected Request",
    422: "Unprocessable Entity",  # WebDAV
    423: "Locked",  # WebDAV
    424: "Failed Dependency",  # WebDAV
    425: "Too Early",  # HTTP/2
    426: "Upgrade Required",
    428: "Precondition Required",  # RFC 6585
    429: "Too Many Requests",  # RFC 6585
    431: "Request Header Fields Too Large",  # RFC 6585
    451: "Unavailable For Legal Reasons",  # RFC 7725
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported",
    506: "Variant Also Negotiates",  # RFC 2295
    507: "Insufficient Storage",  # WebDAV
    508: "Loop Detected",  # WebDAV
    510: "Not Extended",  # RFC 2774
    511: "Network Authentication Required",  # RFC 6585
}
