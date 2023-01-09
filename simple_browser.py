# sockets are like files that we can send and receive data
# when you receive a file/socket, you gotta open it.
# First you gotta create your socket in your computer so it can receive messages
# These are notes from the class "Build a simple web browser with Python taught by Charles Severance at Freecodecamp"
# Link to the class: https://www.youtube.com/watch?v=o0XbHvKxw7Y&t=1767s (00:36:08)
import socket

# This command creates a socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect this socket to a domain name and a Port
mysocket.connect(("data.pr4e.org", 80))
# This commands to Get the page1.htm file from this domain name using HTTP 1.0 protocol. The encode method is for encoding this request in UTF-8
cmd = "GET http:data.pr4e.org/page1.htm HTTP/1.0 \r\n\r\n".encode()
# Send the command to the server
mysocket.send(cmd)
# This loop receives the data
while True:
    # ___This command receives the data in packs of 512 characters, it's common practice of the Transmission Control Protocol. But since the internet is fast nowadays we hardly even notice it.
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    # __The decode is important because we encoded the phone call in UTF-8 and we decode it so Python can read it.
    print(data.decode(), end="")
# after the connection is made you should close your socket
mysocket.close()
