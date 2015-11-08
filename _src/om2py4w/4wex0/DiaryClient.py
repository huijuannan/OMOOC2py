import socket
import threading
import time

shutdown = False
tLock = threading.Lock()

def receving(name, sock):
	while not shutdown:
		try:
			tLock.acquire()
			while True:
				data, addr = sock.recvfrom(1024)
				print data
		except:
		                pass
		finally:
			tLock.release()



host = '127.0.0.1'
port = 5001

server = ("127.0.0.1", 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receving, args = ("RecvThread", s))
rT.start()

s.sendto("hi", server)
time.sleep(0.1)
message = raw_input('->  ')

while message != 'quit':
 	if message != '':
 		s.sendto(message, server)
 	tLock.acquire()
 	message = raw_input('->  ')
 	tLock.release()
 	time.sleep(0.1)

shutdown = True
rT.join() 
s.close()
