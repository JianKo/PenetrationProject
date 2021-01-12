# Machine : Vulnersity
# TITLE :  Gobuster Scanning result

# Directory Tree Scan
## command  : gobuster dir -u http://10.10.19.165:3333 -w directory_guessing_list.txt

Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_) <br>

[+] Url:            http://10.10.19.165:3333 <br>
[+] Threads:        10 <br>
[+] Wordlist:       directory_guessing_list.txt<br>
[+] Status codes:   200,204,301,302,307,401,403 <br>
[+] User Agent:     gobuster/3.0.1 <br>
[+] Timeout:        10s <br>

2020/05/22 22:39:09 Starting gobuster

/images (Status: 301) <br>
/css (Status: 301) <br>
Progress: 585 / 207644 (0.28%)load: 1.41  cmd: gobuster 3281 waiting 0.10u 0.08s <br>
Progress: 675 / 207644 (0.33%) <br>
/js (Status: 301) <br>
/fonts (Status: 301) <br>
/internal (Status: 301) <br>

# File Upload Point
## command : gobuster dir -u http://10.10.19.165:3333/internal/ -w directory_guessing_list.txt

Gobuster v3.0.1 <br>
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_) <br>


[+] Url:            http://10.10.131.4:3333/internal <br>
[+] Threads:        10 <br>
[+] Wordlist:       directory_guessing_list.txt <br>
[+] Status codes:   200,204,301,302,307,401,403 <br>
[+] User Agent:     gobuster/3.0.1 <br>
[+] Timeout:        10s <br>

2020/05/23 16:56:26 Starting gobuster <br>

/uploads (Status: 301) <br>