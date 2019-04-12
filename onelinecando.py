
import http.server
from http.server import SimpleHTTPRequestHandler
from http.server import HTTPServer
 
PORT = 8000
 
class VisibleHTTPRequestHandler(SimpleHTTPRequestHandler):
    
    def log_request(self, cod='-', size='-'):
        print(self._heading("HTTP Request"))
        print(self.raw_requestline,)
        for header, value in self.headers.items():
            print(header + ":", value)
    
    def do_GET(self, method='GET'):
        self.wfile = FileWrapper(self.wfile)
        SimpleHTTPRequestHandler.do_GET(self)
        print("")
        print(self._heading("HTTP Response"))
        print(self.wfile)
    
    def _heading(self, s):
        line = '=' * len(s)
        return line + '\n' + s + '\n' + line
        
class FileWrapper:
    def __init__(self, wfile):
        self.wfile = wfile
        self.contents = []
            
    def __getattr__(self, key):
        return getattr(self.wfile, key)
        
    def write(self, s):
        self.contents.append(s)
        self.wfile.write(s)
            
    def __str__(self):
        return ''.join(str(self.contents))
            
if __name__ == '__main__':
    httpd = HTTPServer(('localhost', PORT), VisibleHTTPRequestHandler)
    httpd.serve_forever()

