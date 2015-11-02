# 网络版日记本
首先，看大妈的演示，抓到这么几个点
1. 在client端运行脚本main.py
2. 首行出现`md2client 15.10.28.2126`，应该是client和server建立连接时候返回的
2. 之后开始打印以往的日记`八荣八耻`
3. 出现求输入的提示符`当下>>>`
4. 输入日记后，没有信息返回
5. 服务端把客户端输入的日记保存在`md4logging.log`里面，用tail -f可以实时追踪其变化
6. 客户端看起来并没有运行什么程序



#### 初步思路
- 建立server和client的连接，并建立连接的client列表
- server读取历史日记，把日记内容传送到client上
- server接收client的输入
- server把收到的client的信息发送给所有连接的client
- server把收到的日记存入历史档案

------
大妈演示的时候，感觉server端并没有运行程序，而是直接看历史日记的文档是否有变化
- 是否server在后台运行的？
- 用thread吗？怎么用