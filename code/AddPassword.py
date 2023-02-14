from PyQt5 import QtCore, QtGui, QtWidgets


class AddPasswordWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.setFixedSize(618, 459)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(600, 400))
        self.widget.setMaximumSize(QtCore.QSize(600, 400))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.TaglineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TaglineEdit.setFont(font)
        self.TaglineEdit.setObjectName("TaglineEdit")
        self.gridLayout.addWidget(self.TaglineEdit, 1, 2, 1, 1)
        self.EmaillineEdit_2 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EmaillineEdit_2.setFont(font)
        self.EmaillineEdit_2.setObjectName("EmaillineEdit_2")
        self.gridLayout.addWidget(self.EmaillineEdit_2, 2, 1, 1, 2)
        self.Passwordlabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Passwordlabel.setFont(font)
        self.Passwordlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Passwordlabel.setObjectName("Passwordlabel")
        self.gridLayout.addWidget(self.Passwordlabel, 3, 0, 1, 1)
        self.Taglabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Taglabel.setFont(font)
        self.Taglabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Taglabel.setObjectName("Taglabel")
        self.gridLayout.addWidget(self.Taglabel, 1, 0, 1, 1)
        self.Emaillabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Emaillabel.setFont(font)
        self.Emaillabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Emaillabel.setObjectName("Emaillabel")
        self.gridLayout.addWidget(self.Emaillabel, 2, 0, 1, 1)
        self.URLlabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.URLlabel.setFont(font)
        self.URLlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.URLlabel.setObjectName("URLlabel")
        self.gridLayout.addWidget(self.URLlabel, 4, 0, 1, 1)
        self.URLlineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.URLlineEdit.setFont(font)
        self.URLlineEdit.setObjectName("URLlineEdit")
        self.gridLayout.addWidget(self.URLlineEdit, 4, 2, 1, 1)
        self.PasswordlineEdit_3 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PasswordlineEdit_3.setFont(font)
        self.PasswordlineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password )
        self.PasswordlineEdit_3.setObjectName("PasswordlineEdit_3")
        self.gridLayout.addWidget(self.PasswordlineEdit_3, 3, 1, 1, 2)
        self.AddAcclabel = QtWidgets.QLabel(self.widget)
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
        self.gridLayout.addWidget(self.AddAcclabel, 0, 0, 1, 4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.GenerateButton = QtWidgets.QPushButton(self.widget)
        self.GenerateButton.setObjectName("GenerateButton")
        self.horizontalLayout_2.addWidget(self.GenerateButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AddButton = QtWidgets.QPushButton(self.widget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("styles\\../Icons/plus-16.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddButton.setIcon(icon)
        self.AddButton.setObjectName("AddButton")
        self.horizontalLayout.addWidget(self.AddButton)
        self.ExitButton = QtWidgets.QPushButton(self.widget)
        self.ExitButton.setObjectName("ExitButton")
        self.horizontalLayout.addWidget(self.ExitButton)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 4)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 618, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
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
    ui = AddPasswordWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
