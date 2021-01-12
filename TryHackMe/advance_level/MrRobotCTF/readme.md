# Mr Robot CTF
```
--- information Gathering ---
Q1. 사이트로 접근 시에 얻을 수 있는 정보가 눈에 띄지 않으며 숨겨진 정보를 찾기 위해 gobuster를 이용
Sol)
gobuster 이용 명령어
[+] gobuster dir -u {http://{IP}} -w {wordlist file}
1. wordlist 파일은 directory 목록을 가진 파일이어야 함
2. 실험 결과 rockyou.txt로 테스트 했을 때 웹에 대해서 숨겨진 정보를 못 찾음
3. gobuster 결과 파일 참고 : goBusterResult.txt

  Research Note .
    gobuster 에서 왠지 '[ERROR] 2020/07/31 20:40:25 [!] net/http: request canceled (Client.Timeout exceeded while reading body)' 에러가 뜸 조사가 필요함

4. gobuster 를 통해 얻은 숨겨진 위치의 디렉토리 명으로 해당 사이트가 wordpress로 이루어진 사이트임을 알 수 있음

Q2. 사이트 정찰을 위해 필요한 것 중에, robots.txt 가 접근이 되는가? 
Sol)
1. robots.txt가 접근이 됨 robots.txt에서 첫 번째 플래그를 얻을 수 있음. 그리고 나서 'fsocity.dic'에 대한 정보가 추가로 있음
2. fsocity.dic 는 어떤 단어들이 모인 리스트 처럼 보임, 그러므로 Q1 에서 얻은 접근 가능한 디렉토리 목록 중에 로그인에 이용되지 않을까 하는 느낌으로 접근
3. fsocity.dic 는 단어가 많기에 몇 가지 추리기 위해 다음과 같은 것들을 추가로 생각해 볼 필요가 있음
  3.1 단어의 중복이 있는가? -> 리눅스 커맨드 이영 (cat {file | sort |uniq > filesave.txt)
  3.2 단언의 중복이 있다면 줄일 경우에 어떻게 사용할까? -> burp suite insprite 기능
4. '3'의 과정을 거친 결과 : commandDupRemoveFile.txt 참조
```

```
--- Credential Gaining ---
Q3. Q2에서 얻은 파일과 burpsuite의 intruder 기능을 이용해 id와 password를 유추해볼 것
Sol)
1. wp-login 에서 로그인을 시도할 경우 'username invalid' 와 같이 id가 없다는 정보를 주고 있음
2. '1'를 이용해 burpsuit 에서 intruder 기능을 이용하면 Lenght 값이 다른 결과가 wp-login으로 접근할 수 있는 id를 얻을 수 있음
3. '2'를 통해 얻은 아이디로 다시 'password' 를 얻어야 하는데 wordpress 로 이루어진 사이트인 것을 알았다면 wpscan 을 이용가능 'fsocity.dic' 과 'rockyou.txt'를 테스트 해볼 수 있음
 3.1 Command Example
 wpscan --url http://10.10.23.82/wp-login.php --usernames Elliot --passwords ./fsocietDictRemoveDup.txt
 3.2 시간이 오래 걸릴 수 있음
 3.3 wpScanResult.txt 파일 참조

```
```
--- Shell 획득 단계 ---
Q4). 획득학 정보로 로그인 가능 reverse shell을 얻을 수 있는 페이지를 찾은 다음 reverse shell 코드 삽임 후 실행 하면 reverse shell 획득

Q5) robots home에 robot 패스워드가 있음 md5 크랙 후 robot으로 권한 변경 (crackstation)

Q6) nmap에서 권한상승 가능, nmap 구버전은 interactive 모드로 쉘을 실행할 수 있음 : !sh

```


