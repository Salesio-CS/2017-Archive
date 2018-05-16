#ifndef MKB_H
#define MKB_H

#include <QMainWindow>
#include <QTcpSocket>

namespace Ui {
class MKB;
}

class MKB : public QMainWindow
{
    Q_OBJECT

public:
    explicit MKB(QWidget *parent = 0);
    ~MKB();

private slots:
    // TCP通しング
    void connectToServer(const QString &host, quint16 port);
    void sendData();
    void receiveData();
    void closeConnection();
    void error();

    // その他的な?
    void on_connect_button_clicked();
    void on_IP_box_editingFinished();
    void on_disconnect_button_clicked();
    void on_Circuit_state_returnPressed();
    void on_circuit_switch_clicked();
    void on_content_weight_display_overflow();

    void on_update_button_clicked();

    void on_update_button_2_clicked();

private:
    Ui::MKB *ui;

    // ソケットのやつ
    QTcpSocket *sock;
    QString mess;
    bool connection_flag;

    // 出力メソッド
    void output(QString data);
};

#endif // MKB_H
