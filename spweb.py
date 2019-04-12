class HTTPRequestHandler2(BaseHTTPRequestHandler):
        __blank_line = ['\r\n', '\n']
 
        def home(self):
            self.send_response(200)
            body = '''<html>
<head>
<title>HTTPServer</title>
<!--<link rel="stylesheet" href="222.css" type="text/css"></link>-->
<!--script src="333.js" type="text/javascript"></script>-->
</head>
<body>
<p1>Login</p1>
<form id="uploadForm" enctype="multipart/form-data" method="post" name="upload">
<input type="file" name="imageFile" id="imageFile" onchange="fileSelected()" />
</form>
<img src="/Mario.png">
</body>
<script src="upload.js" type="text/javascript"></script>
</html>'''
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(body))
            self.end_headers()
            self.wfile.write(body)
 
        def png(self, pngpath):
            import os
            self.send_response(200)
            self.send_header('Content-Type', 'image/png')
            dt = ''
            ln = 0
            with open('./images/%s'%pngpath, 'rb') as f:
                block = f.read(1024)
                while block:
                    dt += block
                    #ln += len(dt)
                    block = f.read(1024)
                    ln = f.tell()
            #self.send_header('content-length', len(dt))
            #self.wfile.write(dt)
            self.send_header('Content-Length', ln)#os.path.getsize('Mario.png'))
            self.end_headers()
            self.wfile.write(dt)
            self.wfile.flush()
            self.close_connection = 1
 
        def uploadjs(self):
            self.send_response(200)
            self.send_header('content-type', 'application/x-javascript')
            js = ''
            fn = 0
            with open('upload.js', 'r') as f:
                for line in f:
                    js += line
            self.send_header('Content-Length', len(js))
            self.end_headers()
            self.wfile.write(js)
 
        def do_GET(self):
            import re
            pngreg = re.compile(r'^/\w+\.png$')
            pngpath = None
            try:
                ret = pngreg.match(self.path)
                pngpath = ret.group()
            except:
                pass
            if self.path == '/':
                self.home()
            elif self.path == '/upload.js':
                self.uploadjs()
            elif pngpath:
                self.png(pngpath)
            else:
                self.close_connection = 1
 
        def saveFile(self, fileName, data):
            if not fileName or not data:
                return
            with open(fileName, 'wb') as f:
                f.write(data)
                f.flush()
 
        def do_POST(self):
            line = self.rfile.readline()
            postheaders = self.Message(self.rfile, 0)
            disposition = postheaders.getheader('content-disposition').strip()
            dps= disposition.split(';')
            filename = None
            for d in dps:
                d = d.strip()
                if d.startswith('filename='):
                    filename = d[len('filename="'):-1].strip()
                    break
            boundary = '--' + self.headers.getparam('boundary')
            endline = boundary + '--'
            data = ''
            startF= endF= False
            line = self.rfile.readline()
            while line:
                #print line,
                if line.strip() == endline:
                    self.saveFile(filename, data)
                    break
                elif line.strip() == boundary:
                    if not startF:
                        startF = True
                    elif startF and not endF:
                        endF = True
                        self.saveFile(filename, data)
                        endF = False
                        startF = True
                else:
                    data += line
                line = self.rfile.readline()
            self.send_response(200)
            self.end_headers()
            self.close_connection = 1
host = '127.0.0.1'
port = 5002
server = ThreadingHTTPServer((host, port), HTTPRequestHandler2)
server.serve_forever()

