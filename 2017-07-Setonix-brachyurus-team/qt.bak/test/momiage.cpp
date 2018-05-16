#include "momiage.h"
#include "ui_momiage.h"

// https://qiita.com/mizu-kazu/items/98259353efe80910f213

// コンストラクタ
momiage::momiage(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::momiage)
{
    ui->setupUi(this);

    // シグナルとSLOTの?
    //インスタンス生成
    this->sock = new QTcpSocket(this);
    //接続
    connect(sock, SIGNAL(connected()), this, SLOT(sendData()));
    //切断
    connect(sock, SIGNAL(disconnected()), this, SLOT(closeConnection()));
    //受信
    connect(sock, SIGNAL(readyRead()), this, SLOT(receiveData()));
    //エラー
    connect(sock, SIGNAL(error(QAbstractSocket::SocketError)), this, SLOT(error()));

    mess = "connection";
    connection_flag = false;
}

// デストラクタ
momiage::~momiage()
{
    mess = "req close";
    sendData();

    receiveData();

    closeConnection();

    delete ui;
    delete sock;
}

// 出力メソッド
void momiage::output(QString data)
{
    ui->output_box->append(data);
}

// -----------------------------------------------------------------------------
// ボタン押されたら送るゾ
// -----------------------------------------------------------------------------
// 接続
void momiage::on_momiage_button_clicked()
{
    QString addr = "";
    QString port_str = "4096";

    addr = ui->address_box->text();
    port_str = ui->port_box->text();

    if (addr.size() == 0 || port_str.size() ==0)
        return;

    //ポート番号の数値化
    bool is_ok;
    int port = port_str.toInt(&is_ok, 10);
    if (!is_ok || port <= 0) return;

    //接続の実行
    this->connectToServer(addr, port);
}

// 金くれ
void momiage::on_content_weight_button_clicked()
{
    mess = "req cw";
    sendData();
}

// すうぃっちキラメキラリ
void momiage::on_circuit_switch_button_clicked()
{
    mess = "req cs";
    sendData();
}

// スイッチオォン
void momiage::on_circuit_on_button_clicked()
{
    mess = "req con";
    sendData();
}

// スイッチオフ会0人
void momiage::on_circuit_off_button_clicked()
{
    mess = "req cof";
    sendData();
}

// 死にたい
void momiage::on_close_button_clicked()
{
    mess = "req close";
    sendData();
}

// 出力箱をクリア
void momiage::on_clean_button_clicked()
{
    ui->output_box->setText("");
}

// -----------------------------------------------------------------------------
// TCP通信関連
// -----------------------------------------------------------------------------
//接続の実行
void momiage::connectToServer(const QString &host, quint16 port)
{
    if (connection_flag)
        return;

    char str[114514];
    sprintf(str, "conn: host=%s, port=%d", host.toUtf8().constData(), port);
    output(QString::fromLocal8Bit(str));

    connection_flag = true;

    mess = "";
    sock->connectToHost(host, port);
}

//データ送信 (tcpSocket の connected() シグナル)
void momiage::sendData()
{
    if (!connection_flag)
        return;

    if (mess == "")
        return;

    //UTF-8化
    QByteArray utf8_str = mess.toUtf8();

    char str[114514];
    sprintf(str, "send: %s", utf8_str.constData());
    output(QString::fromLocal8Bit(str));

    //送信
    sock->write(utf8_str);
}

//データ受信 (tcpSocket の readyRead() シグナル)
void momiage::receiveData()
{
    //受信
    QByteArray rcv_bytes = sock->readAll();

    QString rcv_data;
    //データなし？
    if (rcv_bytes.length() == 0)
        rcv_data = "[no data]";
    //データあり → UTF8でQString化
    else rcv_data = QString::fromUtf8(rcv_bytes);

    if (rcv_data == "not close")
        closeConnection();

    //表示
    char str[114514];
    sprintf(str, "recv : %s", rcv_data.toUtf8().constData());
    output(QString::fromLocal8Bit(str));
}

//切断 (tcpSocket の disconnected() シグナル)
void momiage::closeConnection()
{
    if (!connection_flag)
        return;

    connection_flag = false;
    sock->close();
}

//エラー (tcpSocket の error() シグナル)
void momiage::error()
{
    char str[114514];
    sprintf(str, "error : %s", sock->errorString().toUtf8().constData());
    output(QString::fromLocal8Bit(str));
    connection_flag = false;
    sock->close();
}
