# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.frm_temp1 = QtWidgets.QFrame(self.centralWidget)
        self.frm_temp1.setGeometry(QtCore.QRect(10, 20, 141, 111))
        self.frm_temp1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_temp1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_temp1.setLineWidth(1)
        self.frm_temp1.setObjectName("frm_temp1")
        self.lcd_temp1 = QtWidgets.QLCDNumber(self.frm_temp1)
        self.lcd_temp1.setGeometry(QtCore.QRect(10, 40, 121, 61))
        self.lcd_temp1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcd_temp1.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcd_temp1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd_temp1.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_temp1.setObjectName("lcd_temp1")
        self.lbl_temp1 = QtWidgets.QLabel(self.frm_temp1)
        self.lbl_temp1.setGeometry(QtCore.QRect(10, 10, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_temp1.setFont(font)
        self.lbl_temp1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_temp1.setObjectName("lbl_temp1")
        self.frm_temp2 = QtWidgets.QFrame(self.centralWidget)
        self.frm_temp2.setGeometry(QtCore.QRect(171, 20, 141, 111))
        self.frm_temp2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_temp2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_temp2.setLineWidth(1)
        self.frm_temp2.setObjectName("frm_temp2")
        self.lcd_temp2 = QtWidgets.QLCDNumber(self.frm_temp2)
        self.lcd_temp2.setGeometry(QtCore.QRect(10, 40, 121, 61))
        self.lcd_temp2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcd_temp2.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcd_temp2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd_temp2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_temp2.setObjectName("lcd_temp2")
        self.lbl_temp2 = QtWidgets.QLabel(self.frm_temp2)
        self.lbl_temp2.setGeometry(QtCore.QRect(10, 10, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_temp2.setFont(font)
        self.lbl_temp2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_temp2.setObjectName("lbl_temp2")
        self.frm_temp3 = QtWidgets.QFrame(self.centralWidget)
        self.frm_temp3.setGeometry(QtCore.QRect(331, 20, 141, 111))
        self.frm_temp3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_temp3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_temp3.setLineWidth(1)
        self.frm_temp3.setObjectName("frm_temp3")
        self.lcd_temp3 = QtWidgets.QLCDNumber(self.frm_temp3)
        self.lcd_temp3.setGeometry(QtCore.QRect(10, 40, 121, 61))
        self.lcd_temp3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcd_temp3.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcd_temp3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd_temp3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_temp3.setObjectName("lcd_temp3")
        self.lbl_temp3 = QtWidgets.QLabel(self.frm_temp3)
        self.lbl_temp3.setGeometry(QtCore.QRect(10, 10, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_temp3.setFont(font)
        self.lbl_temp3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_temp3.setObjectName("lbl_temp3")
        self.frm_temp4 = QtWidgets.QFrame(self.centralWidget)
        self.frm_temp4.setGeometry(QtCore.QRect(491, 20, 141, 111))
        self.frm_temp4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_temp4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_temp4.setLineWidth(1)
        self.frm_temp4.setObjectName("frm_temp4")
        self.lcd_temp4 = QtWidgets.QLCDNumber(self.frm_temp4)
        self.lcd_temp4.setGeometry(QtCore.QRect(10, 40, 121, 61))
        self.lcd_temp4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcd_temp4.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcd_temp4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd_temp4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_temp4.setObjectName("lcd_temp4")
        self.lbl_temp4 = QtWidgets.QLabel(self.frm_temp4)
        self.lbl_temp4.setGeometry(QtCore.QRect(10, 10, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_temp4.setFont(font)
        self.lbl_temp4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_temp4.setObjectName("lbl_temp4")
        self.frm_temp5 = QtWidgets.QFrame(self.centralWidget)
        self.frm_temp5.setGeometry(QtCore.QRect(650, 20, 141, 111))
        self.frm_temp5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_temp5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_temp5.setLineWidth(1)
        self.frm_temp5.setObjectName("frm_temp5")
        self.lcd_temp5 = QtWidgets.QLCDNumber(self.frm_temp5)
        self.lcd_temp5.setGeometry(QtCore.QRect(10, 40, 121, 61))
        self.lcd_temp5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcd_temp5.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcd_temp5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd_temp5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_temp5.setObjectName("lcd_temp5")
        self.lbl_temp5 = QtWidgets.QLabel(self.frm_temp5)
        self.lbl_temp5.setGeometry(QtCore.QRect(10, 10, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_temp5.setFont(font)
        self.lbl_temp5.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_temp5.setObjectName("lbl_temp5")
        self.frm_relaybuttons = QtWidgets.QFrame(self.centralWidget)
        self.frm_relaybuttons.setGeometry(QtCore.QRect(520, 149, 271, 321))
        self.frm_relaybuttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_relaybuttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_relaybuttons.setObjectName("frm_relaybuttons")
        self.btn_relay1on = QtWidgets.QPushButton(self.frm_relaybuttons)
        self.btn_relay1on.setGeometry(QtCore.QRect(10, 30, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_relay1on.setFont(font)
        self.btn_relay1on.setStyleSheet("")
        self.btn_relay1on.setObjectName("btn_relay1on")
        self.btn_relay1off = QtWidgets.QPushButton(self.frm_relaybuttons)
        self.btn_relay1off.setEnabled(False)
        self.btn_relay1off.setGeometry(QtCore.QRect(10, 170, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_relay1off.setFont(font)
        self.btn_relay1off.setStyleSheet("")
        self.btn_relay1off.setObjectName("btn_relay1off")
        self.btn_relay2off = QtWidgets.QPushButton(self.frm_relaybuttons)
        self.btn_relay2off.setEnabled(False)
        self.btn_relay2off.setGeometry(QtCore.QRect(140, 170, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_relay2off.setFont(font)
        self.btn_relay2off.setStyleSheet("")
        self.btn_relay2off.setObjectName("btn_relay2off")
        self.btn_relay2on = QtWidgets.QPushButton(self.frm_relaybuttons)
        self.btn_relay2on.setGeometry(QtCore.QRect(140, 30, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_relay2on.setFont(font)
        self.btn_relay2on.setStyleSheet("")
        self.btn_relay2on.setObjectName("btn_relay2on")
        self.frm_tempctrl = QtWidgets.QFrame(self.centralWidget)
        self.frm_tempctrl.setGeometry(QtCore.QRect(9, 150, 501, 321))
        self.frm_tempctrl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_tempctrl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_tempctrl.setObjectName("frm_tempctrl")
        self.spn_relay1max = QtWidgets.QDoubleSpinBox(self.frm_tempctrl)
        self.spn_relay1max.setGeometry(QtCore.QRect(10, 60, 231, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spn_relay1max.sizePolicy().hasHeightForWidth())
        self.spn_relay1max.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.spn_relay1max.setFont(font)
        self.spn_relay1max.setToolTipDuration(-1)
        self.spn_relay1max.setStyleSheet("QDoubleSpinBox { border: 2px inset grey; } \n"
"QDoubleSpinBox::up-button { subcontrol-position: left; width: 70px; height: 65px;}\n"
"QDoubleSpinBox::down-button { subcontrol-position: right; width: 70px; height: 65px;}")
        self.spn_relay1max.setWrapping(False)
        self.spn_relay1max.setFrame(True)
        self.spn_relay1max.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_relay1max.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spn_relay1max.setSpecialValueText("")
        self.spn_relay1max.setAccelerated(False)
        self.spn_relay1max.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spn_relay1max.setKeyboardTracking(True)
        self.spn_relay1max.setSingleStep(0.5)
        self.spn_relay1max.setProperty("value", 20.0)
        self.spn_relay1max.setObjectName("spn_relay1max")
        self.spn_relay2max = QtWidgets.QDoubleSpinBox(self.frm_tempctrl)
        self.spn_relay2max.setGeometry(QtCore.QRect(260, 60, 231, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spn_relay2max.sizePolicy().hasHeightForWidth())
        self.spn_relay2max.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.spn_relay2max.setFont(font)
        self.spn_relay2max.setToolTipDuration(-1)
        self.spn_relay2max.setStyleSheet("QDoubleSpinBox { border: 2px inset grey; } \n"
"QDoubleSpinBox::up-button { subcontrol-position: left; width: 70px; height: 65px;}\n"
"QDoubleSpinBox::down-button { subcontrol-position: right; width: 70px; height: 65px;}")
        self.spn_relay2max.setWrapping(False)
        self.spn_relay2max.setFrame(True)
        self.spn_relay2max.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_relay2max.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spn_relay2max.setSpecialValueText("")
        self.spn_relay2max.setAccelerated(False)
        self.spn_relay2max.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spn_relay2max.setKeyboardTracking(True)
        self.spn_relay2max.setSingleStep(0.5)
        self.spn_relay2max.setProperty("value", 20.0)
        self.spn_relay2max.setObjectName("spn_relay2max")
        self.spn_relay2min = QtWidgets.QDoubleSpinBox(self.frm_tempctrl)
        self.spn_relay2min.setGeometry(QtCore.QRect(260, 220, 231, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spn_relay2min.sizePolicy().hasHeightForWidth())
        self.spn_relay2min.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.spn_relay2min.setFont(font)
        self.spn_relay2min.setToolTipDuration(-1)
        self.spn_relay2min.setStyleSheet("QDoubleSpinBox { border: 2px inset grey; } \n"
"QDoubleSpinBox::up-button { subcontrol-position: left; width: 70px; height: 65px;}\n"
"QDoubleSpinBox::down-button { subcontrol-position: right; width: 70px; height: 65px;}")
        self.spn_relay2min.setWrapping(False)
        self.spn_relay2min.setFrame(True)
        self.spn_relay2min.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_relay2min.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spn_relay2min.setSpecialValueText("")
        self.spn_relay2min.setAccelerated(False)
        self.spn_relay2min.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spn_relay2min.setKeyboardTracking(True)
        self.spn_relay2min.setSingleStep(0.5)
        self.spn_relay2min.setProperty("value", 20.0)
        self.spn_relay2min.setObjectName("spn_relay2min")
        self.spn_relay1min = QtWidgets.QDoubleSpinBox(self.frm_tempctrl)
        self.spn_relay1min.setGeometry(QtCore.QRect(10, 220, 231, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spn_relay1min.sizePolicy().hasHeightForWidth())
        self.spn_relay1min.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.spn_relay1min.setFont(font)
        self.spn_relay1min.setToolTipDuration(-1)
        self.spn_relay1min.setStyleSheet("QDoubleSpinBox { border: 2px inset grey; } \n"
"QDoubleSpinBox::up-button { subcontrol-position: left; width: 70px; height: 65px;}\n"
"QDoubleSpinBox::down-button { subcontrol-position: right; width: 70px; height: 65px;}")
        self.spn_relay1min.setWrapping(False)
        self.spn_relay1min.setFrame(True)
        self.spn_relay1min.setAlignment(QtCore.Qt.AlignCenter)
        self.spn_relay1min.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spn_relay1min.setSpecialValueText("")
        self.spn_relay1min.setAccelerated(False)
        self.spn_relay1min.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spn_relay1min.setKeyboardTracking(True)
        self.spn_relay1min.setSingleStep(0.5)
        self.spn_relay1min.setProperty("value", 20.0)
        self.spn_relay1min.setObjectName("spn_relay1min")
        self.lbl_relay1max = QtWidgets.QLabel(self.frm_tempctrl)
        self.lbl_relay1max.setGeometry(QtCore.QRect(13, 9, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_relay1max.setFont(font)
        self.lbl_relay1max.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_relay1max.setObjectName("lbl_relay1max")
        self.lbl_relay2max = QtWidgets.QLabel(self.frm_tempctrl)
        self.lbl_relay2max.setGeometry(QtCore.QRect(260, 10, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_relay2max.setFont(font)
        self.lbl_relay2max.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_relay2max.setObjectName("lbl_relay2max")
        self.lbl_relay2min = QtWidgets.QLabel(self.frm_tempctrl)
        self.lbl_relay2min.setGeometry(QtCore.QRect(260, 170, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_relay2min.setFont(font)
        self.lbl_relay2min.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_relay2min.setObjectName("lbl_relay2min")
        self.lbl_relay1min = QtWidgets.QLabel(self.frm_tempctrl)
        self.lbl_relay1min.setGeometry(QtCore.QRect(20, 170, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_relay1min.setFont(font)
        self.lbl_relay1min.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_relay1min.setObjectName("lbl_relay1min")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_temp1.setText(_translate("MainWindow", "Temp 1"))
        self.lbl_temp2.setText(_translate("MainWindow", "Temp 2"))
        self.lbl_temp3.setText(_translate("MainWindow", "Temp 3"))
        self.lbl_temp4.setText(_translate("MainWindow", "Temp 4"))
        self.lbl_temp5.setText(_translate("MainWindow", "Temp 5"))
        self.btn_relay1on.setText(_translate("MainWindow", "Relay 1\n"
"Activate"))
        self.btn_relay1off.setText(_translate("MainWindow", "Relay 1\n"
"Deactivate"))
        self.btn_relay2off.setText(_translate("MainWindow", "Relay 2\n"
"Deactivate"))
        self.btn_relay2on.setText(_translate("MainWindow", "Relay 2\n"
"Activate"))
        self.lbl_relay1max.setText(_translate("MainWindow", "Relay 1: MAX \n"
"(Temp1)"))
        self.lbl_relay2max.setText(_translate("MainWindow", "Relay 2: MAX \n"
"(Temp2+Temp3)"))
        self.lbl_relay2min.setText(_translate("MainWindow", "Relay 2: MIN \n"
"(Temp2+Temp3)"))
        self.lbl_relay1min.setText(_translate("MainWindow", "Relay 1: MIN \n"
"(Temp1)"))
