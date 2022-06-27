# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# https://github.com/ChristopherTopalian
# py_name_of_user_002.py
# shows the Username using print and MessageBoxW

import ctypes
from getpass import getuser

ctypes.windll.shcore.SetProcessDpiAwareness(1)

theTitle = "Username"

theUsername = getuser()

theText = "Username is:"

theMessage = theText + "\n\n" + theUsername  

print(theMessage)

ctypes.windll.user32.MessageBoxW(0,
theMessage, theTitle, 0)

input("Press Enter to Exit")
