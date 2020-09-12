#!/usr/bin/python3

import re
from pycipher import Bifid

with open('ramblings_size.txt', 'w') as fpwrite:
	with open('ramblings.txt', 'r') as fp:
		line = fp.readline()
		while line:
			regex = re.compile('[^a-zA-Z]')
			line = "".join(line.strip().split())
			line = regex.sub('', line)
			line = line.replace('j', '')
			line = line.replace('J', '')
			fpwrite.write("%d | %s\n" % (len(line), line))
			line = fp.readline()

ciphertext = ""
with open('message.txt', 'r') as fp:
	ciphertext = fp.readline().strip()

with open('ramblings_size.txt', 'r') as fp:
	with open('results.txt', 'w') as res:
		line = fp.readline()
		while line:
			line = line.strip()
			print("using line ", line)
			splits = line.split("|")
			line = splits[1]
			line = line.strip()
			if len(line) != 25:
				line = fp.readline()
				continue
			attempt1 = Bifid(line, 5).decipher(ciphertext)
			res.write(attempt1 + "\n")
			attempt1 = Bifid(line[::-1], 5).decipher(ciphertext)
			res.write(attempt1 + "\n")
			print("tried line ", line)
			line = fp.readline()
