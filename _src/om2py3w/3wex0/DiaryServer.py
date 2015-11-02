#-*-coding: utf-8-*-
import socket

# host = '192.168.1.105'
# port = 5000
host = '127.0.0.1'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

print "Server Startted"

while True:
	data, addr = s.recvfrom(1024)

	if str(data) == "hi" or str(data) == "r":
		file = open("DiaryPool.txt")
		history = file.read()
		file.close()
		# print len(history)
		s.sendto('*'*15 +"I'm diary history" +'*'*15+'\n' +history, addr)
	elif str(data) == "?":
		strHelp= """
		 ? :          help 
		r or hi: show all diary
		quit :    quit
		"""
		s.sendto(strHelp, addr)
	else:
		file = open("DiaryPool.txt","a")
		file.write(str(data)+"\n\n")
		file.close()
		# history = 'Recored.'
		# for client in clients:
		# 	s.sendto(data, client)
	# s.sendto(history, addr)
s.close()