# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# py_logic_gate_001_and.py
# creates an AND gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 1
B = 1

if (A == 1 and B == 1):
    print('Both True')

    windll.user32.MessageBoxW(0,
    'Both True', 'AND Gate', 0)

input('Press Enter to Exit')

# AND GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  0
# 1  0  =  0
# 1  1  =  1

# AND 0001

# Activates Only if Both True
