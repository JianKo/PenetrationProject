# Advent Of Cyber
```
Arctic Forum

[+] PortScan Command :s udo nmap -sC -sV {IP} 
- Referenced file : Day2Scaning.txt

1. gobuster dir -u {IP} -w {wordlist}
: find folder  "sysadmin"

2. access to http://10.10.33.153:3000/sysadmin
: page source view
: checkout the github 
: -> arctic digital design : https://github.com/ashu-savani/arctic-digital-design
: we get the admin id and password

3. use id n password access to http://10.10.33.153:3000/sysadmin


```