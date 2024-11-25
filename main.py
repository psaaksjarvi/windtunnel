import time

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QIODevice
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import serial
import pandas as pd
import serial
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtUiTools import QUiLoader
from ui_mazair import Ui_MainWindow
from datetime import datetime
import serial.tools.list_ports

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.ui = Ui_MainWindow()
        print("MyWindow")
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.text = ""
        self.data = []
        self.mass = []
        self.drag = 0
        self.down_force = 0
        self.velocity = [0]
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.restart)
        self.change_in_speed = []
        self.plot_timer = QtCore.QTimer(self)
        self.plot_timer.timeout.connect(self.read_serial_data)
        self.plot_timer.start(10)
        self.students = []
        self.columns = ["Date", "FirstName", "LastName", "TeamName", "House", "CrossSectionalArea", "MinDrag", "MaxDrag", "MinDownForce", "MaxDownForce"]
        self.fields_filled_in = False
        self.ready_to_read = True
        self.air_density = 1.225
        self.drag_coefficient = 0.35
        self.arduino_ports = []

    def calc_down_force(self):
        return sum(mass)
    
    def restart(self):
        self.ser.close()
        self.listWidget.clear()
        self.listWidget.addItem("Stopped")
#         self.listWidget.addItem("Bitrate\t\t{}bps".format(self.ser.baudrate))


#     def save_user(self):
#         self.plot_timer.stop()
#         self.s1 = Student(datetime.now(), self.name_line_edit.text(), self.surname_line_edit.text(), self.team_line_edit.text(), self.house_combo.currentText(), self.cross_sect_line_edit.text(), 12, 2, 222, 900)        # self.students.append(self.name_line_edit.text())
#         self.s1.save_results
#         with open("/home/peter/Desktop/WindTunnelStats.csv","a") as f:
#             writer = csv.writer(f,delimiter=",")
#             writer.writerow(self.s1.save_results())
#         self.data = []
#         self.mass = 0
#         self.down_force = 0
#         self.velocity = [0]
    def find_arduino_port(self):
        self.arduino_ports = [
            p.device
            for p in serial.tools.list_ports.comports()
            if 'COM' in p.description
        ]
        print(self.arduino_ports)
        if not self.arduino_ports:
            self.listWidget.clear()
            self.listWidget.addItem("No Arduino found. Make sure it's connected.")
            raise IOError("No Arduino found. Make sure it's connected.")
        return self.arduino_ports[0]

    def start(self):
        self.arduino_port = self.find_arduino_port()
        print(f"Connecting to Arduino on port: {self.arduino_port}")
        #self.ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=0.4)
        self.ser = serial.Serial(port=self.arduino_port, baudrate=115200, timeout=0.4)
        self.listWidget.clear()
        self.listWidget.addItem("Connected to\t{}".format(self.ser.port))
        self.listWidget.addItem("Bitrate\t\t{}bps".format(self.ser.baudrate))
        time.sleep(2)
        if self.ser.readable():
            self.read_serial_data()
        else:
            self.listWidget.clear()
            self.listWidget.addItem("No connection..\nCheck Arduino Connections")


    def read_serial_data(self):
        try:
            self.text = self.ser.read_until(b'\r\n')
            self.data = (self.text.decode('utf-8').rstrip())
            print(self.data)
            if "Mass: " in self.data:
                if (self.data[5] == '-'):
                    self.data = self.data[6:]
                else:
                    grams = float(self.data[6:])
                    grams = grams * 100
                    self.massLCD.display(grams)
                    self.mass.append(self.data[6:])
                    self.write_data_to_file((self.data[6:])*100)
            if "Velocity: " in self.data:
                speed = float(self.data[10:])
                speed = int(speed)
                self.velocityLCD.display(speed)
                self.velocity.append(self.data)
                self.write_data_to_file(float(self.data[9:]))
            if "Drag: " in self.data:
                self.drag = float(self.data[6:])
                self.dragLCD.display(self.drag)
                print(self.drag)
        except:
            pass


#     def write_data_to_file(self, data_to_write):
#             # CHECK THE FIRST READING WHETHER MASS oR VELOCITY
#         with open('/home/peter/Desktop/dragster_2021.csv', 'a') as f:
#             writer2 = csv.writer(f, delimiter=',')
#             if len(str(data_to_write)) < 5:
#                 writer2.writerow(['', '', '', '', data_to_write, ''])
#             else:
#                 writer2.writerow(['', '', '', '', '', data_to_write])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
