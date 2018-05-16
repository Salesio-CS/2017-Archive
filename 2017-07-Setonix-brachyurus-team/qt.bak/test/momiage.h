#ifndef MOMIAGE_H
#define MOMIAGE_H

#include <QMainWindow>
#include <QTcpSocket>

namespace Ui {
class momiage;
}

class momiage : public QMainWindow
{
    Q_OBJECT

public:
    explicit momiage(QWidget *parent = 0);
    ~momiage();

private slots:
    // TCP通しング
    void connectToServer(const QString &host, quint16 port);
    void sendData();
    void receiveData();
    void error();
    void closeConnection();

    // ボタンクリック時動きング
    void on_momiage_button_clicked();
    void on_content_weight_button_clicked();
    void on_close_button_clicked();
    void on_circuit_switch_button_clicked();
    void on_circuit_on_button_clicked();
    void on_circuit_off_button_clicked();

    void on_clean_button_clicked();

private:
    Ui::momiage *ui;
    // ソケットのやつ
    QTcpSocket *sock;
    QString mess;
    bool connection_flag;

    // 出力メソッド
    void output(QString data);
};

#endif // MOMIAGE_H
