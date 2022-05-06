# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# py_logic_gate_015_contradiction.py
# creates a CONTRADICTION gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 0
B = 0

if ((A == 0 or A == 1) or
    (B == 0 or B == 1)):
    print("A or B is 0 or 1, Contradiction Gate Activated\nClosing App")

    windll.user32.MessageBoxW(0,
    'A or B is 0 or 1, Contradiction Gate Activated\nClosing App', 'Contradiction Gate', 0)

    quit()

#input("Press Enter to Exit")

# CONTRADICTION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  0
# 1  0  =  0
# 1  1  =  0

# C 0000

# If A is 0 or 1 or B is 0 or 1
# meaning, any combination of 0 and 1
# activates the quit() function
# to represent the contradiction gate logically

# we could choose to not use the quit() function
# and instead just inform the person that
# the contradiction gate has been activated
