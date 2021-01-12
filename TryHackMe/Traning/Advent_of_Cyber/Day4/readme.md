# Day4 : Training 

```
Export IP = 10.10.158.130
ssh mcsysadmin@[your-machines-ip]

username: mcsysadmin
password: bestelf1234
```

***#1 How many visible files are there in the home directory(excluding ./ and ../)?***
```
:8
```

***#2 What is the content of file5?***
```
: recipes

[-] Guide
- cat file5
```

***#3 Which file contains the string ‘password’?***
```
:file6

- grep -nr 'password'
```
***#4 What is the IP address in a file in the home folder?***
```
: 10.0.0.05

- grep -rn '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'
file2:35:10.0.0.05eXWx4auBc8Swra4aPvIoBre+PRsVgu9GVbGwD33X8bd7TWwlZxzSVYa
```

***#5 How many users can log into the machine?***
```
: 3

- cat /etc/passwd | grep /bin/bash 
- 쉘을 가지고 있는 유저의 갯수

```

***#6 What is the sha1 hash of file8? ***
```
: fa67ee594358d83becdd2cb6c466b25320fd2835

- sha1sum file8

```


***#8 What is mcsysadmin’s password hash?***
```
: $6$jbosYsU/$qOYToX/hnKGjT0EscuUIiIqF8GHgokHdy/Rg/DaB.RgkrbeBXPdzpHdMLI6cQJLdFlS4gkBMzilDBYcQvu2ro

- find / -name *shadow* -exec ls -lt {} \; 2>/dev/null
```

