# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# https://github.com/ChristopherTopalian
# py_logic_gate_function_015_contradiction.py
# creates a CONTRADICTION gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateContradiction(a, b):
    if ((a == 0 and b == 0) or
        (a == 0 and b == 1) or
        (a == 1 and b == 0) or
        (a == 1 and b == 1)):
        return "One or Both False or True. Negative Message is placed here, or we can leave it blank"
    else:
        return "Choose the correct combination of 0 and 1"

def displayIt(a, b):
    print(gateContradiction(a, b))

    windll.user32.MessageBoxW(0,
    gateContradiction(a, b), 'CONTRADICTION Gate', 0)

displayIt(1, 1)

input('Press Enter to Exit')

# CONTRADICTION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  0
# 1  0  =  0
# 1  1  =  0

# C 0000

# Activates Only if One or Both False or True
# meaning, any combination of 0 and 1
# negative message is placed in the body of the if, or left blank

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated
