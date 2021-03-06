# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bot_voice.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

voice = [0]


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(240, 182)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 241, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/jarvis/Jarvis/utils/images/bot.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.radioButton_male = QtWidgets.QRadioButton(Form)
        self.radioButton_male.setGeometry(QtCore.QRect(10, 120, 51, 41))
        self.radioButton_male.setObjectName("radioButton_male")
        self.radioButton_male.toggled.connect(self.maleselected)

        self.radioButton_female = QtWidgets.QRadioButton(Form)
        self.radioButton_female.setGeometry(QtCore.QRect(10, 30, 51, 21))
        self.radioButton_female.setObjectName("radioButton_female")
        self.radioButton_female.toggled.connect(self.femaleselected)

        self.movie = QtGui.QMovie("D:/jarvis/Jarvis/utils/images/bot.gif")
        self.label.setMovie(self.movie)
        self.startAnimation()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def startAnimation(self):
        self.movie.start()

    def maleselected(self, selected):
        if selected:
            voice[0] = 0
            file = open("somefile.txt", "w")
            file.write("0")
            print("You selected male")

    def femaleselected(self, selected):
        if selected:
            f = open("somefile.txt", 'r+')
            f.seek(0)
            f.write("1")
            print("You selected female")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Voice"))
        self.radioButton_male.setText(_translate("Form", "Male"))
        self.radioButton_female.setText(_translate("Form", "Female"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())