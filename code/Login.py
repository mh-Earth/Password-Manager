from PyQt5 import QtCore, QtGui, QtWidgets


class AuthWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(320, 316)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(30)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Loginlabel_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.Loginlabel_3.setFont(font)
        self.Loginlabel_3.setStyleSheet("#funcWidget QLineEdite{\n"
"    border-raduis: 5px;\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#funcWidget QLineEdit:focuse{\n"
"    border-color:#5500ff;\n"
"}")
        self.Loginlabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Loginlabel_3.setObjectName("Loginlabel_3")
        self.verticalLayout_4.addWidget(self.Loginlabel_3)
        self.MasterPasswordlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.MasterPasswordlabel.setFont(font)
        self.MasterPasswordlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MasterPasswordlabel.setObjectName("MasterPasswordlabel")
        self.verticalLayout_4.addWidget(self.MasterPasswordlabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setMinimumSize(QtCore.QSize(300, 35))
        self.passwordLineEdit.setText("")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.verticalLayout_4.addWidget(self.passwordLineEdit)
        self.ShowPasswordButton = QtWidgets.QPushButton(self.centralwidget)
        self.ShowPasswordButton.setStyleSheet("image: url(:/icon/Icons/visible-16.ico);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Important stuff/QT_Designer/Icons/visible-16.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ShowPasswordButton.setIcon(icon)
        self.ShowPasswordButton.setObjectName("ShowPasswordButton")
        self.verticalLayout_4.addWidget(self.ShowPasswordButton)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.Exitlabel_3 = QtWidgets.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/Icons/x-mark-16.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exitlabel_3.setIcon(icon1)
        self.Exitlabel_3.setObjectName("Exitlabel_3")

        self.Createlabel_3 = QtWidgets.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/Icons/plus-16.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Createlabel_3.setIcon(icon2)
        self.Createlabel_3.setObjectName("Createlabel_3")

        self.horizontalLayout_3.addWidget(self.Createlabel_3)
        self.horizontalLayout_3.addWidget(self.Exitlabel_3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        # Add manually
        self.passwordVisibility = True
        self.ShowPasswordButton.clicked.connect(self.togglePasswordVisibility)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def togglePasswordVisibility(self):
        if self.passwordVisibility:
            self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ShowPasswordButton.setText("Hide Password")
            self.passwordVisibility = False

        else:
            self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ShowPasswordButton.setText("Show Password")
            self.passwordVisibility = True
    
    # TODO
    # Buttons -> login
    def login(self):
        print("Login")
        pass

    # Buttons -> exit
    def exit(self):
        QtWidgets.qApp.quit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Catagory Login"))
        self.Loginlabel_3.setText(_translate("MainWindow", "Login"))
        self.MasterPasswordlabel.setText(_translate("MainWindow", "Master Password"))
        self.ShowPasswordButton.setText(_translate("MainWindow", "Show Password"))
        self.Exitlabel_3.setText(_translate("MainWindow", "Exit"))
        self.Createlabel_3.setText(_translate("MainWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AuthWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
