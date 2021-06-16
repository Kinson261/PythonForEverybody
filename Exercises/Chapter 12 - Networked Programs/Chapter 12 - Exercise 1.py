"""
Exercise 1: Change the socket program socket1.py to prompt the user
for the URL so it can read any web page. You can use split('/') to
break the URL into its component parts so you can extract the host
name for the socket connect call. Add error checking using try and
except to handle the condition where the user enters an improperly
formatted or non-existent URL.
"""

import socket


website = input('Enter website:\n')

if website.startswith('https://'):
    if website.startswith('http://'):
        pass
    pass
else:
    website = 'https://' + website

host = website.split(sep='/')
host = host[2]
port = 80

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, port))
    cmd = f'GET {website} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(1000)
        if len(data) < 1:
            break
        data.decode()
        print(data.decode(), end='')

except:
    print("Non-existent URL")

mysock.close()
