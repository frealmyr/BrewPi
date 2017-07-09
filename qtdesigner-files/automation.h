#ifndef AUTOMATION_H
#define AUTOMATION_H

#include <QWidget>

namespace Ui {
class automation;
}

class automation : public QWidget
{
    Q_OBJECT

public:
    explicit automation(QWidget *parent = 0);
    ~automation();

private:
    Ui::automation *ui;
};

#endif // AUTOMATION_H
