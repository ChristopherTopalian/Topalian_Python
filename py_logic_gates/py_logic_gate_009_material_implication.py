# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# py_logic_gate_009_material_implication.py
# creates a MATERIAL IMPLICATION gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 0
B = 0

if (A == 0 or B == 1):
    print('Both True or Both False or B True')

    windll.user32.MessageBoxW(0,
    'Both True or Both False or B True', 'Mi Gate', 0)

input('Press Enter to Exit')

# MATERIAL IMPLICATION GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  1
# 1  0  =  0
# 1  1  =  1

# Mi 1101

# Activates Only if Both True
# or Both False or B True
