/********************************************************************************
** Form generated from reading UI file 'momiage.ui'
**
** Created by: Qt User Interface Compiler version 5.9.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MOMIAGE_H
#define UI_MOMIAGE_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_momiage
{
public:
    QWidget *centralWidget;
    QPushButton *momiage_button;
    QTextEdit *output_box;
    QPushButton *content_weight_button;
    QPushButton *close_button;
    QPushButton *circuit_switch_button;
    QPushButton *circuit_on_button;
    QPushButton *circuit_off_button;
    QLabel *label;
    QLabel *label_2;
    QLineEdit *address_box;
    QLineEdit *port_box;
    QPushButton *clean_button;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;
    QToolBar *toolBar;

    void setupUi(QMainWindow *momiage)
    {
        if (momiage->objectName().isEmpty())
            momiage->setObjectName(QStringLiteral("momiage"));
        momiage->resize(452, 370);
        centralWidget = new QWidget(momiage);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        momiage_button = new QPushButton(centralWidget);
        momiage_button->setObjectName(QStringLiteral("momiage_button"));
        momiage_button->setGeometry(QRect(10, 120, 211, 41));
        output_box = new QTextEdit(centralWidget);
        output_box->setObjectName(QStringLiteral("output_box"));
        output_box->setGeometry(QRect(230, 10, 211, 261));
        content_weight_button = new QPushButton(centralWidget);
        content_weight_button->setObjectName(QStringLiteral("content_weight_button"));
        content_weight_button->setGeometry(QRect(120, 180, 101, 31));
        close_button = new QPushButton(centralWidget);
        close_button->setObjectName(QStringLiteral("close_button"));
        close_button->setGeometry(QRect(11, 250, 211, 21));
        circuit_switch_button = new QPushButton(centralWidget);
        circuit_switch_button->setObjectName(QStringLiteral("circuit_switch_button"));
        circuit_switch_button->setGeometry(QRect(10, 180, 101, 31));
        circuit_on_button = new QPushButton(centralWidget);
        circuit_on_button->setObjectName(QStringLiteral("circuit_on_button"));
        circuit_on_button->setGeometry(QRect(11, 220, 101, 25));
        circuit_off_button = new QPushButton(centralWidget);
        circuit_off_button->setObjectName(QStringLiteral("circuit_off_button"));
        circuit_off_button->setGeometry(QRect(120, 220, 101, 25));
        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(10, 10, 71, 17));
        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(10, 60, 81, 17));
        address_box = new QLineEdit(centralWidget);
        address_box->setObjectName(QStringLiteral("address_box"));
        address_box->setGeometry(QRect(10, 30, 171, 25));
        port_box = new QLineEdit(centralWidget);
        port_box->setObjectName(QStringLiteral("port_box"));
        port_box->setGeometry(QRect(10, 80, 171, 25));
        clean_button = new QPushButton(centralWidget);
        clean_button->setObjectName(QStringLiteral("clean_button"));
        clean_button->setGeometry(QRect(10, 280, 431, 25));
        momiage->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(momiage);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 452, 22));
        momiage->setMenuBar(menuBar);
        mainToolBar = new QToolBar(momiage);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        momiage->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(momiage);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        momiage->setStatusBar(statusBar);
        toolBar = new QToolBar(momiage);
        toolBar->setObjectName(QStringLiteral("toolBar"));
        momiage->addToolBar(Qt::TopToolBarArea, toolBar);

        retranslateUi(momiage);

        QMetaObject::connectSlotsByName(momiage);
    } // setupUi

    void retranslateUi(QMainWindow *momiage)
    {
        momiage->setWindowTitle(QApplication::translate("momiage", "momiage", Q_NULLPTR));
        momiage_button->setText(QApplication::translate("momiage", "\346\216\245\347\266\232 (eating momiage)", Q_NULLPTR));
        content_weight_button->setText(QApplication::translate("momiage", "\345\206\205\345\256\271\351\207\217\345\217\226\345\276\227", Q_NULLPTR));
        close_button->setText(QApplication::translate("momiage", "\346\216\245\347\266\232\343\202\255\343\203\253", Q_NULLPTR));
        circuit_switch_button->setText(QApplication::translate("momiage", "\345\233\236\350\267\257\347\212\266\346\205\213\345\217\226\345\276\227", Q_NULLPTR));
        circuit_on_button->setText(QApplication::translate("momiage", "\345\233\236\350\267\257\343\202\252\343\203\263", Q_NULLPTR));
        circuit_off_button->setText(QApplication::translate("momiage", "\345\233\236\350\267\257\343\202\252\343\203\225", Q_NULLPTR));
        label->setText(QApplication::translate("momiage", "IP Address", Q_NULLPTR));
        label_2->setText(QApplication::translate("momiage", "PORT Number", Q_NULLPTR));
        port_box->setText(QApplication::translate("momiage", "4096", Q_NULLPTR));
        clean_button->setText(QApplication::translate("momiage", "clean", Q_NULLPTR));
        toolBar->setWindowTitle(QApplication::translate("momiage", "toolBar", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class momiage: public Ui_momiage {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MOMIAGE_H
