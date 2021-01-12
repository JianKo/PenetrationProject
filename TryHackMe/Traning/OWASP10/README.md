# Machine : OWASP Top 10


```
[Day 1] Command Injection Practical
#1 What strange text file is in the website root directory?
: drpepper.txt
- ls 

#2 How many non-root/non-service/non-daemon users are there?
: 0
- cat /etc/passwd

#3 What user is this app running as?
: www-data
- whoami

#4 What is the user's shell set as?
: /usr/sbin/nologin
- cat /etc/passwd

#5 What version of Ubuntu is running?
: 18.04.4
- cat /etc/issue

#6 Print out the MOTD.  What favorite beverage is shown?
: DR PEPPER
- find /* -name 00-header
- cat /etc/update-motd.d/

[Day 2] Broken Authentication Practical
#1 What is the flag that you found in darren's account?
: fe86079416a21a3c99937fea8874b667

#3 What is the flag that you found in arthur's account?
: d9ac0f7db4fda460ac3edeb75d75e16e

- register
- ID : (space)darrrern
- Email : Anything
- passwod : Anything

```