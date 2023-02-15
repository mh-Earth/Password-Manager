from PyQt5 import QtCore, QtGui, QtWidgets


class AddAccountWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 408)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.GridLayout = QtWidgets.QGridLayout()
        self.GridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.GridLayout.setHorizontalSpacing(0)
        self.GridLayout.setVerticalSpacing(30)
        self.GridLayout.setObjectName("GridLayout")
        self.TaglineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TaglineEdit.setFont(font)
        self.TaglineEdit.setObjectName("TaglineEdit")
        self.GridLayout.addWidget(self.TaglineEdit, 1, 2, 1, 1)
        self.EmaillineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EmaillineEdit.setFont(font)
        self.EmaillineEdit.setObjectName("EmaillineEdit")
        self.GridLayout.addWidget(self.EmaillineEdit, 3, 1, 1, 2)
        self.Passwordlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Passwordlabel.setFont(font)
        self.Passwordlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Passwordlabel.setObjectName("Passwordlabel")
        self.GridLayout.addWidget(self.Passwordlabel, 4, 0, 1, 1)
        self.Taglabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Taglabel.setFont(font)
        self.Taglabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Taglabel.setObjectName("Taglabel")
        self.GridLayout.addWidget(self.Taglabel, 1, 0, 1, 1)
        self.PasswordlineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PasswordlineEdit_3.setFont(font)
        self.PasswordlineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordlineEdit_3.setObjectName("PasswordlineEdit_3")
        self.GridLayout.addWidget(self.PasswordlineEdit_3, 4, 1, 1, 2)
        self.AddAcclabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddAcclabel.sizePolicy().hasHeightForWidth())
        self.AddAcclabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.AddAcclabel.setFont(font)
        self.AddAcclabel.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.AddAcclabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AddAcclabel.setObjectName("AddAcclabel")
        self.GridLayout.addWidget(self.AddAcclabel, 0, 0, 1, 4)
        self.URLlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.URLlabel.setFont(font)
        self.URLlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.URLlabel.setObjectName("URLlabel")
        self.GridLayout.addWidget(self.URLlabel, 5, 0, 1, 1)
        self.Emaillabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Emaillabel.setFont(font)
        self.Emaillabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Emaillabel.setObjectName("Emaillabel")
        self.GridLayout.addWidget(self.Emaillabel, 3, 0, 1, 1)
        self.URLlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.URLlineEdit.setFont(font)
        self.URLlineEdit.setObjectName("URLlineEdit")
        self.GridLayout.addWidget(self.URLlineEdit, 5, 2, 1, 1)
        self.horizontalLayoutGridLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayoutGridLayout.setObjectName("horizontalLayoutGridLayout")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayoutGridLayout.addWidget(self.checkBox)
        self.GenerateButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GenerateButton.setFont(font)
        self.GenerateButton.setObjectName("GenerateButton")
        self.horizontalLayoutGridLayout.addWidget(self.GenerateButton)
        self.GridLayout.addLayout(self.horizontalLayoutGridLayout, 4, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../project wasly/Icons/plus-16.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddButton.setIcon(icon)
        self.AddButton.setObjectName("AddButton")
        self.horizontalLayout.addWidget(self.AddButton)
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setObjectName("ExitButton")
        self.horizontalLayout.addWidget(self.ExitButton)
        self.GridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 4)
        self.UsernamelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.UsernamelineEdit.setFont(font)
        self.UsernamelineEdit.setObjectName("lineEdit")
        self.GridLayout.addWidget(self.UsernamelineEdit, 2, 1, 1, 2)
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameLabel.setObjectName("label")
        self.GridLayout.addWidget(self.usernameLabel, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.GridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        #  Add manually
        # binding button events 
        self.GenerateButton.clicked.connect(self.genPassword)
        self.checkBox.clicked.connect(self.togglePassword)
        # Global Status
        self.isLoggedIn = True

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    # Buttons -> exit
    def exit(self):
        QtWidgets.qApp.quit()
    
    # Buttons -> Generate
    def genPassword(self):
        import string,random

        apl = string.ascii_letters + string.digits + string.digits
        aplList = []
        aplList.extend(apl)
        random.shuffle(aplList)

        genPassWord = "".join(aplList[:16])
        self.PasswordlineEdit_3.setText(genPassWord)


    # checkBox -> showpassword
    def togglePassword(self):
        if self.checkBox.isChecked():
            self.PasswordlineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.PasswordlineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Password"))
        self.Passwordlabel.setText(_translate("MainWindow", "Password"))
        self.Taglabel.setText(_translate("MainWindow", "Tag/Label"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.Emaillabel.setText(_translate("MainWindow", "Email"))
        self.URLlabel.setText(_translate("MainWindow", "URL"))
        self.AddAcclabel.setText(_translate("MainWindow", "Add Password"))
        self.checkBox.setText(_translate("MainWindow", "Show"))
        self.GenerateButton.setText(_translate("MainWindow", "Generate"))
        self.AddButton.setText(_translate("MainWindow", "Add"))
        self.ExitButton.setText(_translate("MainWindow", "Cancel"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AddAccountWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
