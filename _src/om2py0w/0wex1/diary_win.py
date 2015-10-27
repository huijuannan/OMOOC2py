# -*- coding: utf-8 -*-
from Tkinter import *
import ScrolledText
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

frame_top_left = Frame(width=350, height=200, bg='white')
frame_top_right = Frame(width=10, height=200)
frame_middle = Frame(width=350, height=180, bg='white')
frame_bottom = Frame(width=350, height=40)

HistoryBox = Text(frame_top_left)
S = Scrollbar(frame_top_right)
# S.pack(side=RIGHT, fill=Y)
# HistoryBox.pack(side=LEFT, fill=Y)
S.config(command=HistoryBox.yview)
HistoryBox.config(yscrollcommand=S.set)


file = open("DiaryPool.txt")
show_text = file.read()
file.close()

HistoryBox.insert(END, show_text)

InputBox = Text(frame_middle)

SAVE = Button(frame_bottom)
SAVE["text"] = "Save"
SAVE["fg"] = "red"
SAVE["command"] = save_diary

# HistoryBox.tag_config('green', foreground='#008B00')

frame_top_left.grid(row=0, column=0, padx=4, pady=5)
frame_top_right.grid(row=0, column=1, padx=4, pady=5)
frame_middle.grid(row=1, column=0, padx=4, pady=5)
frame_bottom.grid(row=2, column=0)
frame_top_left.grid_propagate(0)
frame_top_right.grid_propagate(0)
frame_middle.grid_propagate(0)
frame_bottom.grid_propagate(0)

HistoryBox.grid()
InputBox.grid()
SAVE.grid()
S.grid()

root.mainloop()