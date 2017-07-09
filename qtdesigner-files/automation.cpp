#include "automation.h"
#include "ui_automation.h"

automation::automation(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::automation)
{
    ui->setupUi(this);
}

automation::~automation()
{
    delete ui;
}
