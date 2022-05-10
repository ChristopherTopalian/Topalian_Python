# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# https://github.com/ChristopherTopalian
# py_logic_gate_function_012_right_complementation.py
# creates a RIGHT COMPLEMENTATION gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateRc(a, b):
    if ((a == 0 and b == 0) or
        (a == 1 and b == 0)):
        return "Both False or A True"
    else:
        return "Choose the correct combination of 0 and 1"

def displayIt(a, b):
    print(gateRc(a, b))

    windll.user32.MessageBoxW(0,
    gateRc(a, b), 'RC Gate', 0)

displayIt(1, 0)

input('Press Enter to Exit')

# RIGHT COMPLEMENTATION GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  0
# 1  0  =  1
# 1  1  =  0

# RC 1010

# Activates Only if Both False
# or A True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated
