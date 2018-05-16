<?php

$pdo = new PDO('mysql:unix_socket=/tmp/mysql.sock;dbname=temp_data;charset=utf8','root','1b2a3e');

switch ($_SERVER['REQUEST_METHOD']) {
    case 'GET':
        $sth = $pdo->prepare("SELECT recorded_at, temp FROM tempra_test");
        $sth->execute();

        $tempData = array();

        while($row = $sth->fetch(PDO::FETCH_ASSOC)){
                $tempData[]=array(
                'label'=>$row['recorded_at'],
                'y'=>(float)$row['temp']
                );
        }

        //jsonとして出力
        header('Content-type: application/json');
        echo json_encode($tempData);
}

?>
