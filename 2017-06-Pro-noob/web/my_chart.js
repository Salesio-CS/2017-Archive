function drawTemp(){
  $.getJSON("http://192.168.2.104:8080/web/temp_Value.php", function(tmpdata){
      var chart = new CanvasJS.Chart("charttemp", {
          title: {
              text: "温度データ"  //グラフタイトル
          },
          width: $("#pills-tabContent").innerWidth(),
          data: [{
              type: 'line',  //グラフの種類
              dataPoints: tmpdata //表示するデータ
          }],
      });
      chart.render();
  });
}

function drawHum(){
  $.getJSON("http://192.168.2.104:8080/web/hum_Value.php", function(humdata){
      var chart = new CanvasJS.Chart("charthum", {
          title: {
              text: "湿度データ"  //グラフタイトル
          },
          width: $("#pills-profile").innerWidth(),
          data: [{
              type: 'line',  //グラフの種類
              dataPoints: humdata //表示するデータ
          }]
      });
      chart.render();
  });
}

function drawUghum(){
  $.getJSON("http://192.168.2.104:8080/web/ughum_Value.php", function(ughumdata){
      var chart = new CanvasJS.Chart("chartughum", {
          title: {
              text: "地中湿度データ"  //グラフタイトル
          },
          width: $("#pills-contact").innerWidth(),
          data: [{
              type: 'line',  //グラフの種類
              dataPoints: ughumdata //表示するデータ
          }]
      });
      chart.render();
  });
}

function drawAll() {
  drawTemp();
  drawHum();
  drawUghum();
}

$("#btn_1").click(function() {
  drawAll();
});

$(document).ready(function(){
  drawAll();
});
