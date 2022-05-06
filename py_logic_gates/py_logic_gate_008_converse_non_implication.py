# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# py_logic_gate_008_converse_non_implication.py
# creates a CONVERSE NON IMPLICATION gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 0
B = 1

if (A == 0 and B == 1):
    print('B True')

    windll.user32.MessageBoxW(0,
    'B True', 'CNi Gate', 0)

input('Press Enter to Exit')

# CONVERSE NON IMPLICATION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  1
# 1  0  =  0
# 1  1  =  0

# CNi 0100

# Activates Only if B True
