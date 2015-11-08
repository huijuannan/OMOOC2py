#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import socket

class UdpServer(object):
	def udpserver(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.bind(('', 9527))

		while True:
			recvData, (remoteHost, remotePort) = sock.recvfrom(1024)
			print"[%s:%s] connect" % (remoteHost, remotePort)

			sendData = sock.sendto("this is data from server", (remoteHost, remotePort))
			print "recvData: ", recvData
			print "sendDataLen: ", sendData

		sock.close()

if __name__ == "__main__":
	udpServer = UdpServer()
	udpServer.udpserver()
