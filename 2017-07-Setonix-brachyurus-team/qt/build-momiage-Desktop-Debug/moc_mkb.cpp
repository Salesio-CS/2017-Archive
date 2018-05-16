/****************************************************************************
** Meta object code from reading C++ file 'mkb.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.10.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../momiage/mkb.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'mkb.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.10.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_MKB_t {
    QByteArrayData data[17];
    char stringdata0[299];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_MKB_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_MKB_t qt_meta_stringdata_MKB = {
    {
QT_MOC_LITERAL(0, 0, 3), // "MKB"
QT_MOC_LITERAL(1, 4, 15), // "connectToServer"
QT_MOC_LITERAL(2, 20, 0), // ""
QT_MOC_LITERAL(3, 21, 4), // "host"
QT_MOC_LITERAL(4, 26, 4), // "port"
QT_MOC_LITERAL(5, 31, 8), // "sendData"
QT_MOC_LITERAL(6, 40, 11), // "receiveData"
QT_MOC_LITERAL(7, 52, 15), // "closeConnection"
QT_MOC_LITERAL(8, 68, 5), // "error"
QT_MOC_LITERAL(9, 74, 25), // "on_connect_button_clicked"
QT_MOC_LITERAL(10, 100, 25), // "on_IP_box_editingFinished"
QT_MOC_LITERAL(11, 126, 28), // "on_disconnect_button_clicked"
QT_MOC_LITERAL(12, 155, 30), // "on_Circuit_state_returnPressed"
QT_MOC_LITERAL(13, 186, 25), // "on_circuit_switch_clicked"
QT_MOC_LITERAL(14, 212, 34), // "on_content_weight_display_ove..."
QT_MOC_LITERAL(15, 247, 24), // "on_update_button_clicked"
QT_MOC_LITERAL(16, 272, 26) // "on_update_button_2_clicked"

    },
    "MKB\0connectToServer\0\0host\0port\0sendData\0"
    "receiveData\0closeConnection\0error\0"
    "on_connect_button_clicked\0"
    "on_IP_box_editingFinished\0"
    "on_disconnect_button_clicked\0"
    "on_Circuit_state_returnPressed\0"
    "on_circuit_switch_clicked\0"
    "on_content_weight_display_overflow\0"
    "on_update_button_clicked\0"
    "on_update_button_2_clicked"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_MKB[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
      13,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   79,    2, 0x08 /* Private */,
       5,    0,   84,    2, 0x08 /* Private */,
       6,    0,   85,    2, 0x08 /* Private */,
       7,    0,   86,    2, 0x08 /* Private */,
       8,    0,   87,    2, 0x08 /* Private */,
       9,    0,   88,    2, 0x08 /* Private */,
      10,    0,   89,    2, 0x08 /* Private */,
      11,    0,   90,    2, 0x08 /* Private */,
      12,    0,   91,    2, 0x08 /* Private */,
      13,    0,   92,    2, 0x08 /* Private */,
      14,    0,   93,    2, 0x08 /* Private */,
      15,    0,   94,    2, 0x08 /* Private */,
      16,    0,   95,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, QMetaType::QString, QMetaType::UShort,    3,    4,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void MKB::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        MKB *_t = static_cast<MKB *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->connectToServer((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< quint16(*)>(_a[2]))); break;
        case 1: _t->sendData(); break;
        case 2: _t->receiveData(); break;
        case 3: _t->closeConnection(); break;
        case 4: _t->error(); break;
        case 5: _t->on_connect_button_clicked(); break;
        case 6: _t->on_IP_box_editingFinished(); break;
        case 7: _t->on_disconnect_button_clicked(); break;
        case 8: _t->on_Circuit_state_returnPressed(); break;
        case 9: _t->on_circuit_switch_clicked(); break;
        case 10: _t->on_content_weight_display_overflow(); break;
        case 11: _t->on_update_button_clicked(); break;
        case 12: _t->on_update_button_2_clicked(); break;
        default: ;
        }
    }
}

const QMetaObject MKB::staticMetaObject = {
    { &QMainWindow::staticMetaObject, qt_meta_stringdata_MKB.data,
      qt_meta_data_MKB,  qt_static_metacall, nullptr, nullptr}
};


const QMetaObject *MKB::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *MKB::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_MKB.stringdata0))
        return static_cast<void*>(this);
    return QMainWindow::qt_metacast(_clname);
}

int MKB::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMainWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 13)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 13;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 13)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 13;
    }
    return _id;
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
