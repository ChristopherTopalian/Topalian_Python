# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# https://github.com/ChristopherTopalian
# py_logic_gate_function_004_nor.py
# creates a NOR gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateNor(a, b):
    if (a == 0 and b == 0):
        return "Both False"
    else:
        return "Choose the correct combination of 0 and 1"

def displayIt(a, b):
    print(gateNor(a, b))

    windll.user32.MessageBoxW(0,
    gateNor(a, b), 'NOR Gate', 0)

displayIt(0, 0)

input('Press Enter to Exit')

# NOR GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  0
# 1  0  =  0
# 1  1  =  0

# NOR 1000

# Activates Only if Both False

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated
