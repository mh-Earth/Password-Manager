# The file is not used in the project, it is just for reference
# Don't delete this file
# Read only

from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser

class PasswordWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 284)
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
        self.passwordLable.setGeometry(QtCore.QRect(30, 140, 91, 31))
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
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(150, 140, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 230, 521, 44))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.togglePassword = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.togglePassword.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.togglePassword.setFont(font)
        self.togglePassword.setObjectName("togglePassword")
        self.horizontalLayout.addWidget(self.togglePassword)
        self.copy = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.copy.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.copy.setFont(font)
        self.copy.setObjectName("copy")
        self.horizontalLayout.addWidget(self.copy)
        self.openIn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.openIn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.openIn.setFont(font)
        self.openIn.setObjectName("openIn")
        self.horizontalLayout.addWidget(self.openIn)
        self.back = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.back.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.horizontalLayout.addWidget(self.back)
        self.UrlLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.UrlLabel_2.setGeometry(QtCore.QRect(30, 181, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.UrlLabel_2.setFont(font)
        self.UrlLabel_2.setObjectName("UrlLabel_2")
        self.Url = QtWidgets.QLabel(self.centralwidget)
        self.Url.setGeometry(QtCore.QRect(150, 181, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Url.setFont(font)
        self.Url.setObjectName("Url")
        MainWindow.setCentralWidget(self.centralwidget)
        # Add manually
        self.passVisiable = False
        self.togglePassword.clicked.connect(self.togglePasswordVisi)
        self.copy.clicked.connect(self.copyPassword)
        self.openIn.clicked.connect(self.openUrl)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def togglePasswordVisi(self):
        if self.passVisiable:
            self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.togglePassword.setText('Show Password')
            self.passVisiable = False
        else:
            self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.togglePassword.setText('Hide Password')
            self.passVisiable = True


    def copyPassword(self):
        self.copy.setText("Copied!")
        QtWidgets.QApplication.clipboard().setText(self.lineEdit.text())
    
    def openUrl(self):
        if self.Url.text().startswith(("https://","http://")):

            webbrowser.open(url=self.Url.text())
        else:
            webbrowser.open(url=f"http://{self.Url.text()}")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password"))
        self.Catagory.setText(_translate("MainWindow", "Catagory:Home"))
        self.emailLabel.setText(_translate("MainWindow", "Email:"))
        self.passwordLable.setText(_translate("MainWindow", "Password"))
        self.email.setText(_translate("MainWindow", "Email:"))
        self.togglePassword.setText(_translate("MainWindow", "Show Password"))
        self.copy.setText(_translate("MainWindow", "Copy"))
        self.openIn.setText(_translate("MainWindow", "Open Url"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.UrlLabel_2.setText(_translate("MainWindow", "URL:"))
        self.Url.setText(_translate("MainWindow", "https://www.google.com"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PasswordWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
