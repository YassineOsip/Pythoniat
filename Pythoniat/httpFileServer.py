import http.server
import socketserver

port = 8080

hanler = http.server.SimpleHTTPRequestHandler
http =  socketserver.TCPServer(("",port),hanler)
print("server run at port : " , port)
http.serve_forever()