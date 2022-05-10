# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# https://github.com/ChristopherTopalian
# py_logic_gate_function_010_material_non_implication.py
# creates a MATERIAL NON IMPLICATION gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateMni(a, b):
    if (a == 1 and b == 0):
        return "A True"
    else:
        return "Choose the correct combination of 0 and 1"

def displayIt(a, b):
    print(gateMni(a, b))

    windll.user32.MessageBoxW(0,
    gateMni(a, b), 'MNi Gate', 0)

displayIt(1, 0)

input('Press Enter to Exit')

# MATERIAL NON IMPLICATION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  0
# 1  0  =  1
# 1  1  =  0

# MNi 0010

# Activates Only if A True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated
