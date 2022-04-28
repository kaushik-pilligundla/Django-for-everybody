import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET https://www.cs.sjsu.edu/faculty/pollett/267.1.22s/Lec20220427.html#(7) HTTP/1.0\r\n\r\n'.encode(
)
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
