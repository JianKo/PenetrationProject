# Remote BOX Scanning Reuslt

### Command :  nmap -sC -sV -oN RemoteScanning.txt 10.10.10.180

### Nmap 7.80 scan initiated Tue May 19 13:15:13 2020 as
Nmap scan report for 10.10.10.180 <br>
Host is up (0.26s latency).<br>
Not shown: 993 closed ports<br>
PORT     STATE SERVICE       VERSION <br>
21/tcp   open  ftp           Microsoft ftpd <br>
|_ftp-anon: Anonymous FTP login allowed (FTP code 230) <br>
| ftp-syst: <br>
|_  SYST: Windows_NT <br>
80/tcp   open  http          Microsoft HTTPAPI httpd 2.0    <br>(SSDP/UPnP)
|_http-title: Home - Acme Widgets <br>
111/tcp  open  rpcbind       2-4 (RPC #100000) <br>
| rpcinfo: <br>
|   program version    port/proto  service <br>
|   100000  2,3,4        111/tcp   rpcbind <br>
|   100000  2,3,4        111/tcp6  rpcbind <br>
|   100000  2,3,4        111/udp   rpcbind <br>
|   100000  2,3,4        111/udp6  rpcbind <br>
|   100003  2,3         2049/udp   nfs <br>
|   100003  2,3         2049/udp6  nfs <br>
|   100003  2,3,4       2049/tcp   nfs <br>
|   100003  2,3,4       2049/tcp6  nfs <br>
|   100005  1,2,3       2049/tcp   mountd <br>
|   100005  1,2,3       2049/tcp6  mountd <br>
|   100005  1,2,3       2049/udp   mountd <br>
|   100005  1,2,3       2049/udp6  mountd <br>
|   100021  1,2,3,4     2049/tcp   nlockmgr <br>
|   100021  1,2,3,4     2049/tcp6  nlockmgr <br>
|   100021  1,2,3,4     2049/udp   nlockmgr <br>
|   100021  1,2,3,4     2049/udp6  nlockmgr <br>
|   100024  1           2049/tcp   status <br>
|   100024  1           2049/tcp6  status <br>
|   100024  1           2049/udp   status <br>
|_  100024  1           2049/udp6  status <br>
135/tcp  open  msrpc         Microsoft Windows RPC <br>
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn <br>
445/tcp  open  microsoft-ds? <br>
2049/tcp open  mountd        1-3 (RPC #100005) <br> 
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows <br>

Host script results: <br>
|_clock-skew: 3m12s <br>
| smb2-security-mode:  <br>
|   2.02:  <br>
|_    Message signing enabled but not required <br>
| smb2-time:  <br>
|   date: 2020-05-19T17:19:54 <br>
|_  start_date: N/A <br>

Service detection performed. Please report any incorrect  <br>results at https://nmap.org/submit/ . <br>

Nmap done at Tue May 19 13:19:16 2020 -- 1 IP address (1 host up) scanned in 243.66 seconds  <br>
