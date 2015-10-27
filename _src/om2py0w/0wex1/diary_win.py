from Tkinter import *
import datetime


class Application(Frame):
	def say_hi(self):
		print "hi, there, everyone!"

	def print_to_cli(self):
		file = open("DiaryPool.txt","a")
		file.write (datetime.datetime.now().__format__('%c')+"\n")
		file.write(self.word.get("1.0",'end')+"\n\n")
		file.close()
		

	def createWidgets(self):
		self.QUIT = Button(self)
		self.QUIT["text"] = "QUIT"
		self.QUIT["fg"] = "red"
		self.QUIT["command"] = self.quit 

		self.QUIT.pack({"side": "left"})

		self.hi_there = Button(self)
		self.hi_there["text"] = "Hello"
		self.hi_there["command"] = self.say_hi
		self.hi_there.pack({"side": "left"})

		# self.Words = StringVar()                            
		self.word = Text(self, width=40, height=30)
		self.word.pack({"side": "bottom"})

		self.SAVE = Button(self)
		self.SAVE["text"] = "Save"
		self.SAVE["fg"] = "red"
		self.SAVE["command"] = self.print_to_cli
		self.SAVE.pack({"side": "bottom"})

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()