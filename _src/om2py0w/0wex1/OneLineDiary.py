#-*-coding: utf-8-*-
import datetime
diary = raw_input('How is your day today? -->')
current_time = datetime.datetime.now()

file = open("DiaryPool.txt","a")
file.write (current_time.__format__('%c')+"\n")
file.write(diary+"\n")
file.close()
print (":)")
