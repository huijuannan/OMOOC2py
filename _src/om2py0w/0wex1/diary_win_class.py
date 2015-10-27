from Tkinter import *
import datetime
# import Tkinter.scrolledtext as ScrolledText


class Application(Frame):


	def save_history(self):
		file = open("DiaryPool.txt","a")
		file.write (datetime.datetime.now().__format__('%c')+"\n")
		file.write(self.word.get("1.0",'end')+"\n\n")
		self.show_text.set(self.get_history())
		file.close()

	def get_history(self):
		file = open("DiaryPool.txt")
		ini_history = file.read()		
		file.close()
		return ini_history
		


	def createWidgets(self):
		

		# self.historyText = StringVar()


		self.history = Text(self, width=40, height=10)
		self.show_text = StringVar()
		self.show_text.set(self.get_history())
		self.history.insert(END, self.show_text)
		self.history.pack({"side": "top"})
		# self.history = Label(self, textvariable=self.historyText, width=40, height=10)
		# self.history.pack({"side": "top"})



		self.word = Text(self, width=40, height=10)
		self.word.pack({"side": "bottom"})

		self.SAVE = Button(self)
		self.SAVE["text"] = "Save"
		self.SAVE["fg"] = "red"
		self.SAVE["command"] = self.save_history()
		self.SAVE.pack({"side": "bottom"})

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()