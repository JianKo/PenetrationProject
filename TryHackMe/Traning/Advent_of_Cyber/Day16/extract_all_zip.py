
import os
import zipfile

listOfFiles = os.listdir("./")
print(type(listOfFiles))

for l in listOfFiles:
	if ".zip" in l :
		print(l)

		with zipfile.ZipFile("./"+l, "r") as zip_ref:
			zip_ref.extractall("./extract_all")