<?php
try {
  $pdo = new PDO('mysql:unix_socket=/tmp/mysql.sock;dbname=temp_data;charset=utf8','root','1b2a3e');
  switch ($_SERVER['REQUEST_METHOD']) {
	case 'GET':
      $st = $pdo->query("SELECT * FROM tempra_test");
      echo json_encode($st->fetchAll(PDO::FETCH_ASSOC));
      break;

	case 'POST':
    $in = json_decode(file_get_contents('php://input'), true);
    if (!isset($in['id']))
    {
      $st = $pdo->prepare("INSERT INTO tempra_test(recorded_at, temp, hum) VALUES(:recorded_at, :temp, :hum)");
    }
    $st->execute($in);
    echo json_encode("normal end");
    break;
  }
} catch(PDOException $e) {
	exit($e->getMessage());
}
?>
