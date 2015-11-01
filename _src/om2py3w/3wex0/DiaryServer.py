#-*-coding: utf-8-*-
import datetime
import socket

host = '192.168.1.105'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

print "Server Startted"

clients = []
while True:
	data, addr = s.recvfrom(1024)

	if str(data) == "hi":
	                clients = clients.append(addr) # need if argument

	file = open("DiaryPool.txt")
	history = file.read()
	file.close()


	for client in clients:
		s.sendto(history, client)

	data, addr = s.recvfrom(1024)
	file = open("DiaryPool.txt","a")
	file.write (current_time.__format__('%c')+"\n")
	file.write(text+"\n\n")
	file.close()

	for client in clients:
		s.sendto(data, client)

s.close()



text = ""
print ('How is your day today? -->')

sentinel = 'quit()' # ends when this string is seen
for line in iter(lambda: raw_input(), sentinel):
	text += "%s\n" % line


current_time = datetime.datetime.now()


print ("-->Diary is finished. Well done: )")
