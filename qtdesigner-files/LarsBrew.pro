#-------------------------------------------------
#
# Project created by QtCreator 2016-09-08T16:56:19
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = LarsBrew
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    automation.cpp

HEADERS  += mainwindow.h \
    automation.h

FORMS    += mainwindow.ui \
    automation.ui \
    logging.ui \
    configuration.ui \
    information.ui
