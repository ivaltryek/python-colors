import bs4
from http.server import BaseHTTPRequestHandler, HTTPServer
from bottle import template
with open('static/index.html') as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt, features="html.parser")

color = '#44B3C2' #Blue 44B3C2 and Yellow F1A94E

soup.find('div')['style'] = 'background:' + color
print(soup)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes(template(str(soup)), "utf-8"))



with HTTPServer(('', 9000), handler) as server:
    server.serve_forever()
