# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# py_logic_gate_014_left_complementation.py
# creates a LEFT COMPLEMENTATION gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 0
B = 0

if (A == 0):
    print('Both False or B False')

    windll.user32.MessageBoxW(0,
    'Both False or B False', 'LC Gate', 0)

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
