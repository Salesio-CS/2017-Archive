/********************************************************************************
** Form generated from reading UI file 'mkb.ui'
**
** Created by: Qt User Interface Compiler version 5.10.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MKB_H
#define UI_MKB_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLCDNumber>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MKB
{
public:
    QWidget *centralWidget;
    QLCDNumber *content_weight_display;
    QLabel *content_weight_label;
    QLineEdit *IP_box;
    QPushButton *connect_button;
    QPushButton *disconnect_button;
    QLabel *IP_address_label;
    QLineEdit *Circuit_state;
    QLabel *sensor_label;
    QPushButton *circuit_switch;
    QPushButton *update_button;

    void setupUi(QMainWindow *MKB)
    {
        if (MKB->objectName().isEmpty())
            MKB->setObjectName(QStringLiteral("MKB"));
        MKB->resize(291, 159);
        centralWidget = new QWidget(MKB);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        content_weight_display = new QLCDNumber(centralWidget);
        content_weight_display->setObjectName(QStringLiteral("content_weight_display"));
        content_weight_display->setGeometry(QRect(150, 90, 121, 51));
        content_weight_label = new QLabel(centralWidget);
        content_weight_label->setObjectName(QStringLiteral("content_weight_label"));
        content_weight_label->setGeometry(QRect(160, 60, 41, 31));
        IP_box = new QLineEdit(centralWidget);
        IP_box->setObjectName(QStringLiteral("IP_box"));
        IP_box->setGeometry(QRect(20, 30, 111, 25));
        connect_button = new QPushButton(centralWidget);
        connect_button->setObjectName(QStringLiteral("connect_button"));
        connect_button->setGeometry(QRect(20, 60, 111, 21));
        disconnect_button = new QPushButton(centralWidget);
        disconnect_button->setObjectName(QStringLiteral("disconnect_button"));
        disconnect_button->setGeometry(QRect(20, 120, 111, 21));
        IP_address_label = new QLabel(centralWidget);
        IP_address_label->setObjectName(QStringLiteral("IP_address_label"));
        IP_address_label->setGeometry(QRect(30, 0, 111, 31));
        Circuit_state = new QLineEdit(centralWidget);
        Circuit_state->setObjectName(QStringLiteral("Circuit_state"));
        Circuit_state->setEnabled(true);
        Circuit_state->setGeometry(QRect(150, 30, 41, 25));
        Circuit_state->setFrame(true);
        Circuit_state->setReadOnly(true);
        sensor_label = new QLabel(centralWidget);
        sensor_label->setObjectName(QStringLiteral("sensor_label"));
        sensor_label->setGeometry(QRect(160, 0, 111, 31));
        circuit_switch = new QPushButton(centralWidget);
        circuit_switch->setObjectName(QStringLiteral("circuit_switch"));
        circuit_switch->setGeometry(QRect(200, 30, 71, 21));
        update_button = new QPushButton(centralWidget);
        update_button->setObjectName(QStringLiteral("update_button"));
        update_button->setGeometry(QRect(20, 90, 111, 21));
        MKB->setCentralWidget(centralWidget);

        retranslateUi(MKB);

        QMetaObject::connectSlotsByName(MKB);
    } // setupUi

    void retranslateUi(QMainWindow *MKB)
    {
        MKB->setWindowTitle(QApplication::translate("MKB", "\343\201\212\350\215\267\347\211\251? \343\202\201\343\201\243\343\201\241\343\202\203\343\202\217\343\201\213\343\202\213\343\201\247", nullptr));
        content_weight_label->setText(QApplication::translate("MKB", "\345\206\205\345\256\271\351\207\217", nullptr));
        connect_button->setText(QApplication::translate("MKB", "\346\216\245\347\266\232", nullptr));
        disconnect_button->setText(QApplication::translate("MKB", "\345\210\207\346\226\255", nullptr));
        IP_address_label->setText(QApplication::translate("MKB", "IP \343\202\242\343\203\211\343\203\254\343\202\271", nullptr));
        Circuit_state->setText(QApplication::translate("MKB", "NON", nullptr));
        sensor_label->setText(QApplication::translate("MKB", "\343\202\273\343\203\263\343\202\265\343\203\274", nullptr));
        circuit_switch->setText(QApplication::translate("MKB", "\345\210\207\343\202\212\346\233\277\343\201\210", nullptr));
        update_button->setText(QApplication::translate("MKB", "\346\203\205\345\240\261\346\233\264\346\226\260", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MKB: public Ui_MKB {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MKB_H
