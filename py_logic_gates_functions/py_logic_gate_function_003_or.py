# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# https://github.com/ChristopherTopalian
# py_logic_gate_function_003_or.py
# creates an OR gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateOr(a, b):
    if ((a == 1 and b == 0) or
        (a == 0 and b == 1) or
        (a == 1 and b == 1)):
        return "One or Both True"
    else:
        return "Choose the correct combination of 0 and 1"

def displayIt(a, b):
    print(gateOr(a, b))

    windll.user32.MessageBoxW(0,
    gateOr(a, b), 'OR Gate', 0)

displayIt(1, 1)

input('Press Enter to Exit')

# OR GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  1
# 1  0  =  1
# 1  1  =  1

# OR 0111

# Activates Only if One or Both True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated
