<?php
$MyIp = $_SERVER['HTTP_X_FORWARDED_FOR'];

$File = '../../log/info.txt';
$FP = fopen($File, 'a') or die("Cant Open The File...");
fwrite($FP, "IP : $MyIp\n");
fclose($FP);

$D_File = 'ip_data.txt';
$D_FP = fopen($D_File, 'w');
fwrite($D_FP, $MyIp);
fclose($D_FP);

header('location:index.html');
?>