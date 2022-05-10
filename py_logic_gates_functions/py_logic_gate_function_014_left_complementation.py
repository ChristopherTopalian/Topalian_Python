# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# https://github.com/ChristopherTopalian
# py_logic_gate_function_014_left_complementation.py
# creates a LEFT COMPLEMENTATION gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateLc(a, b):
    if ((a == 0 and b == 0) or
        (a == 0 and b == 1)):
        return "Both False or B True"
    else:
        return "Choose the correct combination of 0 and 1"

def displayIt(a, b):
    print(gateLc(a, b))

    windll.user32.MessageBoxW(0,
    gateLc(a, b), 'LC Gate', 0)

displayIt(0, 1)

input('Press Enter to Exit')

# LEFT COMPLEMENTATION GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  1
# 1  0  =  0
# 1  1  =  0

# LC 1100

# Activates Only if Both False
# or B True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated
