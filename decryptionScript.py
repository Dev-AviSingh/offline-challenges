import numpy as np
flag = 'LTPBKZMAHHWZRZK' 

key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)


key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text


shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text


key = 3  # Number of columns
num_cols = key

