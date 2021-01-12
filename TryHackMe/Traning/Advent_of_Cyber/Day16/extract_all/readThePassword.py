import os

for x in os.listdir("./"):
	if ".txt" in x :
		print("file name is:",x)
		os.system("cat " +x +"|grep password")

