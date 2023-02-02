from PyQt5 import QtCore, QtGui, QtWidgets


class PasswordWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(568, 272)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Catagory = QtWidgets.QLabel(self.centralwidget)
        self.Catagory.setGeometry(QtCore.QRect(30, 30, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Catagory.setFont(font)
        self.Catagory.setObjectName("Catagory")
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setGeometry(QtCore.QRect(30, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.passwordLable = QtWidgets.QLabel(self.centralwidget)
        self.passwordLable.setGeometry(QtCore.QRect(30, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordLable.setFont(font)
        self.passwordLable.setObjectName("passwordLable")
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(150, 100, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.email.setFont(font)
        self.email.setObjectName("email")
        self.copy = QtWidgets.QPushButton(self.centralwidget)
        self.copy.setGeometry(QtCore.QRect(40, 200, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.copy.setFont(font)
        self.copy.setObjectName("copy")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(390, 200, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.togglePassword = QtWidgets.QPushButton(self.centralwidget)
        self.togglePassword.setGeometry(QtCore.QRect(220, 200, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.togglePassword.setFont(font)
        self.togglePassword.setObjectName("togglePassword")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(150, 150, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.passVisiable = False
        self.togglePassword.clicked.connect(self.togglePasswordVisi)
        self.copy.clicked.connect(self.copyPassword)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def togglePasswordVisi(self):
        if self.passVisiable:
            self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.passVisiable = False
        else:
            self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.passVisiable = True


    def copyPassword(self):
        self.copy.setText("Copied!")
        QtWidgets.QApplication.clipboard().setText(self.lineEdit.text())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password"))
        self.Catagory.setText(_translate("MainWindow", "Catagory:Home"))
        self.emailLabel.setText(_translate("MainWindow", "Email:"))
        self.passwordLable.setText(_translate("MainWindow", "Password"))
        self.email.setText(_translate("MainWindow", "Email:"))
        self.copy.setText(_translate("MainWindow", "Copy"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.togglePassword.setText(_translate("MainWindow", "Show Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PasswordWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
