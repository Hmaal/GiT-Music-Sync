

# Constants
ITEM_TAG = 'dict';
KEY_TAG = 'key';

STRING_TYPE_TAG = 'string';

LOCATION_KEY_VALUE = 'Location';
NAME_KEY_VALUE = 'Name';


#########################################	Methods	##################################

# Method meant to be used to find starting tags for xml file lines.
def containsTag(line, tagName):
	fullTag = '<' + tagName + '>';
	alteredText = line.strip();
	return alteredText.startswith(fullTag);

def stripTag(line, tagName):
	openTag = '<' + tagName + '>';
	closeTag = '</' + tagName + '>';
	alteredText = line.strip();
	alteredText = alteredText.replace(openTag, '');
	return alteredText.replace(closeTag, '');

def getLocationURL(line):
	if( containsTag(line, KEY_TAG)):
		keyRemovedText = stripTag( line, KEY_TAG);
		
		if( keyRemovedText.startswith(LOCATION_KEY_VALUE)):
			return keyRemovedText.replace(LOCATION_KEY_VALUE, '', 1) + '\n'; 
		
	return '';

def getTrackName(line):
	if( containsTag(line, KEY_TAG)):
		keyRemovedText = stripTag( line, KEY_TAG);

		if( keyRemovedText.startswith(NAME_KEY_VALUE )):
			return keyRemovedText.replace(NAME_KEY_VALUE, '', 1) + '\n';
	return '';



#########################################	Logic	##################################

f = open('../Files/Test iTunes Music Library copy.xml', 'r');
nf = open('../Files/GiT MS Test.xml', 'w');
fileOutput = '';

for line in f:
	tempLine = f.readline();

	#if( containsTag(tempLine, ITEM_TAG)):
	#	print(tempLine);
		
	#getLocationURL( tempLine );
	
	#if( containsTag( tempLine, ITEM_TAG ) ):
	
	#if( containsTag( tempLine, KEY_TAG) ):
		#currLine = stripTag( tempLine, KEY_TAG);

		#if( currLinecontainsTag( templine, ))
		#while( not containsTag( f.readline(), '/' + ITEM_TAG ) ):
			#tempLine = f.readline();
			#nf.write( '\n' );
			nf.write( getLocationURL( tempLine ) );
			nf.write( getTrackName( tempLine ) );
			#nf.write( '\n' );


f.close();

