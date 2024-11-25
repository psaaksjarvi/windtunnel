# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mazair3.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLCDNumber, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(716, 465)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 181, 61))
        font = QFont()
        font.setFamilies([u"Mandalore Condensed"])
        font.setPointSize(61)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 210, 131, 31))
        font1 = QFont()
        font1.setFamilies([u"Mandalore Condensed"])
        font1.setPointSize(20)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(310, 210, 121, 31))
        self.label_3.setFont(font1)
        self.stop_button = QPushButton(self.centralwidget)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setGeometry(QRect(350, 330, 161, 41))
        font2 = QFont()
        font2.setFamilies([u"Mandalore Condensed"])
        font2.setPointSize(15)
        self.stop_button.setFont(font2)
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(210, 10, 331, 61))
        self.listWidget.setFrameShadow(QFrame.Raised)
        self.listWidget.setLineWidth(5)
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(170, 330, 161, 41))
        self.start_button.setFont(font2)
        self.velocityLCD = QLCDNumber(self.centralwidget)
        self.velocityLCD.setObjectName(u"velocityLCD")
        self.velocityLCD.setGeometry(QRect(20, 120, 171, 81))
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(True)
        self.velocityLCD.setFont(font3)
        self.velocityLCD.setLineWidth(5)
        self.velocityLCD.setSmallDecimalPoint(False)
        self.velocityLCD.setDigitCount(5)
        self.velocityLCD.setSegmentStyle(QLCDNumber.Filled)
        self.massLCD = QLCDNumber(self.centralwidget)
        self.massLCD.setObjectName(u"massLCD")
        self.massLCD.setGeometry(QRect(260, 120, 181, 81))
        font4 = QFont()
        font4.setBold(True)
        self.massLCD.setFont(font4)
        self.massLCD.setLineWidth(5)
        self.massLCD.setSmallDecimalPoint(False)
        self.massLCD.setDigitCount(5)
        self.dragLCD = QLCDNumber(self.centralwidget)
        self.dragLCD.setObjectName(u"dragLCD")
        self.dragLCD.setGeometry(QRect(510, 120, 181, 81))
        self.dragLCD.setFont(font4)
        self.dragLCD.setLineWidth(5)
        self.dragLCD.setSmallDecimalPoint(False)
        self.dragLCD.setDigitCount(5)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(560, 210, 141, 31))
        self.label_4.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 716, 17))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MAZAIR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MAZAIR", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Velocity: m / s", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Mass: grams", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Drag", None))
    # retranslateUi

