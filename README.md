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

---

#### ``` getuser() ```
```python
import getpass

print(getpass.getuser())
input('')
```

---

#### ``` for in loop ```
```python
ourNumbers = [
    4, 875, 23, 543, 12
]

for z in ourNumbers:
    print(z)

input('')
```

---

#### ``` for in range with len ```
```python
ourNumbers = [
    4, 875, 23, 543, 12
]

for z in range(len(ourNumbers)):
    print(ourNumbers[z])

input('')
```

---

#### ``` write custom HTML file ```
```python
ourHTMLContent = """
<html>
<head>
<title> Our HTML page </title>

<style>

body
{
    padding: 10px;
    background-color: rgb(30, 30, 30);
    font-family: Arial;
    font-size: 20px;
    color: rgb(255, 255, 255);
}

</style>

</head>

<body>

<div> Hi Everyone </div>

</body>

</html>

"""

with open('ourNewWebpage.html', 'w') as theFile:
    theFile.write(ourHTMLContent)
```

---

#### ``` write custom HTML file with Python Date ```
```python
ourHTMLContent = """
<html>
<head>
<title> Our HTML page </title>

<style>

body
{
    padding: 10px;
    background-color: rgb(30, 30, 30);
    font-family: Arial;
    font-size: 20px;
    color: rgb(255, 255, 255);
}

</style>

</head>

<body>

<div> Hi Everyone </div>

</body>

</html>

"""

with open('ourNewWebpage.html', 'w') as theFile:
    theFile.write(ourHTMLContent)
```
