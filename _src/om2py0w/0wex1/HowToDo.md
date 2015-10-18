### 构想
1. 用raw_input()获取输入，并存入一个txt文件当中
2. 每次写入用户输入之前，先写入一行当前的日期和时间
3. 提供一些可供用户操作的命令，比如回看、删除、搜索等

基于前两个构想，写出代码如下：
```python
#-*-coding: utf-8-*-
import datetime
diary = raw_input('How is your day today? -->')
current_time = datetime.datetime.now()

file = open("DiaryPool.txt","a")
file.write (current_time.__format__('%c')+"\n\n")
file.write(diary+"\n")
file.close()
print (":)")
```