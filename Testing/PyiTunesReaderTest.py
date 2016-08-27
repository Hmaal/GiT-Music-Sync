
# Import system level modules
import sys
import os

# Grab path to pyItunes module and import files
x = sys.path.append(os.path.abspath("/Users/hmaal/Desktop/2016 Projects/Cloned Projects/pyitunes/"))
from pyItunes import *


print( 'Yahoo' )

l = Library("../Files/IMLTest.xml")
pl = l.getPlaylistNames()

songCount = 0
playlistCount = 0

# Prints Every Song that has a Rating and an Artist
'''
for id, song in l.songs.items():
	if(song.rating and song.artist):
		print(song.name + ' ' + str(song.rating) + ' ' + song.artist)
		print(song.location + '\n \n')
'''


# Iterates through all Playlists in the Library and Prints all the Songs in each Playlist
for plItem in pl:
	playlistCount = playlistCount + 1
	print('Playlist #' + str(playlistCount) + ' Name: ' + l.getPlaylist(plItem).name)

	for song in l.getPlaylist(plItem).tracks:
		if(song.rating and song.artist):
			songCount = songCount + 1
			print(str(songCount) + ": " + "[Rating:%d] %s - %s" % (song.rating, song.artist, song.name))

	print("\n")
	songCount = 0