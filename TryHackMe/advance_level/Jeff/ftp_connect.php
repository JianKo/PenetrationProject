<?php
/* 
    Todo: I need to finish coding this database backup script.
          also maybe convert it to a wordpress plugin in the future.
*/
$dbFile = 'db_backup/backup.sql';
$ftpFile = 'backup.sql';

$username = "backupmgr";
$password = "SuperS1ckP4ssw0rd123!";

$ftp = ftp_connect("172.20.0.1"); // todo, set up /etc/hosts for the container host


$dir = ftp_nlist($ftp, " ");

echo ''.print_r($dir, true) . '';

?>