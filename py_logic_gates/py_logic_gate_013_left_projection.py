# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# py_logic_gate_013_left_projection.py
# creates a LEFT PROJECTION gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 1
B = 0

if (A == 1):
    print('Both True or A True')

    windll.user32.MessageBoxW(0,
    'Both True or A True', 'LP Gate', 0)

input('Press Enter to Exit')

# LEFT PROJECTION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  0
# 1  0  =  1
# 1  1  =  1

# LP 0011

# Activates Only if Both True
# or A True
