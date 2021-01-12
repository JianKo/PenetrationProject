# Emdee five for life
```
Export IP=178.62.100.75:31225
```

## Exploit Code
```
mport hashlib
import requests
from bs4 import BeautifulSoup
import re

# 세션 유지
req = requests.session()
url = "http://178.62.100.75:31225/"

r = req.get(url)

soup = BeautifulSoup(r.text,"lxml")
hash_string = soup.find("h3",{"align":"center"}).text

# MD5 암호화
result = hashlib.md5(hash_string.encode()).hexdigest()
data = {"hash" : result}

# 암호화 된 텍스트 재전송 후 플래그 획득
reqUrl = req.post(url,data=data)
print(reqUrl.text

```