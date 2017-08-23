# Import system level modules
import sys
import os
import Tkinter as tk

# Import file for User Interface
import UI as UI

# Grab path to pyItunes module and import files
imp_PyTunes = sys.path.append(os.path.abspath("/Users/hmaal/Desktop/2016 Projects/Cloned Projects/pyitunes/"))
from pyItunes import *


# Start Main Loop of Program/App
mainApp = UI.Application( )
mainApp.master.title('Google Music P-iTunes Sync')
mainApp.mainloop()