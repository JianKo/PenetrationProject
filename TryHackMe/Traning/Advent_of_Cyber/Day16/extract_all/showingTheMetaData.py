import os
import exiftool
from pprint import pprint

files = ["./"]

with exiftool.ExifTool() as et:
	metadata = et.get_metadata_batch(files)

for d in metadata:
	try:
		print(d['XMP:Version'])
		
	except:
		pass
# for d in metadata:
# 		print(d)
# 		print("\n")