import re
import os
import requests

path = "./Web-Shells"

for x in os.listdir(path):
	req = "http://10.10.10.181/" + x 
	r = requests.get(req)

	if re.findall("not found",r.text):
		pass
	else :
		print("Guessing is : ", x)


	# print (r.text)
