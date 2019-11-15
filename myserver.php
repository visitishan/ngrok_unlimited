<?php
if(isset($_GET['link'])){
    $txt = $_GET['link'];
    $myfile = file_put_contents('addr2.txt', $txt);
    echo "Success";
}else{
    echo "path OK";
    $myfileContents = file_get_contents("addr2.txt");
    header('Location: '.$myfileContents);
}
?>