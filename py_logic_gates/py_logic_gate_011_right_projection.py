# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# py_logic_gate_011_right_projection.py
# creates a RIGHT PROJECTION gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 1
B = 1

if (B == 1):
    print('Both True or B True')

    windll.user32.MessageBoxW(0,
    'Both True or B True', 'RP Gate', 0)

input('Press Enter to Exit')

# RIGHT PROJECTION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  1
# 1  0  =  0
# 1  1  =  1

# RP 0101

# Activates Only if Both True
# or B True
