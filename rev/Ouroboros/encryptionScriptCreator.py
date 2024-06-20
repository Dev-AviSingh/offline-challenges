from ciphers import cipherTemplates
from random import shuffle

codeSnippets = []

codeSnippets.append(
	"flag = 'snakeseatsnakes'")

codeSnippets.append(
	"import numpy as np")

for i in range(1000):
	for c in cipherTemplates:
		codeSnippets.append(c)
	shuffle(cipherTemplates)

codeSnippets.append(
	"print(flag)")

with open("encryptionScript.py", "w") as f:
	for codeSnippet in codeSnippets:
		f.write(codeSnippet)
		f.write("\n")