#-*-coding: utf-8-*-
import socket

# host = '192.168.1.105'
# port = 5000
host = '127.0.0.1'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

print "Server Startted"

clients = []

while True:
	data, addr = s.recvfrom(1024)

	if str(data) == "hi":
	                clients.append(addr) # need if argument
	                file = open("DiaryPool.txt")
	                history = file.read()
	                file.close()
	                for client in clients:
	                	s.sendto(history, client)
	else:
		file = open("DiaryPool.txt","a")
		file.write(str(data)+"\n\n")
		file.close()
		# for client in clients:
		# 	s.sendto(data, client)

s.close()