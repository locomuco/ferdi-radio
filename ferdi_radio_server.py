import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("files", PORT), Handler)

print ("serving at port", PORT)
httpd.serve_forever()