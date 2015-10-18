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

#### 如何令其可以一直运行,等待我们的输入
- 或是接受其它命令?
- 怎么退出脚本?

Google的[结果](http://stackoverflow.com/questions/11664443/raw-input-across-multiple-lines-in-python)，有两种解决途径
1. 比较容易理解的版本：
```python
text = ""
stopword = ""
while True:
    line = raw_input()
    if line.strip() == stopword:
        break
    text += "%s\n" % line
print text
```
2. *看起来*更简洁的版本
```python
sentinel = '' # ends when this string is seen
for line in iter(raw_input, sentinel):
    pass # do things here
```
查了iter的[文档](https://docs.python.org/2/library/functions.html?highlight=raw_input#iter)，
但是在这种情况下，iter第一个input必须是callable object。


- So, 加入了lambda，将这一部分变成callable，参考[这里](https://www.daniweb.com/programming/software-development/code/495069/way-to-enter-multiple-values-with-raw_input)。但是具体的原理还是不理解啦～还要进一步学习：）
于是，代码修改为:

```python
#-*-coding: utf-8-*-
import datetime
text = ""
print ('How is your day today? -->')

sentinel = 'quit()' # ends when this string is seen
for line in iter(lambda: raw_input(), sentinel):
	text += "%s\n" % line
	
current_time = datetime.datetime.now()

file = open("DiaryPool.txt","a")
file.write (current_time.__format__('%c')+"\n")
file.write(text+"\n\n")
file.close()
print ("-->Diary is finished. Well done: )")
```
