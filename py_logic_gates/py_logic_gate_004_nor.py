# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# py_logic_gate_004_nor.py
# creates a NOR gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 0
B = 0

if (A == 0 and B == 0):
    print('Both False')

    windll.user32.MessageBoxW(0,
    'Both False', 'NOR Gate', 0)

input('Press Enter to Exit')

# NOR GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  0
# 1  0  =  0
# 1  1  =  0

# NOR 1000

# Activates Only if Both False
