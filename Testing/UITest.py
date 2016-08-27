import Tkinter as tk

class Application(tk.Frame):
	def __init__(self, master = None):
		tk.Frame.__init__(self, master)
		self.grid(sticky = tk.N + tk.E + tk.S + tk.W)
		self.createWidgets()

	def createWidgets(self):
		top = self.winfo_toplevel()
		top.rowconfigure(0, weight = 1)
		top.rowconfigure(1, weight = 1)
		top.rowconfigure(2, weight = 1)

		top.columnconfigure(0, weight = 1)
		top.columnconfigure(1, weight = 1)
		top.columnconfigure(2, weight = 1)

		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)
		self.columnconfigure(2, weight=1)

		self.rowconfigure(0, weight=1)
		self.rowconfigure(1, weight=1)
		self.rowconfigure(2, weight=1)

		self.quitButton = tk.Button(self, text = 'Quit', command = self.quit) #, colors = 'black'
		self.quitButton.grid(row = 2, column = 2, sticky = tk.N + tk.E + tk.S + tk.W)

app = Application()
app.master.title('Sample Application')
app.mainloop()