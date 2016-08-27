from Tkinter import *

class App:

	def __init__(self, master):

		frame = Frame(master)
		frame.pack()

		self.button = Button(
			frame, text="Quit", fg="red", command=frame.quit
		)
		self.button.pack(side=LEFT)

		self.yoBtn = Button(frame, text="Hello", command=self.say_hi)
		self.yoBtn.pack(side=LEFT)

		self.newItemBtn = Button(frame, text="Insert", command=self.addItem)
		self.newItemBtn.pack(side=LEFT)

		self.btn_returnItems = Button(frame, text="Print Selected", command=self.printSelected)
		self.btn_returnItems.pack(side=LEFT)

	def say_hi(self):
		print "Hi There, Everyone!"
		listbox.delete(ACTIVE)

	def methTest(self, itemContext):
		items = map(int, listbox.curselection())
		print("Working?")
		print(itemContext)
		print(self)

	def addItem(self):
		print "Adding a new Item!"
		listbox.insert(END, "New Item")

	def printSelected(self):
		items = map(int, listbox.curselection())
		print("Printing Items!")
		print(items)


root = Tk()

app = App( root )

listbox = Listbox(root, selectmode=EXTENDED)
listbox.bind("<Double-Button-1>", app.methTest)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

root.mainloop()


# w = Label( root, text='Hellow Word from Python(Tkinter)' )
# w.pack()

# Creates window instance, only one widget per program and must be created before any other window
'''
root = Tk()

app = App( root )

root.mainloop()
'''