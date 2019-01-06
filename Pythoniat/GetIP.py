import socket

hostname = socket.gethostname()
print(hostname)
ip = socket.gethostbyname(socket.getfqdn())
# or using : socket.gethostbyname(socket.gethostname())
print(ip)
