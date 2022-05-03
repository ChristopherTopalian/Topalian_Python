# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# py_message_box_buttons_ok_cancel.py
# creates a message box with a title, text message,OK button and Cancel button

import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

ourTitle = "Question"

ourText = "Ready?"

choice = ctypes.windll.user32.MessageBoxW(0,
ourText, ourTitle, 1)

if (choice == 1):
    print("Pressed OK")
    # code that we want to activate goes here

if (choice == 2):
    print("Pressed Cancel")
    # code that we want to activate goes here

input('Press Enter to Exit')
