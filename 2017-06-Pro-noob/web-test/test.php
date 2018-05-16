<?php
try {
    $pdo = new PDO('mysql:unix_socket=/tmp/mysql.sock;dbname=temp_data;charset=utf8','root','1b2a3e');
    print '接続完了';

    $sql=$pdo->prepare('insert into tempra_test values(null, ?, ?, ?)');
    if ($sql->execute(["2018/01/20 21:01:40", 100, 100])) {
            echo '追加に成功しました。\n';
	} else {
	    echo '追加に失敗しました。\n';
	}
} catch(PDOException $e) {
    print '接続失敗';
    exit($e->getMessage());
}

?>
