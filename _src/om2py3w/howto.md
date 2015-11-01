# 网络版日记本
- 建立server和client的连接，并建立连接的client列表
- server读取历史日记，把日记内容传送到client上
- server接收client的输入
- server把收到的client的信息发送给所有连接的client
- server把收到的日记存入历史档案

------
大妈演示的时候，感觉server端并没有运行程序，而是直接看历史日记的文档是否有变化
- 是否server在后台运行的？
- 用thread吗？怎么用