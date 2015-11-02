import socket
 
def Main():
 	# host = '192.168.1.105'
 	# port = 5000
 	host = '127.0.0.1'
 	port = 5000

 	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 	s.bind((host, port))

 	print "Server Startted"
 	while True:
 		data, addr = s.recvfrom(1024)
 		print "message from: " + str(addr)
 		print "from connect user: " + str(data)
 		data = str(data).upper()
 		print "Sending: " + str(data)
 		s.sendto(data, addr)

 	s.close()

if __name__ == "__main__":
 	Main()