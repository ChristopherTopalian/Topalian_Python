# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# py_logic_gate_010_material_non_implication.py
# creates a MATERIAL NON IMPLICATION gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 1
B = 0

if (A == 1 and B == 0):
    print('A True')

    windll.user32.MessageBoxW(0,
    'A True', 'MNi Gate', 0)

input('Press Enter to Exit')

# MATERIAL NON IMPLICATION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  0
# 1  0  =  1
# 1  1  =  0

# MNi 0010

# Activates Only if A True
