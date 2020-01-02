from __future__ import print_function
from pwn import *
from sympy import *
import re
from decimal import Decimal


ip = "ctf.balqs.nctu.me"
port = 9001
r = remote(ip,port)

counter = 0

while (1):
	sym1 = r.recvuntil('\n')
	print(sym1, end='')
	
	if 'flag' in sym1:
		print(str(counter)+' bivariate linear equation found')
		break
	else:
		counter += 1
	sym2 = r.recvuntil('\n')
	print(sym2, end='')

	sym1 = re.findall(r'[-\d]+', sym1)
	sym2 = re.findall(r'[-\d]+', sym2)
	
	x = Symbol('x')
	y = Symbol('y')

	cof_x_1 = int(sym1[0])
	cof_y_1 = int(sym1[1])
	const_1 = int(sym1[2])

	cof_x_2 = int(sym2[0])
	cof_y_2 = int(sym2[1])
	const_2 = int(sym2[2])

	ans = (solve([cof_x_1 * x + cof_y_1 * y - const_1, cof_x_2 * x + cof_y_2 * y -const_2], [x,y]))

	try:
		int(ans[x])
	except:
		ans[x] = 1
		ans[y] = (const_1 - cof_x_1 * 1.0)/cof_y_1
		if str(ans[y]).endswith('.0'):
			ans[y] = int(ans[y])

	print(r.recvuntil('= '), end='')	# x =
	r.sendline(str(ans[x],))
	print(ans[x])

	print(r.recvuntil('= '), end='')	# y =
	r.sendline(str(ans[y]))
	print(ans[y])
