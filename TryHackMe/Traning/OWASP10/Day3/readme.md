# Day3 : Sensitive Data Exposure (Challenge)
```
Export IP = 10.10.104.196

#1 What is the name of the mentioned directory?
- 로그인 페이지에서 view pageSource 로 주석 처리된 아래의 메세지 확인
<!-- Must remember to do something better with the database than store it in /assets... -->
- '/aassets' 언급하므로 접근 가능

#2 Navigate to the directory you found in question one. What file stands out as being likely to contain sensitive data?
- webapp.db 

#3 Use the supporting material to access the sensitive data. What is the password hash of the admin user?
- 6eea9b7ef19179a06954edd0f6c05ceb

[+] Solve Point
$ sqlite3 webapp.db
sqlite> .tables
sqlite> select * from users;

#4 Crack the hash. What is the admin's plaintext password?
- qwertyuiop
[+] Solve Point
1. crackstation crack MD5

#5 Login as the admin. What is the flag?
- THM{Yzc2YjdkMjE5N2VjMzNhOTE3NjdiMjdl}

```