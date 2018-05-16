<!-- タイトル -->
<!DOCTYPE html>
<html lang = "ja">
<?php mb_internal_encoding("UTF-8"); ?>
<head>
<title>傘viewer</title>
</head>
<body>

<h1>稼働状況</h1>

<!-- GET通信 -->

<!-- 192.168.0.125に送信 -->
<?php

$query = array('source' => '1');
$query = http_build_query($query);

?>

<form <?php echo 'https://192.168.0.125:8008/' . $query ; ?> method = 'get'>
<input type = 'submit' value = 'データの取得'><br>

<!-- フォーム -->

<?php

$time = getdate();

echo nl2br("Updade Time : ".$time['year']." ".$time['month']." ".$time['mday']." ".
	$time['weekday']." ".$time['hours'].":".$time['minutes'].":".$time['seconds']."\n"); 
echo nl2br("ALL : 2 , Go out : 2 , Open : 1 , Unknown : 0\n");


echo $_GET['source'];

?>

</body>