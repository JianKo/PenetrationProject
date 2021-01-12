# Advent of Cyber Day6 : Data Elf-iltration
```

[+] Download File : holidaythief.pcap

#1 What data was exfiltrated via DNS?
- DNS 로 필터링한 후 follow stream 기능을 이용해 정보 획득
: 43616e64792043616e652053657269616c204e756d6265722038343931

- wireshark에서 'File' -> 'Export Object' -> Http 로 데이터 추출

#2 What did Little Timmy want to be for Christmas?

2.1 christmaslists.zip 크랙
- zip2john christmaslists.zip >  hash
- john hash
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/Users/scops/tools/mytool/guessing/JohnTheRipper/run/password.lst
december         (christmaslists.zip)
1g 0:00:00:00 DONE 2/3 (2020-08-09 17:11) 33.33g/s 1875Kp/s 1875Kc/s 1875KC/s butterfly..december
Use the "--show" option to display all of the cracked passwords reliably
Session completed.


#3 TryHackMe.jpg 데이터 추출 : steghide
- steghide extract -sf {파일명}



```