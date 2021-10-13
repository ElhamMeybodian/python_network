from socket import *

serverName = '127.0.0.1'
serverPort = 12111
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input('Input lowercase sentence : ')
message = str.encode(message)  # convert string to byte
clientSocket.send(message)
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())
clientSocket.close()
