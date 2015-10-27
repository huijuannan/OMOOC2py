# -*- coding: utf-8 -*-
from Tkinter import *
# import ttk
import datetime

def save_diary():
	diary = InputBox.get("1.0",'end') +"\n\n"
	now = datetime.datetime.now().__format__('%c')+"\n"
	HistoryBox.insert(END, now)
	HistoryBox.insert(END, diary)
	InputBox.delete(1.0, END)
	file = open("DiaryPool.txt","a")
	file.write (now)
	file.write(diary)
	file.close()

root = Tk()
root.title("Dear Diary")


HistoryBox = Text(root, width=40, height=10)

file = open("DiaryPool.txt")
show_text = file.read()
file.close()

HistoryBox.insert(END, show_text)
HistoryBox.pack({"side": "top"})


InputBox = Text(root, width=40, height=10)
InputBox.pack({"side": "top"})

SAVE = Button(root)
SAVE["text"] = "Save"
SAVE["fg"] = "red"
SAVE["command"] = save_diary
SAVE.pack({"side": "bottom"})


	# file = open("DiaryPool.txt","a")
	# 	file.write (datetime.datetime.now().__format__('%c')+"\n")
	# 	file.write(self.word.get("1.0",'end')+"\n\n")
	# 	self.show_text.set(self.get_history())
	# 	file.close()
root.mainloop()