from http.server import HTTPServer,BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html; charset=utf-8')
    self.send_header('Teste','abc')
    self.end_headers()
    data = f"""
    <html>
      <head>
        <title>Hello, world!</title>
      </head>
      <body>
        <p>Testando nosso servidor HTTP!</p>
        <p>Diretório: {self.path}</p>
      </body>
    </html>    
    """.encode()
    self.wfile.write(data)

server  = HTTPServer(('localhost',8000), SimpleHandler)
server.serve_forever()