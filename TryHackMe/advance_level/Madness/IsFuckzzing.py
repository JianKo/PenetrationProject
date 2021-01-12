import requests

url = "http://10.10.23.147/th1s_1s_h1dd3n/?secret="

for x in range(1,100):

	r = requests.get(url+str(x))

	print(r.text)

	if "wrong" in r.text:
		pass
	else:
		print(r.text)

	r.close()

# answer index 73
# result
#   Urgh, you got it right! But I won't tell you who I am! y2RPJ4QaPF!B