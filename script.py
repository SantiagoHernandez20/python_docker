from http.server import BaseHTTPRequestHandler, HTTPServer


class WebHttp(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Python Server</title>
        </head>
        <body>
            <h1>Servidor web python</h1>
            <p>Servidor con python y html sin utilizar frameworks</p>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode('utf-8'))

def ejecutar():
    server_address = ('', 9000)
    httpd =  HTTPServer(server_address, WebHttp)
    print('Servidor corriendo en en puerto 9000')
    httpd.serve_forever()

if __name__ == "__main__":
    ejecutar()