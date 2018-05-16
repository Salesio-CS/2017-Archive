#include "momiage.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    momiage w;
    w.show();

    return a.exec();
}
