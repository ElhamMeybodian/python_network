from socket import *

serverName = '127.0.0.1'
serverPort = 12010
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence : ')
message = str.encode(message)  # convert string to byte
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())  # convert byte to string
clientSocket.close()
