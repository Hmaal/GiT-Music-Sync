# Import system level modules
import sys
import os

# Grab path to pyItunes module and import files
x = sys.path.append(os.path.abspath("/Users/hmaal/Desktop/2016 Projects/Cloned Projects/pyitunes/"))
from pyItunes import *
from Tkinter import *

class App:

	def __init__(self, master):

		frame = Frame(master)
		frame.pack()

		# Quit Button
		self.btn_Quit = Button(frame, text="Quit", fg="red", command=frame.quit)
		self.btn_Quit.pack(side=LEFT)

		# Delete Button
		self.btn_Delete = Button(frame, text="Delete", command=self.deleteItem)
		self.btn_Delete.pack(side=LEFT)

		# Insert Button
		self.btn_Insert = Button(frame, text="Insert", command=self.addItem)
		self.btn_Insert.pack(side=LEFT)

		# Print List of Items
		self.btn_returnItems = Button(frame, text="Print Selected", command=self.printSelected)
		self.btn_returnItems.pack(side=LEFT)

	def deleteItem(self):
		print("Deleting Item")
		print(lb_Playlists.get(ACTIVE))
		lb_Playlists.delete(ACTIVE)

	def methTest(self, itemContext):
		items = map(int, lb_Playlists.curselection())
		print("Working?")
		print(items)
		print(itemContext)
		print(self)

	def addItem(self):
		print "Adding a new Item!"
		lb_Playlists.insert(END, "New Item")

	def printSelected(self):
		items = map(int, lb_Playlists.curselection())
		print("Printing Items!")
		print(items)
		print(lb_Playlists.get(ACTIVE))

	def populateSongs(self, contextItem):
		lb_Songs.delete(0, END)
		for item in map_Songs.get(lb_Playlists.get(ACTIVE)):
			lb_Songs.insert(END, item)


root = Tk()

app = App( root )

# Initialize Songs and Playlists
l = Library("../Files/IMLTest.xml")
pl = l.getPlaylistNames()

# Listbox for Playlists
lb_Playlists = Listbox(root, selectmode=BROWSE)
lb_Playlists.bind("<Double-Button-1>", app.populateSongs)
lb_Playlists.pack(side="left")

# Listbox for Songs based on Playlists
lb_Songs = Listbox(root, selectmode=MULTIPLE)
lb_Songs.pack(side="right")

# Helper Varaibles for Libarary
songCount = 0
playlistCount = 0
map_Songs = { }

# Iterate through Playlists
for plItem in pl:
	playlistCount = playlistCount + 1
	playlist_Name = l.getPlaylist(plItem).name
	playlist_Songs = []

	# Insert Playlist into proper Listbox
	print('Playlist #' + str(playlistCount) + ' Name: ' + playlist_Name)
	lb_Playlists.insert(END, l.getPlaylist(plItem).name)

	# Gather All Songs for a Specific Playlist into a List
	for song in l.getPlaylist(plItem).tracks:
		if(song.rating and song.artist):
			songCount = songCount + 1
			song_Detail = str(songCount) + ": " + "[Rating:%d] %s - %s" % (song.rating, song.artist, song.name)
			playlist_Songs.append(song_Detail)
	
	# Add all Songs in List to Map
	map_Songs[playlist_Name] = playlist_Songs

	print("\n")
	songCount = 0


root.mainloop()
