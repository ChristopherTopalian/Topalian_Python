# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# https://github.com/ChristopherTopalian
# py_logic_gate_function_013_left_projection.py
# creates a LEFT PROJECTION gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateLp(a, b):
    if ((a == 1 and b == 0) or
        (a == 1 and b == 1)):
        return "A True or Both True"
    else:
        return "Choose the correct combination of 0 and 1"

def displayIt(a, b):
    print(gateLp(a, b))

    windll.user32.MessageBoxW(0,
    gateLp(a, b), 'LP Gate', 0)

displayIt(1, 1)

input('Press Enter to Exit')

# LEFT PROJECTION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  0
# 1  0  =  1
# 1  1  =  1

# LP 0011

# Activates Only if A True
# or Both True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated
