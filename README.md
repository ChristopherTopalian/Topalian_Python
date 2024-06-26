# Topalian_Python

### ``` os.getcwd() ```
 ```python
import os

theFolderPath = os.getcwd()

print(theFolderPath)
input('')
```

---

### ``` time.sleep() ```
```python
import time

time.sleep(4.0)

print('4 seconds passed')
input('')
```

---

### ``` time.sleep(), while loop ```
```python
import time

x = 0

while x != 1:
    time.sleep(4.0)
    print('4 seconds passed')

input('')
```

---

### ``` while loop activated by input ```
```python
import time

x = input('Type 1 and press Enter\n')

while (x == '1'):
    time.sleep(4.0)
    print('4 seconds passed')

input('')
```
