from PyQt5 import QtCore, QtGui, QtWidgets


class CreateCatagoryMainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(538, 356)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(100, 0, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.NamelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NamelineEdit.setGeometry(QtCore.QRect(100, 90, 411, 31))
        self.NamelineEdit.setObjectName("NamelineEdit")
        self.PasslineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PasslineEdit.setGeometry(QtCore.QRect(100, 150, 411, 31))
        self.PasslineEdit.setObjectName("PasslineEdit")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(10, 90, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.name.setFont(font)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(10, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.password.setFont(font)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.create = QtWidgets.QPushButton(self.centralwidget)
        self.create.setGeometry(QtCore.QRect(390, 261, 121, 41))
        self.create.setObjectName("create")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(100, 261, 121, 41))
        self.cancel.setObjectName("cancel")
        MainWindow.setCentralWidget(self.centralwidget)

        # Add manually
        # self.cancel.clicked.connect(self.exit)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    # Buttons -> exit


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Create Category"))
        self.title.setText(_translate("MainWindow", "Create Category"))
        self.name.setText(_translate("MainWindow", "Name"))
        self.password.setText(_translate("MainWindow", "Password"))
        self.create.setText(_translate("MainWindow", "Create"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowTitle("Create Category")
    ui = CreateCatagoryMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
