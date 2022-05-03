#Dedicated to God the Father
#All Rights Reserved Christopher Topalian Copyright 2000-2022
#py_message_box__ok_button.py
#creates a message box with a title, text message and an OK Button

import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

ourTitle = "Greeting Message"

ourText = "Howdy"

ctypes.windll.user32.MessageBoxW(0,
ourText, ourTitle, 0)
