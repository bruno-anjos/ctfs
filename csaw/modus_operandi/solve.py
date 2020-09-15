#!/usr/bin/python3

from pwn import *

p = remote('crypto.chal.csaw.io', 5001)

modes_seq = []

def solve():
	global p
	global modes_seq
	
	counter = 1
	plaintext = ("a" * 32)
	
	# receive initial message
	p.recvlineS(keepends=False)
	while True:
		# receive plaintext prompt
		p.recvlineS(keepends=False)
		# send plaintext
		p.sendline(plaintext)
		# receive header from line with ciphertext
		p.recvuntilS("Ciphertext is:")
		# receive ciphertext
		cipher = p.recvlineS().strip()
		# receive ECB or CBC prompt
		p.recvlineS(keepends=False)
		# check if it is ECB
		is_ecb = check_equal_with_bs(cipher)
		# send cipher mode
		if is_ecb:
			p.sendline('ECB')
			modes_seq += ["ECB"]
		else:
			p.sendline('CBC')
			modes_seq += ["CBC"]
		print(f"cipher {counter}")
		counter += 1


def check_equal_with_bs(cipher):
	bs = 32
	b0 = cipher[:bs]
	b1 = cipher[bs:bs*2]

	if b0 == b1:
		return True


mode_seqs = ['ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'ECB', 'ECB', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'ECB', 'ECB', 'ECB', 'ECB', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'CBC', 'CBC', 'CBC', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'ECB', 'ECB', 'ECB', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'CBC', 'CBC', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'CBC', 'ECB', 'CBC', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'ECB', 'CBC', 'ECB', 'ECB', 'ECB', 'CBC', 'CBC', 'CBC', 'CBC', 'CBC', 'ECB', 'CBC']
binary = ""

for mode in mode_seqs:
	if mode == "ECB":
		binary += "0"
	else:
		binary += "1"

print(binary)