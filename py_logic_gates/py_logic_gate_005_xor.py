# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# py_logic_gate_005_xor.py
# creates an XOR gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 1
B = 0

if ((A == 0 and B == 1) or
    (A == 1 and B == 0)):
    print('A True or B True')

    windll.user32.MessageBoxW(0,
    'A True or B True', 'XOR Gate', 0)

input('Press Enter to Exit')

# XOR GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  1
# 1  0  =  1
# 1  1  =  0

# XOR 0110

# Activates Only if A True or B True
