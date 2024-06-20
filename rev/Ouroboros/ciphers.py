ceaser = \
'''
shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext
'''

atbash = \
'''
ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext
'''

vignere = \
"""
key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext
"""

playfair = \
"""
key = "KEYWORD"
key_matrix = []
used = []


for char in key.upper():
    if char not in used and char != 'J':
        key_matrix.append(char)
        used.append(char)

for i in range(65, 91):
    char = chr(i)
    if char not in used and char != 'J':
        key_matrix.append(char)
        used.append(char)

key_matrix = [key_matrix[i * 5:(i + 1) * 5] for i in range(5)]

def find_position(char):
    for row in range(5):
        for col in range(5):
            if key_matrix[row][col] == char:
                return row, col


flag = flag.replace('J', 'I')
if len(flag) % 2 != 0:
    flag += 'X'

ciphertext = ""
i = 0
while i < len(flag):
    a = flag[i]
    b = flag[i + 1]
    row1, col1 = find_position(a)
    row2, col2 = find_position(b)
    if row1 == row2:    
        ciphertext += key_matrix[row1][(col1 + 1) % 5]
        ciphertext += key_matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        ciphertext += key_matrix[(row1 + 1) % 5][col1]
        ciphertext += key_matrix[(row2 + 1) % 5][col2]
    else:
        ciphertext += key_matrix[row1][col2]
        ciphertext += key_matrix[row2][col1]
    i += 2

flag = ciphertext
"""

hill = \
"""
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  
flag = flag.upper().replace(' ', '')
if len(flag) % 3 != 0:
    flag += 'X' * (3 - len(flag) % 3)

def text_to_numbers(text):
    return [ord(char) - 65 for char in text]

def numbers_to_text(numbers):
    return ''.join(chr(num + 65) for num in numbers)

plaintext_numbers = text_to_numbers(flag)
ciphertext_numbers = []

for i in range(0, len(plaintext_numbers), 3):
    block = np.array(plaintext_numbers[i:i + 3])
    encrypted_block = np.dot(key_matrix, block) % 26
    ciphertext_numbers.extend(encrypted_block)

ciphertext = numbers_to_text(ciphertext_numbers)
flag = ciphertext
"""

substitution = \
"""
key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext
"""

transposition = \
"""
key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)
"""

railfence = \
"""
key = 3  
ciphertext = [''] * key
rail = 0
direction = 1

for char in flag:
    ciphertext[rail] += char
    rail += direction
    if rail == 0 or rail == key - 1:
        direction = -direction

flag = ''.join(ciphertext)
"""


columnarTransposition = \
"""
key = "3214"  
num_cols = len(key)
num_rows = len(flag) // num_cols + (len(flag) % num_cols != 0)
grid = [[''] * num_cols for _ in range(num_rows)]

for i, char in enumerate(flag):
    row = i // num_cols
    col = i % num_cols
    grid[row][int(key[col]) - 1] = char

ciphertext = ''.join(sum(grid, []))
flag = ciphertext
"""

autokey = \
"""
key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext
"""


cipherTemplates = [
    ceaser,
    atbash,
    vignere,
    playfair,
    hill,
    substitution,
    transposition,
    railfence,
    columnarTransposition,
    autokey
]