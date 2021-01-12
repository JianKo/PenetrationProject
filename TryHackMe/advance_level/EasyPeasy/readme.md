# Easy Peasy
```
export ip = 10.10.184.49



Part 2.
#1 Using Gobuster find 1 flag
- http://{export ip}/hidden/ 
  -> gobuster use with /usr/share/dirb/wordlists/common.txt
- echo "{base64 Message}" | base64 -d

#2 Futher enumerate the machine, wht is flag2?
- {export_ip}:65524/robots.txt 
- get user-agent value
- md5 get hasing : a18672860d0510e5ab6699730763b250
- tools : hash-identifier
- digest site:  https://md5hashing.net/hash/md5/a18672860d0510e5ab6699730763b250

#3 crack the hash with easypesay.txt what is the flag 3?
- check the main page read

#4 what is the hidden directory?
- /n0th1ng3ls3m4tt3r
- pentester shape : base62 decode

#5 Using the wordlist thata provided to you in this task crack the hash what is the passwd?
- john --wordlist=easypeasy.txt --format=gost ./hash.txt
- john --show ./hash.txt


#6 What is the password to login to the machine via SSH?
- wget http://10.10.184.49:65524/n0th1ng3ls3m4tt3r/binarycodepixabay.jpg
- steghide extract -sf {Image_file}
- binary to ascii : https://www.rapidtables.com/convert/number/binary-to-ascii.html


#7 What is the user flag?
- ROT13 decode

#8 What is the root flag?
- .mysecretcronjob.sh  << input reverse shell code
- listen nc port 
- will be root


```