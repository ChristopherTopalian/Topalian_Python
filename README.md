Dedicated to God the Father
# Topalian_Python
All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
https://github.com/ChristopherTopalian

#### ``` os.getcwd() ```
```python
import os

theFolderPath = os.getcwd()

print(theFolderPath)
input('')
```

---

#### ``` time.sleep() ```
```python
import time

time.sleep(4.0)

print('4 seconds passed')
input('')
```

---

#### ``` time.sleep(), while loop ```
```python
import time

x = 0

while x != 1:
    time.sleep(4.0)
    print('4 seconds passed')

input('')
```

---

#### ``` while loop activated by input ```
```python
import time

x = input('Type 1 and press Enter\n')

while (x == '1'):
    time.sleep(4.0)
    print('4 seconds passed')

input('')
```

---

#### ```print and sleep```
```python
import time

print('Hi Friend')

time.sleep(3.0)

print('Is the sun shining?')

sunShining = input('y/n\n')

if (sunShining == 'y'):
    print('Nice that it is sunny out')
else:
    print('The sun will be there soon')

input('')
```
