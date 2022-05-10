# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# https://github.com/ChristopherTopalian
# py_logic_gate_function_001_and.py
# creates an AND gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateAnd(a, b):
    if (a == 1 and b == 1):
        return "Both True"
    else:
        return "Choose the correct combination of 0 and 1"

def displayIt(a, b):
    print(gateAnd(a, b))

    windll.user32.MessageBoxW(0,
    gateAnd(a, b), 'AND Gate', 0)

displayIt(1, 1)

input('Press Enter to Exit')

# AND GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  0
# 1  0  =  0
# 1  1  =  1

# AND 0001

# Activates Only if Both True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated
