# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OurGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess as sp
import cv2 as cv
import pandas as pd
from datetime import datetime
from datetime import date
import face_recognition
import os
from csv import DictWriter
from getpass import getpass
from cvzone.PoseModule import PoseDetector
class Ui_MyInterface(object):
    def setupUi(self, MyInterface):
        MyInterface.setObjectName("MyInterface")
        MyInterface.resize(639, 572)

        self.VideoStreamer = QtWidgets.QPushButton(MyInterface)
        self.VideoStreamer.setGeometry(QtCore.QRect(70, 280, 111, 25))
        self.VideoStreamer.setObjectName("VideoStreamer")
        self.VideoStreamer.clicked.connect(self.myvideo)

        self.DataBase = QtWidgets.QPushButton(MyInterface)
        self.DataBase.setGeometry(QtCore.QRect(470, 280, 89, 25))
        self.DataBase.setObjectName("DataBase")
        self.DataBase.clicked.connect(self.openMyFile)

        

        self.retranslateUi(MyInterface)
        QtCore.QMetaObject.connectSlotsByName(MyInterface)

    def myvideo(self):
        cmd=["python3","newtest.py"]
        sp.Popen(cmd)
    
    def openMyFile(self):
         YourCSV=["python3","csvOpener.py"]
         sp.Popen(YourCSV)


    def retranslateUi(self, MyInterface):
        _translate = QtCore.QCoreApplication.translate
        MyInterface.setWindowTitle(_translate("MyInterface", "Dialog"))
        self.VideoStreamer.setText(_translate("MyInterface", "Video Streamer"))
        self.DataBase.setText(_translate("MyInterface", "Data Base"))
      


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyInterface = QtWidgets.QDialog()
    ui = Ui_MyInterface()
    ui.setupUi(MyInterface)
    MyInterface.show()
    sys.exit(app.exec_())

