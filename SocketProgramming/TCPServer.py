from socket import *

serverPort = 12111
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024)
    capitalizeMessage = message.upper()
    connectionSocket.send(capitalizeMessage)
    connectionSocket.close()
