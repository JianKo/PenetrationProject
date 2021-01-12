import json
import requests


reqUrl = "http://10.10.169.100:3000/f"

value = {'value':'C','next':'s'}

while True:
	
	r = requests.get(reqUrl,headers=value)
	res_ =json.loads(r.text)
	

	print(res_['value'],end='')

	
	if res_['value'] in "end":
		print("")
		exit()

	reqUrl = "http://10.10.169.100:3000/"+res_['next']
	

