# 网络版日记本
首先，看大妈的演示，抓到这么几个点
1. 在client端运行脚本main.py
2. 首行出现`md2client 15.10.28.2126`，应该是client和server建立连接时候返回的
3. 之后开始打印以往的日记`八荣八耻`
4. 出现求输入的提示符`当下>>>`
5. 输入日记后，没有信息返回
6. 服务端把客户端输入的日记保存在`md4logging.log`里面，用tail -f可以实时追踪其变化


#### 初步思路
- 建立server和client的连接
- server读取历史日记，把日记内容传送到client上
- server接收client的输入
- server把收到的日记存入历史档案
- 当server收到client发送的`r`或者`hi`的时候打印所有的日记
- 当server收到client发送的`?`的时候，打印帮助

#### socket 初探
网上有不少用socket做cli界面的实时聊天的例子，其中一个非常简单的范例如下：

- Server

```python
import socket 
def Main():
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
 ```

 - Client

 ```python
 import socket
def Main():
	 host = '127.0.0.1'
	 port = 5001
	 server = ("127.0.0.1", 5000)
	 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	 s.bind((host, port))

	 message = raw_input('->  ')
	 while message != 'q':
	 	s.sendto(message, server)
	 	data, addr = s.recvfrom(1024)
	 	print "Recived from server: " + str(data)
	 	message = raw_input('->  ')
	 s.close()
if __name__ == "__main__":
	Main()
```

上面的例子里得到的信息点：
- socket默认的连接是tcp，因此当建立一个UDP连接的时候就要用`socket.socket(socket.AF_INET, socket.SOCK_DGRAM)`
- 如果socket.socket相当于说我要弄一个插座，那么s.bind相当于给插座通上电，但是，这时候还没有插上插头
- s.sendto()和s.recvfrom()，就相当于插头和插座连接上交换数据的过程


在这个例子的基础上，加入一下内容，改写为网络版日记本：
- clinet发送第一个信息给server之后，server返回以往所有的日记，client打印出来
- client之后输入的内容，server并不返回数据，就默默存到历史日记文档里面
- 当client发出需要历史日记的要求的时候，server把历史日记发给client

基于以上，将代码改写为
- Server

```python
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
		s.sendto('*'*15 +"I'm diary history" +'*'*15+'\n' +history, addr)
	elif str(data) == "?":
		strHelp= """
		?: help 
		r or hi: show all diary
		quit: quit
		"""
		s.sendto(strHelp, addr)
	else:
		file = open("DiaryPool.txt","a")
		file.write(str(data)+"\n\n")
		file.close()		
s.close()
```

- Client

```python
import socket
def Main():
	 host = '127.0.0.1'
	 port = 5001

	 server = ("127.0.0.1", 5000)

	 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	 s.bind((host, port))


	 s.sendto("hi", server)
	 data, addr = s.recvfrom(1024)
	 print data

	 message = raw_input('->  ')
	 # s.setblocking(0)
	 s.settimeout(0.01)

	 while message != 'quit':
	 	if message != '':
	 		s.sendto(message, server)
	 		try:
	 			data, addr = s.recvfrom(1024)
	 			print data
	 		except:
	 			pass
	 	message = raw_input('->  ')
	 s.close()
if __name__ == "__main__":
	Main()
```

改写的过程中遇到的问题及解决过程：
- 之前的范例，对于client来说，每一个`sendto()`都对应一个`recvfrom()`。但在日记本程序里面，输入日记的时候是server是不返回信息的。这时候如果只单纯写s.recvfrom(1024)，那么程序就会无限等，没有办法再输入下一个数据。解决尝试：
  - s. setblocking(0)，这个命令括号里面的默认是1，1的意思是，blocking mode，即如果我没等到（recvfrom）或者没把信息发出去（sendto），那么这个线路就会堵着。而0代表non-blocking mode，就是，如果我没收到或没法出去，那就返回一个错误信息
  - 所以第一个尝试用了，`s.setblocking(0)`加上`try ... except ...`，但是，发现出现了一个问题：当我输入`hi`或者`r`，回车以后没有信息返回，而要等到我再输入下一行信息的时候，才会返回历史日记的内容。检查了一下官方文档，发现了`s.settimeout()`
  > ** socket.settimeout(value)**

    > Set a timeout on blocking socket operations. The value argument can be a nonnegative float expressing seconds, or None. If a float is given, subsequent socket operations will raise a timeout exception if the timeout period value has elapsed before the operation has completed. Setting a timeout of None disables timeouts on socket operations. s.settimeout(0.0) is equivalent to s.setblocking(0); s.settimeout(None) is equivalent to s.setblocking(1).
  - 看了这个信息以后，猜测可能是因为在non-blocking mode，等待时间是0，也即如果没有当下收到回复或者发出的话，那么就报错，而收到信息也许需要写时间，所以每次都是等到输入下一行信息的时候才收到上一次server发送的消息
  - 把程序改为`s.settimeout(1)`，问题解决，但是1秒迟滞的时间太久，所以改为0.01,依然照常运行，问题搞定。



  ------
  - 大妈演示的时候，感觉server端并没有运行程序，而是直接看历史日记的文档是否有变化，本来以为是一个坑，想着是用python做的后台运行之类的。
  后来想明白了，就是开两个终端，一个运行server.py，另一个终端tail -f就可以。

  ---
  ### 运用Threading的解决方案
 - 之前对网络版日记本的想法是，每当Client发送一个信息(`sendto()`)给Server之后，再从Server那里尝试接收一条消息（`recvfrom()`）。
 - 但如果Server想给客户端发公告呢？那就只有等到Client给Server发送消息的时候，才可以收到，这样Server的主动权貌似就太小了。
 - 于是结合YouTube上看到的[视频](https://www.youtube.com/watch?v=PkfwX6RjRaI)，尝试了运用threading来接收消息
 > Threading可以让python在后台运行一些程序。所以，这一版本的思路是，我们让`recvfrom()`在后台一直运行，
 只要接收到了消息就`print`出来，这样以来就解决了上面的矛盾

 - So, 上代码，Client改作如下：

 ```python
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

 ```

- Threading的部分和[视频](https://www.youtube.com/watch?v=PkfwX6RjRaI)一致
- 但用Threading有一个问题，就是万一代码遇到了问题，而`recvfrom()`会无限运行，这时候就只有用`pkill`来结束程序了。

  ---------
  #### 待解决的问题
1. 1周的作业docotp应用拖到现在
  - 怎么结合？
2. 每次结束Server的时候都是用`ctrl+C`,那么最后一行的`s.close()`有什么作用？
  - 更否更优雅地解决？
3. 当日记文档变得越来越长的时候，1024byte显然不够，那么是把这个值改大还是分次传送呢？