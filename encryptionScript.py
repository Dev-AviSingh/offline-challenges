flag = 'snakeseatsnakes'
import numpy as np

shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext


key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext


key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)


key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext


shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
    else:





