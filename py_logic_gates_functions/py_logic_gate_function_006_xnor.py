# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# https://github.com/ChristopherTopalian
# py_logic_gate_function_006_xnor.py
# creates an XNOR gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateXnor(a, b):
    if ((a == 0 and b == 0) or
        (a == 1 and b == 1)):
        return "Both False or Both True"
    else:
        return "Choose the correct combination of 0 and 1"

def displayIt(a, b):
    print(gateXnor(a, b))

    windll.user32.MessageBoxW(0,
    gateXnor(a, b), 'XNOR Gate', 0)

displayIt(0, 0)

input('Press Enter to Exit')

# XNOR GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  0
# 1  0  =  0
# 1  1  =  1

# XNOR 1001

# Activates Only if Both False
# or Both True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated
