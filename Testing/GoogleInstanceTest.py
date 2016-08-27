from gmusicapi import Mobileclient, Musicmanager

###

# Music Manager access
#mm = Musicmanager()

# Call once per session, used to login using OAuth
#mm.perform_oauth()

# Used to login after OAUth has been established
#mm.login()

#library = mm.get_uploaded_songs()

###

# Mobile Client access
api = Mobileclient()

logged_in = api.login('user@gmail.com', 'my-password', Mobileclient.FROM_MAC_ADDRESS)
# logged_in is True if login was successful

library = api.get_all_songs()

# Iterate through list of dictionaries, printing information about each track
for album in library:
	for k, v in album.items():
		print('Key: ' + str(k) + ' Value: ' + str(v))
	print('\n')
