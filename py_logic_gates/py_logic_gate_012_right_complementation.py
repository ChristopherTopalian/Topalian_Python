# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# py_logic_gate_012_right_complementation.py
# creates a RIGHT COMPLEMENTATION gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 1
B = 0

if (B == 0):
    print('Both False or A True')

    windll.user32.MessageBoxW(0,
    'Both False or A True', 'RC Gate', 0)

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
