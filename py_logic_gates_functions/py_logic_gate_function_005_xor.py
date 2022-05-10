# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# https://github.com/ChristopherTopalian
# py_logic_gate_function_005_xor.py
# creates an XOR gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateXor(a, b):
    if ((a == 1 and b == 0) or
        (a == 0 and b == 1)):
        return "A True or B True"
    else:
        return "Choose the correct combination of 0 and 1"

def displayIt(a, b):
    print(gateXor(a, b))

    windll.user32.MessageBoxW(0,
    gateXor(a, b), 'XOR Gate', 0)

displayIt(0, 1)

input('Press Enter to Exit')

# XOR GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  1
# 1  0  =  1
# 1  1  =  0

# XOR 0110

# Activates Only if A True or B True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated
