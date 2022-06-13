# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# py_folder_current_002.py
# getcwd gets the path of the current working directory (cwd)
# cwd means current working directory
# another word for directory is folder
# shows the path of the folder where this script is currently working from
# the folder path is shown in the console and a message box

import ctypes
import os

ctypes.windll.shcore.SetProcessDpiAwareness(1)

theTitle = "Path of Current Working Directory"

theFolderPath = os.getcwd()

print(theFolderPath)

ctypes.windll.user32.MessageBoxW(0,
theFolderPath, theTitle, 0)

input("Press Enter to Exit")
