# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# py_tkinter_url_go_to.py
# creates an interface window using tkinter that has one label and two buttons.
# when left clicked, each button opens one specified URL in our default web browser.

import ctypes
import webbrowser
from tkinter import *

collegeWebsite = "https://CollegeOfScripting.weebly.com"

collegeYouTube = "https://www.youtube.com/ScriptingCollege"

ctypes.windll.shcore.SetProcessDpiAwareness(1)

ourWindow = Tk()

# window width, height, xPos, yPos
ourWindow.geometry('400x220+200+150')

ourWindow.title('COSMAS')

def urlGoTo(whichURL) :
    webbrowser.open(whichURL)

labelCollegeName = Label(ourWindow,
text = 'College of Scripting\nMusic & Science',
width = 200,
font = ("Tahoma", 14, 'bold'), fg = 'white',
bg = 'black').pack(pady = 5, padx =5)

buttonCollegeWebsite = Button(ourWindow, text = "Website", command = lambda: urlGoTo(collegeWebsite),
font = ("Tahoma", 12, 'bold'),
activebackground = "white",
fg = 'white', bg = 'black').pack(pady=5, padx=5)

buttonCollegeYouTube = Button(ourWindow, text = "YouTube Channel", command = lambda: urlGoTo(collegeYouTube),
font = ("Tahoma", 12, 'bold'),
activebackground = "white",
fg = 'white', bg = 'black').pack(pady=5, padx=5)

ourWindow.mainloop()
