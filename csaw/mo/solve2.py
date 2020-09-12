#!/usr/bin/python3

from pwn import *
import time

ec = 0
cc = 0
p = remote('crypto.chal.csaw.io', 5001)

modes_seq = ['ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'ECB', 'ECB', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'ECB', 'ECB', 'ECB', 'ECB', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'CBC', 'CBC', 'CBC', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'ECB', 'ECB', 'ECB', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'CBC', 'CBC', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'CBC', 'CBC', 'CBC', 'ECB', 'CBC']

def solve():
	global ec
	global cc
	global p
	global modes_seq
	
	
	print(p.recvlineS(keepends=False))
	index = 0
	while True:
		line = p.recvlineS(timeout=5, keepends=False)
		print(line)
		if 'Enter plaintext:' not in line:
			print("line: ", line)
			print(p.recvall(timeout=10))
			break
		print(modes_seq[index])
		p.sendline(modes_seq[index])
		print(p.recvuntilS("Ciphertext is:"))
		cipher = p.recvlineS().strip()
		print("\n".join([cipher[i:i+32] for i in range(0, 32*3, 32)]))
		print(p.recvlineS(keepends=False))
		p.sendline(modes_seq[index])
		index += 1


def check_equal_with_bs(cipher):
	bs = 32
	maxbs = 32
	while True:
		if bs > maxbs:
			return False
		b0 = cipher[0]
		b1 = cipher[bs]
		b2 = cipher[bs-1]
		b3 = cipher[bs*2-1]

		if b0 == b1 and b2 == b3:
			return True

		bs *= 2

start = time.time()
try:
	solve()
except EOFError:
	print(p.clean(5))
end = time.time()
print("time took: ", end - start)
print("reached %d, %d" %(ec, cc))
print("seq: ", modes_seq)