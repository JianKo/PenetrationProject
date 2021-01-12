# MACHINE : Advent of Cyber
***Day 1***
```
Elf (cookie modifyed attack)
Inventory Managemnt
#1 What is the name of the cookie used for authentication?
:authid

#2 If you decode the cookie, what is the value if the fixed part of the cookie
:v4er9ll1!ss

#3 After accessing his account, what did the user mcinventory request?
: firewall

```

***Day 2***
```
Arctic Forum (OSINT)
#1 What is the path of the hidden page?
: gobuster dir -u {IP} -w{Dictionary}
: /sysadmin

#2 What is the password you found?
: it is OSINT!
: find github repo
: defaultpass

#3 What do you have to take to the "partay"
: read the access page!

```

***Day 3***
```
Evil Elf ( *.pcap analysis)
#1 Whats the destinatnion IP on packet number 998
:63.32.89.195

#2 What item is on the christmas list?
: ps4

#3 Crack buddy's password:
:rainbow 

SHORT NOTE
: #1 click the right button -> scroll down
: #2 statistics ->  EndPoints -> fist list right click -> find
: #3 sha512 dictionary cracking with haschcat command
   hashcat -a 0 -m 1800 hash {password_list_path} --force

```

***Day 4***
```
Trainig
#1 how many visible files are there in the home directory(excluding ./ and ../)?
: 8

#2 What item is the content of files5?
: recipes

#3 which file contains the string password?
: file6 

#4 whay is the IP address in a file in the home folder?
:  10.0.0.05
: Refer linke : https://www.putorius.net/grep-an-ip-address-from-a-file.html

#5 How may users can log into the machine?
: log means login
: cat /etc/passwd | grep /bin/bash
: 3

#6 What is the sha1 hash of file8?
: sha1sum file8

#7 Finding the has?
: find / -name "*shadow*" -exec ls lt {} \; 2>/dev/null 
or
: find / -name "*shadow*" 2>/dev/nul/
```

***Day 5***
```
Trainig
#1 What is Lola's date of birth? Format: Month Date, Year(e.g November 12, 2019)
: December 29, 1900
: exiftool

#2 What is Lola's current occupation?
: Santa's Helpers
: Search by twitter

#3 What phone does Lola make?
: iPhone X
: Search by twitter

#4 What date did Lola first start her photography? Format: dd/mm/yyyy?
: 23/10/2014
: find by waybackmachine!
: and there is flag to the text!

#5 What famous woman does Lola have on her web page?
: ada lovelace
: find by waybackmachine!
: and there is flag to the text!

```

***Day 6***
```
Trainig
#1 What data was exfiltrated via DNS?
: Candy Cane Serial Number 8491
: wireshark *.pcap file
: Answer is in DNS packet 
: HTTP extract

#2 What did Little Timmy want to be for christmas?
: Pentester
: zip2john christmaslists.zip > hash
: john hash

#3 What was hidden within the file?
: RFC527
: cat christsmaslisttimmy.txt


```

***Day 7***
```
Skilling Up
Command : nmap -A -sC -sV 10.10.205.160 -oN Day7Scaaning.txt
#1 How many TCP ports number under 1000 are open?
:3

#2 What is the name of the OS of the host?
:linux

#3 What version of ssh is running?
:7.4

#4 what is the name of the file that is accessbile on the server you found running?
:interesting.file
```

***Day 8***
```
SUID Shenanigans
#1 What port is ssh running on?
: 65534

#2 Find and run a file as igor, Read the file /home/igor/flag.txt
: find / -perm -4000 -user igor 2>/dev/null
: /usr/bin/nmap -iL /home/igor/flag1.txt

#3 Find another binary file that has the SUID bit set. Using this file, can you become the root user and read the /root/flag2.txt file?
: find / -perm -4000 -user root 2>/dev/null
: each lines analysis
: /usr/bin/system-contorl -> bash or /bin/bash!
```

***Day 9***
```
Requests
#1 What is the value of the flag?
: CRIPtKiDd
: refer Directory Day9 *py file
```

***Day 10***
Metsploit-a-ho-ho-ho
tag: nikto, struts2, 
```
#1 Compromise the web server using Metasploit. What is flag1?
: flag find command
: find . -type f -iname "flag"

#2 Now you've compromised the web server, get onto the main system. What is Santa's SSH password?
: cat /home/santa/ssh_creds.txt

#3 who is on line 148 of the naughty list?
: sed '148!d' {file name}

#4 who is on line 52 of the nice list?
: sed '52!d' {file name}

```

***Day 11***
```
Elf Applications
#1 What is the password inside the creds, txt file?
: securepassword123
: # method
: showmount -e 10.10.12.24
: mount 10.10.12.24:/opt/files /mnt/nfs
: check it local path '/mnt/nfs'

#2 What is the name of the file running on port 21?
: file.txt
: # method
: ftp -> open -> 10.10.12.24 (anonymous,anonymous)

#3 What is the password after enumeraing the databases?
: bestpassword
: # method
: @ myqsl -u root -h 10.10.12.24 -p
: @ input password 
: show databases;
: use database_name;
: show tables;
: select * from table_name;
```


***Day 12***
```
Elf Applications
#1 What is the md5 hashsum of the encrypted note1 file?
: md5sum {file}


#2 Where was elf Bod told to meet Alice?
: Santa's Grotto
: # method
: gpg -d {file}

#3 Decrypt note2 and obtain the flag!
:# method
: openssl rsautl -decrypt -inkey priavet.ket -in {file_encrypt} -out {save_decrypt_file}
```

***Day 13***
```
Accumlate
#1 A web Server is running on the target. what is the hidden directory which the
website lives on?
: retro

#2 Gain initial access and read the contents fo user.txt
: remmina rdp cliet use it

#3 [Optional] Elevate privileges and read the content of root.txt
:hhupd.exe Privilege Escalte
```

***Day 14***
```
Unknown Storage
Accumlate
#1 What is the name of the file you found?
:employee_name.txt

#2 What is in the file?
:mcchef

```