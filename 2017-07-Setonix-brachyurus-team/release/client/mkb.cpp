#include <QtCore/QEventLoop>
#include <QtCore/QTimer>

#include "mkb.h"
#include "ui_mkb.h"

MKB::MKB(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MKB)
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

MKB::~MKB()
{
    delete ui;
    sendData();

    receiveData();

    closeConnection();

    delete ui;
    delete sock;
}

// -----------------------------------------------------------------------------
// TCP通信関連
// -----------------------------------------------------------------------------
//接続の実行
void MKB::connectToServer(const QString &host, quint16 port)
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
void MKB::sendData()
{
    if (!connection_flag)
        return;

    if (mess == "")
        return;

    //UTF-8化
    QByteArray utf8_str = mess.toUtf8();

    //送信
    sock->write(utf8_str);
}

//データ受信 (tcpSocket の readyRead() シグナル)
void MKB::receiveData()
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
    {
        closeConnection();
        return;
    }

    QStringList rcv_list = rcv_data.split(" ");
    if (3 <= rcv_list.size())
    {
        if (rcv_list.at(0) == "not")
        {
            if (rcv_list.at(1) == "cw")
            {
                QString num = rcv_list.at(2);
                ui->content_weight_display->display(num.toInt());
            }
            if (rcv_list.at(1) == "cs")
            {
                QString state;
                if (rcv_list.at(rcv_list.size() - 1) == "1")
                    state = "ON";
                else
                    state = "OFF";
                ui->Circuit_state->setText(state);
            }
            if (rcv_list.at(1) == "upd")
            {
                QString num = rcv_list.at(2);
                ui->content_weight_display->display(num.toInt());
                QString state;
                if (rcv_list.at(3) == "1")
                    state = "ON";
                else
                    state = "OFF";
                ui->Circuit_state->setText(state);
            }
        }
    }
}

//切断 (tcpSocket の disconnected() シグナル)
void MKB::closeConnection()
{
    if (!connection_flag)
        return;

    connection_flag = false;
    sock->close();

    ui->Circuit_state->setText("NON");
    ui->content_weight_display->display(0);
}

//エラー (tcpSocket の error() シグナル)
void MKB::error()
{
    char str[114514];
    sprintf(str, "error : %s", sock->errorString().toUtf8().constData());
    output(QString::fromLocal8Bit(str));
    connection_flag = false;
    sock->close();
}

// 出力メソッド
void MKB::output(QString data)
{
    ui->Circuit_state->text() = data;
}

// -----------------------------------------------------------------------------
// ボタン押されたら送るゾ
// -----------------------------------------------------------------------------
// 接続
void MKB::on_connect_button_clicked()
{
    if (connection_flag)
        return;

    QString addr = "";
    QString port_str = "50093";

    addr = ui->IP_box->text();

    if (addr.size() == 0 || port_str.size() ==0)
        return;

    //ポート番号の数値化
    bool is_ok;
    int port = port_str.toInt(&is_ok, 10);
    if (!is_ok || port <= 0) return;

    //接続の実行
    this->connectToServer(addr, port);

    // 更新
    on_update_button_clicked();
}

// 死にたい
void MKB::on_disconnect_button_clicked()
{
    if (!connection_flag)
        return;

    mess = "req close";
    sendData();
}

// 更新ゾ
void MKB::on_update_button_clicked()
{
    mess = "req cw";
    sendData();
    //mess = "req upd";
    //endData();
    //sock->waitForReadyRead();
    //receiveData();
}
void MKB::on_update_button_2_clicked()
{
    on_update_button_clicked();
}

// 切り替え
void MKB::on_circuit_switch_clicked()
{
    mess = "req cs";
    sendData();
    sock->waitForReadyRead(1000);
    if (ui->Circuit_state->text() == "ON")
        mess = "req cof";
    else if (ui->Circuit_state->text() == "OFF")
        mess = "req con";
    else
        mess = "";

    sendData();
}

// その他 殻にしときましょ
void MKB::on_IP_box_editingFinished()
{

}

void MKB::on_Circuit_state_returnPressed()
{

}

void MKB::on_content_weight_display_overflow()
{

}
