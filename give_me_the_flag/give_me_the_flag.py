from z3 import *

flag = input('Please give me the flag: ')
key = [21, 23, 9, 22, 3, 16, 17, 7, 8, 10, 11, 4, 0, 2, 13, 6, 1, 14, 18, 19, 5, 20, 12, 15]
check_values = [247, 220, 217, 225, 154, 146, 217, 173, 173, 244, 245, 225, 199, 148, 106, 163, 159, 106, 106, 173, 244, 244, 173]

assert len(flag) == 24
assert flag[:4] == 'flag'

x = ['0']*24
s = Solver()

for k in key:
	x[k] = Real('x['+str(k)+']')

x[0] = 102
x[1] = 108
x[2] = 97
x[3] = 103

for k1, k2 in zip(key[:-1], key[1:]):
	s.add(x[k1]+x[k2] == check_values[0])
	assert ord(flag[k1]) + ord(flag[k2]) == check_values[0], 'invalid flag'
	check_values = check_values[1:]

print(s.check())
print(s.model())
print('YOU GOT IT! ｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡')
