# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# py_logic_gate_002_nand.py
# creates a NAND gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 0
B = 0

if (A == 0 or B == 0):
    print('A True or B True or Both False')

    windll.user32.MessageBoxW(0,
    'A True or B True or Both False', 'NAND Gate', 0)

input('Press Enter to Exit')

# NAND GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  1
# 1  0  =  1
# 1  1  =  0

# NAND 1110

# Activates Only if A True or B True,
# or Both False
