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
