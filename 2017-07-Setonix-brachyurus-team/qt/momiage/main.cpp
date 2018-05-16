#include "mkb.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MKB w;
    w.show();

    return a.exec();
}
