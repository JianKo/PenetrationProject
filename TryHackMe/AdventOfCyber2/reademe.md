# Advent of Cyber All Review

## Web Exploitation
```
[Day1] : A Christmas Crisis
-> Cookie Modifyed

1. Register Anything Credential && Login
2. Cookie Analysis &&& auth field decoded
3. auth field user modifyed "santa"
4. All Checked && Get Flag

[Day2] : The Elf Strikes Back!
-> File Upload Bypass && Reverse Shell

1. Access to "?id=ODIzODI5MTNiYmYw"
2. accept file : images extension
3. change to shell.php -> shell.jpeg.php 
4. file upload path : /uploads/
5. Reverse Shell Conneciton && read "/var/www/flag.txt"

[Day3] : Christmas Chaos
-> Crendential Brute Forcing

1. (admin,12345), Login Success
2. Read Flag


[Day4] : Santa's Watching
-> Parameter Fuzzing Skill, [wfuzz]

1. wfuzz -c -z file, {FILE_PATH} {TARGET_URL}?{PARAMETER}=FUZZ

[Day5] : Someone stole Santa's gift list !
-> SQL injection
1. login Page -> "/santapanel"
2. SQLI Payload
- username : admin' or '1' --
- password : #

3. sqlmap -r {BURPSUITE_SAVE_ITEM_FILE} --tamper=space2comment --dump-all --dbms sqlite


[Day6] : Be careful with what you wish on a Christmas night
-> Cross Site Scripting
1. Stored Cross-Stie Scripting
2. Query String Parameter => q
3. ZAP -> 2

```