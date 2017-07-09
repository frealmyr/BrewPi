#pylint: disable=E0401,R0903,C0103,C0301,E1101,C0325,C0111,E0611
import sys
import time
import datetime as dt
import csv
import os
import RPi.GPIO as GPIO
from collections import namedtuple #For getting remaining free storage
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
import numpy as np
import design

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT)

### Temp sensor QThreads ###
class Get_temp01(QThread):
    """Gets temp from temp sensor 1 if it is enabled"""
    mySignal = QtCore.pyqtSignal(float) #Signal that connects to main code

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        while True:
            try: #Try-ex for pulling sensor data
                tempfile = open("/sys/bus/w1/devices/28-031655b507ff/w1_slave") #Reading sensor values
                thetext = tempfile.read() #Storing sensor values in tempfile
                tempfile.close() #Closing the tempfile
                tempdata = thetext.split("\n")[1].split(" ")[9] #Trims the float-value
                temp1_read = float(tempdata[2:]) #Trims the float-value
                temp1_read = temp1_read / 1000 #Trims the float-value
                self.mySignal.emit(temp1_read) #Sends the trimmed float-value to signal
                self.write_templog(temp1_read)
                time.sleep(5) #Sleeps x seconds before re-doing loop
            except: #Catch ex where sensor is unaviable
                print("Error getting value from tempsensor_01")

    def write_templog(self, floatvalue):
        """Writes a newline in the seperate temp1log file with float value and timestamp"""
        now = dt.datetime.now() #Refreshing time
        print("Temp read and emitted")
        with open('temp01log.csv', "a", newline='') as csvfile: #Logging temp
            temp01writer = csv.writer(csvfile, delimiter=',') #Opening file
            temp01writer.writerow(["%.2f" % floatvalue]+[now.strftime("%H:%M %d-%m-%Y")]) #Adding row
        print("Log written")

class Get_temp02(QThread):
    """Gets temp from temp sensor 2 if it is enabled"""
    mySignal = QtCore.pyqtSignal(float) #Signal that connects to main code

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        while True:
            try: #Try-ex for pulling sensor data
                tempfile = open("/sys/bus/w1/devices/28-031655b73dff/w1_slave") #Reading sensor values
                thetext = tempfile.read() #Storing sensor values in tempfile
                tempfile.close() #Closing the tempfile
                tempdata = thetext.split("\n")[1].split(" ")[9] #Trims the float-value
                temp2_read = float(tempdata[2:]) #Trims the float-value
                temp2_read = temp2_read / 1000 #Trims the float-value
                self.mySignal.emit(temp2_read) #Sends the trimmed float-value to signal
                self.write_templog(temp2_read)
                time.sleep(5) #Sleeps x seconds before re-doing loop
            except: #Catch ex where sensor is unaviable
                print("Error getting value from tempsensor_02")

    def write_templog(self, floatvalue):
        now = dt.datetime.now() #Refreshing time
        print("Temp read and emitted")
        with open('temp01log.csv', "a", newline='') as csvfile: #Logging temp
            temp01writer = csv.writer(csvfile, delimiter=',') #Opening file
            temp01writer.writerow(["%.2f" % floatvalue]+[now.strftime("%H:%M %d-%m-%Y")]) #Adding row
        print("Log written")

class Get_temp03(QThread):
    """Gets temp from temp sensor 3 if it is enabled"""
    mySignal = QtCore.pyqtSignal(float) #Signal that connects to main code

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        while True:
            try: #Try-ex for pulling sensor data
                tempfile = open("/sys/bus/w1/devices/28-031655d92dff/w1_slave") #Reading sensor values
                thetext = tempfile.read() #Storing sensor values in tempfile
                tempfile.close() #Closing the tempfile
                tempdata = thetext.split("\n")[1].split(" ")[9] #Trims the float-value
                temp3_read = float(tempdata[2:]) #Trims the float-value
                temp3_read = temp3_read / 1000 #Trims the float-value
                self.mySignal.emit(temp3_read) #Sends the trimmed float-value to signal
                self.write_templog(temp3_read)
                time.sleep(5) #Sleeps x seconds before re-doing loop
            except: #Catch ex where sensor is unaviable
                print("Error getting value from tempsensor_03")

    def write_templog(self, floatvalue):
        now = dt.datetime.now() #Refreshing time
        print("Temp read and emitted")
        with open('temp01log.csv', "a", newline='') as csvfile: #Logging temp
            temp01writer = csv.writer(csvfile, delimiter=',') #Opening file
            temp01writer.writerow(["%.2f" % floatvalue]+[now.strftime("%H:%M %d-%m-%Y")]) #Adding row
        print("Log written")

class Get_temp04(QThread):
    """Gets temp from temp sensor 4 if it is enabled"""
    mySignal = QtCore.pyqtSignal(float) #Signal that connects to main code

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        while True:
            try: #Try-ex for pulling sensor data
                tempfile = open("/sys/bus/w1/devices/28-041658b39fff/w1_slave") #Reading sensor values
                thetext = tempfile.read() #Storing sensor values in tempfile
                tempfile.close() #Closing the tempfile
                tempdata = thetext.split("\n")[1].split(" ")[9] #Trims the float-value
                temp4_read = float(tempdata[2:]) #Trims the float-value
                temp4_read = temp4_read / 1000 #Trims the float-value
                self.mySignal.emit(temp4_read) #Sends the trimmed float-value to signal
                self.write_templog(temp4_read)
                time.sleep(5) #Sleeps x seconds before re-doing loop
            except: #Catch ex where sensor is unaviable
                print("Error getting value from tempsensor_04")

    def write_templog(self, floatvalue):
        now = dt.datetime.now() #Refreshing time
        print("Temp read and emitted")
        with open('temp01log.csv', "a", newline='') as csvfile: #Logging temp
            temp01writer = csv.writer(csvfile, delimiter=',') #Opening file
            temp01writer.writerow(["%.2f" % floatvalue]+[now.strftime("%H:%M %d-%m-%Y")]) #Adding row
        print("Log written")

class Get_temp05(QThread):
    """Gets temp from temp sensor 5 if it is enabled"""
    mySignal = QtCore.pyqtSignal(float) #Signal that connects to main code

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        while True:
            try: #Try-ex for pulling sensor data
                tempfile = open("/sys/bus/w1/devices/28-041658efc1ff/w1_slave") #Reading sensor values
                thetext = tempfile.read() #Storing sensor values in tempfile
                tempfile.close() #Closing the tempfile
                tempdata = thetext.split("\n")[1].split(" ")[9] #Trims the float-value
                temp5_read = float(tempdata[2:]) #Trims the float-value
                temp5_read = temp5_read / 1000 #Trims the float-value
                self.mySignal.emit(temp5_read) #Sends the trimmed float-value to signal
                self.write_templog(temp5_read)
                time.sleep(5) #Sleeps x seconds before re-doing loop
            except: #Catch ex where sensor is unaviable
                print("Error getting value from tempsensor_05")

    def write_templog(self, floatvalue):
        now = dt.datetime.now() #Refreshing time
        print("Temp read and emitted")
        with open('temp01log.csv', "a", newline='') as csvfile: #Logging temp
            temp01writer = csv.writer(csvfile, delimiter=',') #Opening file
            temp01writer.writerow(["%.2f" % floatvalue]+[now.strftime("%H:%M %d-%m-%Y")]) #Adding row
        print("Log written")

class Relay_Logic(QThread):
    """Logic that is used for automatic relay control"""
    relay02_setmaxtemp = 25.50
    relay02_setmintemp = 18.50

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        self.relay01_logic()

    def relay01_deactivate(self):
        #GPIO.output(20,GPIO.LOW)
        self.btn_relay01off.setEnabled(False)
        self.btn_relay01on.setEnabled(True)
        print ("Relay 1 off!")

    def relay02_activate(self):
        #GPIO.output(20,GPIO.HIGH)
        self.btn_relay02off.setEnabled(True)
        self.btn_relay02on.setEnabled(False)
        print ("Relay 2 on!")

    def relay02_deactivate(self):
        #GPIO.output(20,GPIO.LOW)
        self.btn_relay02off.setEnabled(False)
        self.btn_relay02on.setEnabled(True)
        print ("Relay 2 off!")

### Main GUI Window ###
class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    """Contains all GUI items, also handles interactions"""
    ### Global variables that needs to be at the start of class due to insertion from QThread workers. ###
    # Active/Inactive flags for relays
    relay01_active = False
    relay02_active = False
    # Relay temp_parameters
    relay01_maxtemp = 20.00
    relay01_mintemp = 15.00
    relay02_maxtemp = 20.00
    relay02_mintemp = 15.00
    # Misc GUI
    current_freestorage = namedtuple('usage', 'total used free')

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.relay01_parameter_read()
        self.free_space()

        #Change current widget in QStackedWidget
        self.nav_btn_automation.clicked.connect(lambda: self.child_navigator.setCurrentIndex(0))
        self.nav_btn_automation.clicked.connect(lambda: self.relay01_parameter_read())
        #self.nav_btn_logging.clicked.connect(lambda: self.child_navigator.setCurrentIndex(1))
        #self.nav_btn_logging.clicked.connect(lambda: self.addmpl())
        self.nav_btn_configuration.clicked.connect(lambda: self.child_navigator.setCurrentIndex(2))

        #Code for handling button presses in GUI.
        self.cfg_btn_relay01_on.clicked.connect(lambda: self.relay01_control(True))
        self.cfg_btn_relay01_off.clicked.connect(lambda: self.relay01_control(False))
        self.cfg_btn_relay02_on.clicked.connect(lambda: self.relay02_activate())
        self.cfg_btn_relay02_off.clicked.connect(lambda: self.relay02_deactivate())
        self.relay01_btn_writeparameters.clicked.connect(lambda: self.relay01_parameter_write())
        self.relay01_btn_writeparameters.clicked.connect(lambda: self.parameter_changed(1, False))
        self.relay02_btn_writeparameters.clicked.connect(lambda: self.parameter_changed(2, False))
        self.cfg_btn_restartapp.clicked.connect(self.close)

        #Misc GUI tweaks for valueChanged/buttonpressed
        self.relay01_sbox_maxtemp.valueChanged.connect(lambda: self.parameter_changed(1, True))
        self.relay01_sbox_mintemp.valueChanged.connect(lambda: self.parameter_changed(1, True))
        self.relay01_cbox_sensors.currentIndexChanged.connect(lambda: self.parameter_changed(1, True))

    ### QThread Management ###
        # QThread: Temp Sensor 01
        self.TempReader1 = Get_temp01()
        self.TempReader1.start()
        self.TempReader1.mySignal.connect(self.relay01_logic)
        self.TempReader1.mySignal.connect(self.disp_lcd_temp01.display)
        # QThread: Temp Sensor 02
        self.TempReader2 = Get_temp02()
        self.TempReader2.start()
        self.TempReader2.mySignal.connect(self.disp_lcd_temp02.display)
        # QThread: Temp Sensor 03
        self.TempReader3 = Get_temp03()
        self.TempReader3.start()
        self.TempReader3.mySignal.connect(self.disp_lcd_temp03.display)
        # QThread: Temp Sensor 04
        self.TempReader4 = Get_temp04()
        self.TempReader4.start()
        self.TempReader4.mySignal.connect(self.disp_lcd_temp04.display)
        # QThread: Temp Sensor 05
        self.TempReader5 = Get_temp05()
        self.TempReader5.start()
        self.TempReader5.mySignal.connect(self.disp_lcd_temp05.display)

    ### Relay Logic & Control ###
    def relay01_logic(self, testfloat):
        """Logic for automated temperature based relay control"""
        if testfloat <= self.relay01_mintemp: #Variable outside funtion so that it doesn't get reset on initalization.
            if self.relay01_active is False: #If-statement for limiting relay_control to one command.
                #Temp. under min-temp, activating relay 01
                print (self.relay01_mintemp)
                self.relay01_active = True
                self.relay01_control(True)
        if testfloat >= self.relay01_maxtemp:
            if self.relay01_active is True:
                #Temp over max-temp, deactivating relay 01
                self.relay01_active = False
                self.relay01_control(False)

    def relay01_control(self, status):
        """Boolean based function for powering on/off the GPIO port to the solid state relay"""
        if status is True: #Enables the relay
            GPIO.output(5, GPIO.HIGH) #Activating power on GPIO 5
            self.cfg_btn_relay01_on.setStyleSheet("background-color: #919E83; color: #B3B3B3")
            self.cfg_btn_relay01_off.setEnabled(True)
            self.cfg_btn_relay01_on.setEnabled(False)
            self.cfg_btn_relay01_off.setStyleSheet("background-color: #ED6464; color: white")
            self.sendtolog("Relay 01 - Activated @", self.relay01_mintemp)
        if status is False: #Disables the relay
            GPIO.output(5, GPIO.LOW) #Disabling power on GPIO 5
            self.cfg_btn_relay01_on.setStyleSheet("background-color: none")
            self.cfg_btn_relay01_off.setEnabled(False)
            self.cfg_btn_relay01_on.setEnabled(True)
            self.cfg_btn_relay01_off.setStyleSheet("background-color: none")
            self.sendtolog("Relay 01 - Deactivated @", self.relay01_maxtemp)

    ### Parameter Read/Write ###
    def relay01_parameter_read(self):
        """Pulls parameters for relay01 logic from a seperate local file"""
        f = open('relay01config', 'rt')
        lines = f.read().splitlines()
        #Finds index of stored temp sensor, reverts to first index if not found.
        findtempvalue = self.relay01_cbox_sensors.findText(lines[0], QtCore.Qt.MatchFixedString)
        if findtempvalue >= 0:
            self.relay01_cbox_sensors.setCurrentIndex(findtempvalue)
        else:
            #If the stored sensor is not found, revert to first index.
            self.relay01_cbox_sensors.setCurrentIndex(1)
            self.sendtolog("--ERROR: NO SENSORS FOUND", 404)
        self.relay01_sbox_maxtemp.setValue(float(lines[1])) # Writing to maxtemp scrollbox
        self.relay01_maxtemp = (float(lines[1])) # Writing to maxtemp global variable
        self.sendtolog("Relay 01 - Max Temp: ", self.relay01_maxtemp)
        self.relay01_sbox_mintemp.setValue(float(lines[2])) # Writing to mintemp scrollbox
        self.relay01_mintemp = (float(lines[2])) # Writing to mintemp global variable
        self.sendtolog("Relay 01 - Min Temp: ", self.relay01_mintemp) # Sending mintemp to log
        f.close() # Closing the reader

    def relay01_parameter_write(self):
        """Stores parameters for relay01 logic to a seperate local file"""
        open('relay01config', 'w').close() #Removing existing paramters from file
        with open('relay01config', 'a') as f: #Writing new parameters to file
            f.write(str(self.relay01_cbox_sensors.currentText()) + "\n")
            print(self.relay01_cbox_sensors.currentText())
            f.write(str(self.relay01_sbox_maxtemp.value()) + "\n")
            f.write(str(self.relay01_sbox_mintemp.value()))
        f.close()

    def available_sensors_read(self): ### !!! Connect this one to combobox focus
        """Function that pulls the list of online sensors"""
        file_in_use = True
        with open('availablesensors', 'rt') as f:
            lines = f.read().splitlines() 
        f.close()
        self.relay01_cbox_sensors.clear()
        self.relay01_cbox_sensors.addItems(lines)
        file_in_use = False

    ### Configuration Options ###
    def available_sensors_scan(self):
        """Function that scans for online i2c sensors"""
        file_in_use = True
        #Reading available sensors from file
        with open('availablesensors', 'rt') as f:
            lines = f.read().splitlines() 
        f.close()
        self.sendtolog("Scanned for sensors, found the following: ", lines)

    ### Misc GUI logic ###
    def parameter_changed(self, relay, status):
        """Enables GUI button when spinbox is changed from stored value"""
        if status is True:
            if relay is 1:
                self.relay01_btn_writeparameters.setStyleSheet("background-color: #ED6464; color: white")
            if relay is 2:
                self.relay02_btn_writeparameters.setStyleSheet("background-color: #ED6464; color: white")
        if status is False:
            if relay is 1:
                self.relay01_btn_writeparameters.setStyleSheet("background-color: none")
            if relay is 2:
                self.relay02_btn_writeparameters.setStyleSheet("background-color: none")

    def free_space(self):
        """Function that pulls the remaning storage capacity of the local device"""
        st = os.statvfs('/')
        free = (st.f_bavail * st.f_frsize) / 1000
        total = (st.f_blocks * st.f_frsize) / 1000
        self.cfg_progressbar_storage.setRange(0, total)
        self.cfg_progressbar_storage.setValue(free)

    def sendtolog(self, loginfo, logdata):
        """Function that sends a message to the listbox logviewer"""
        if self.cfg_listbox_logoutput.count() < 17:
            self.cfg_listbox_logoutput.addItem(dt.datetime.now().strftime("%d/%m-%H:%M: ") + loginfo + str(logdata))
        else:
            self.cfg_listbox_logoutput.takeItem(0)
            self.cfg_listbox_logoutput.addItem(dt.datetime.now().strftime("%d/%m-%H:%M: ") + loginfo + str(logdata))

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()
    form.setWindowState(QtCore.Qt.WindowMaximized)
    form.showMaximized()
    app.exec_()

if __name__ == '__main__':
    main()