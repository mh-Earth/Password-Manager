from PyQt5 import QtCore, QtGui, QtWidgets
from crateCatagory import CreateCatagoryMainWindow
from AddPassword import AddPasswordWindow
from Login import AuthWindow
from Password import PasswordWindow
from Encryption import Encryption
from Dialog import DialogBox
import sys

class Ui_MainWindow(object):
    def __init__(self) -> None:
        super().__init__()
        self.dialogBox = DialogBox()
        # pickle system
        self.FILE_PATH = "data.pkl"
        self.CATAGORY_CONTAINER = 'catagories'
        self.CATEGORYPASSWORD_CONTAINER = 'catagorypasswords'
        self.CATAGORYLIST_CONTAINER = "catagoryList"
        self.encrypt = Encryption()
        self.data = self.encrypt.loadObjFromFile(self.FILE_PATH)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1044, 338)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.catagoryLabel = QtWidgets.QLabel(self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.catagoryLabel.setFont(font)
        self.catagoryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.catagoryLabel.setObjectName("label")
        self.verticalLayout.addWidget(self.catagoryLabel)
        self.catagoryList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.catagoryList.sizePolicy().hasHeightForWidth())
        self.catagoryList.setSizePolicy(sizePolicy)
        self.catagoryList.setObjectName("catagoryList")
        self.verticalLayout.addWidget(self.catagoryList)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 2)
        self.searchPassword = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.searchPassword.setFont(font)
        self.searchPassword.setObjectName("searchPassword")
        self.gridLayout.addWidget(self.searchPassword, 0, 0, 1, 1)
        self.search = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search.setFont(font)
        self.search.setInputMask("")
        self.search.setText("")
        self.search.setObjectName("search")
        self.gridLayout.addWidget(self.search, 0, 1, 1, 2)
        self.addCatagoryButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.addCatagoryButton.sizePolicy().hasHeightForWidth())
        self.addCatagoryButton.setSizePolicy(sizePolicy)
        self.addCatagoryButton.setMinimumSize(QtCore.QSize(200, 35))
        self.addCatagoryButton.setMaximumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.addCatagoryButton.setFont(font)
        self.addCatagoryButton.setObjectName("addCatagory")
        self.gridLayout.addWidget(self.addCatagoryButton, 3, 0, 1, 2)
        self.deleteCatagory = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.deleteCatagory.sizePolicy().hasHeightForWidth())
        self.deleteCatagory.setSizePolicy(sizePolicy)
        self.deleteCatagory.setMinimumSize(QtCore.QSize(200, 35))
        self.deleteCatagory.setMaximumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.deleteCatagory.setFont(font)
        self.deleteCatagory.setObjectName("deleteCatagory")
        self.gridLayout.addWidget(self.deleteCatagory, 4, 0, 1, 2)
        self.addPassword = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addPassword.setFont(font)
        self.addPassword.setObjectName("addPassword")
        self.gridLayout.addWidget(self.addPassword, 0, 4, 1, 1)
        self.passwordList = QtWidgets.QTreeWidget(self.centralwidget)
        self.passwordList.setObjectName("passwordList")
        self.gridLayout.addWidget(self.passwordList, 2, 2, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        # add manually
        self.addCatagoryButton.clicked.connect(self.OpenCrateCatagoryWindow)
        self.deleteCatagory.clicked.connect(self.delete)
        self.addPassword.clicked.connect(self.OpenAddPasswordWindow)

        # open selected password
        self.passwordList.itemDoubleClicked.connect(self.OpenPassword)
        self.passwordList.itemActivated.connect(
            self.OpenPassword)  # enter key binding
        # open Catagory
        self.catagoryList.itemDoubleClicked.connect(self.OpenAuthWindow)
        self.catagoryList.itemActivated.connect(
            self.OpenAuthWindow)  # enter key binding
        
        # search key
        self.search.returnPressed.connect(self.Search)
        self.searchPassword.clicked.connect(self.Search)

        self.openCatagory = None

        # Loading all catagories
        self.loadCatagories()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def loadCatagories(self):
        for catagory in self.data[self.CATAGORYLIST_CONTAINER]:
            item = QtWidgets.QListWidgetItem()
            item.setText(catagory)
            self.catagoryList.addItem(item)

    def OpenCrateCatagoryWindow(self):
        self.crateCatagoryWindow = QtWidgets.QMainWindow()
        self.crateCatagoryWindowUi = CreateCatagoryMainWindow()
        self.crateCatagoryWindowUi.setupUi(self.crateCatagoryWindow)

        # banding events to button
        self.crateCatagoryWindowUi.create.clicked.connect(self.addCatagory)
        self.crateCatagoryWindowUi.cancel.clicked.connect(
            self.crateCatagoryWindow.close)

        self.crateCatagoryWindow.show()

    def OpenAddPasswordWindow(self):
        if self.openCatagory == None:
            self.dialogBox.Information(title="No catagory",message="Please open a catagory first or create a catagory")
            return
        self.addPasswordWindow = QtWidgets.QMainWindow()
        self.addPasswordWindowUi = AddPasswordWindow()
        self.addPasswordWindowUi.setupUi(self.addPasswordWindow)

        # banding events to button
        self.addPasswordWindowUi.AddButton.clicked.connect(self.createPassword)
        self.addPasswordWindowUi.ExitButton.clicked.connect(
            self.addPasswordWindow.close)
        # showing the window
        self.addPasswordWindow.show()

    def OpenAuthWindow(self):
        self.authWindow = QtWidgets.QMainWindow()
        self.authWindowUi = AuthWindow()
        self.authWindowUi.setupUi(self.authWindow)

        # banding events to button
        self.authWindowUi.Createlabel_3.clicked.connect(self.OpenCatagory)
        self.authWindowUi.Exitlabel_3.clicked.connect(self.authWindow.close)
        self.authWindowUi.passwordLineEdit.returnPressed.connect(self.OpenCatagory)
        self.authWindowUi.MasterPasswordlabel.setText(
            f"Password for {self.catagoryList.item(self.catagoryList.currentRow()).text()}")

        self.authWindow.show()


    def addCatagory(self):
        if self.crateCatagoryWindowUi.NamelineEdit.text() != "" and self.crateCatagoryWindowUi.PasslineEdit.text() != "":
            item = QtWidgets.QListWidgetItem()
            item.setText(self.crateCatagoryWindowUi.NamelineEdit.text())
            # item = self.catagoryList.item(3)
            self.catagoryList.addItem(item)

            self.data[self.CATAGORY_CONTAINER].update({

                f"{self.crateCatagoryWindowUi.NamelineEdit.text()}": {}
            }

            )
            self.data[self.CATEGORYPASSWORD_CONTAINER].update({
                f"{self.crateCatagoryWindowUi.NamelineEdit.text()}": f"{self.crateCatagoryWindowUi.PasslineEdit.text()}"
            })

            self.data[self.CATAGORYLIST_CONTAINER].append(
                self.crateCatagoryWindowUi.NamelineEdit.text())

            # updating the new dictionary
            self.encrypt.storeData(self.data, self.FILE_PATH)
            # closing the CreateCatagoryWindow
            self.crateCatagoryWindow.close()
        
        else:
            self.dialogBox.Information(title="Invalid",message="Invalid Credential")

    def delete(self):
        if self.openCatagory != None:
            # self.dialogBox.Warnings(title="Delete Catagory",message=f"Delete {self.openCatagory}?")
            # self.dialogBox.confirmation()
            
            self.catagoryList.takeItem(self.catagoryList.currentRow())
            del self.data[self.CATAGORY_CONTAINER][self.openCatagory]
            self.data[self.CATAGORYLIST_CONTAINER].remove(self.openCatagory)
            self.encrypt.storeData(self.data, self.FILE_PATH)
            # updating the catagory list
            self.catagoryList.clear()
            self.loadCatagories()
            # clearing the passwords
            self.passwordList.clear()
        
        else:
            self.dialogBox.Critical(title="No catagory selected",message="Please open a catagory first or create a catagory")



    def createPassword(self):
        label = self.addPasswordWindowUi.TaglineEdit.text()
        email = self.addPasswordWindowUi.EmaillineEdit_2.text()
        password = self.addPasswordWindowUi.PasswordlineEdit_3.text()
        url = self.addPasswordWindowUi.URLlineEdit.text()

        if label != "" and email != "" and password != "" and url != "":
            self.data[self.CATAGORY_CONTAINER][self.openCatagory].update({
                f'{str(len(self.data[self.CATAGORY_CONTAINER][self.openCatagory]) +1)}': {
                    "id": f'{len(self.data[self.CATAGORY_CONTAINER][self.openCatagory]) +1}',
                    "email": email,
                    "tag": label,
                    "password": password,
                    "url": url
                }
            })

            # updating the new dictionary
            self.encrypt.storeData(self.data, self.FILE_PATH)
            # close the AddPasswordWindow
            self.addPasswordWindow.close()
        
        else:
            self.dialogBox.Critical(title="Invalid",message="Invalid Credential")


        # Reopening the password list
        self.OpenCatagoryByName(self.openCatagory)

    def Search(self):
        if self.openCatagory == None:
            self.dialogBox.Information(title="No catagory",message="Please open a catagory first or create a catagory")
            return
        
        query = self.search.text()
        result = []
        # Searching for the query in the opened catagory only
        for i in self.data[self.CATAGORY_CONTAINER][self.openCatagory]:
            for j in self.data[self.CATAGORY_CONTAINER][self.openCatagory][i]:
                if str(self.data[self.CATAGORY_CONTAINER][self.openCatagory][i][j]).find(query) != -1:
                    if self.data[self.CATAGORY_CONTAINER][self.openCatagory][i] not in result:
                        result.append(self.data[self.CATAGORY_CONTAINER][self.openCatagory][i])
        
            
        # display the result in password list
        self.passwordList.clear()

        for index, data in enumerate(result):
                item_0 = QtWidgets.QTreeWidgetItem(self.passwordList)
                self.passwordList.topLevelItem(index).setText(
                    0, str(data['id']))
                self.passwordList.topLevelItem(index).setText(
                    1, str(data['email']))
                self.passwordList.topLevelItem(index).setText(
                    2, str(data['tag']))
                self.passwordList.topLevelItem(
                    index).setText(3, "**************")
                self.passwordList.topLevelItem(index).setText(
                    4, str(data['url']))

    def OpenPassword(self):
        self.passwordWindow = QtWidgets.QMainWindow()
        self.passwordWindowUi = PasswordWindow()
        self.passwordWindowUi.setupUi(self.passwordWindow)

        id = self.passwordList.currentItem().text(0)
        password = self.data[self.CATAGORY_CONTAINER][self.openCatagory][id]['password']
        email = self.data[self.CATAGORY_CONTAINER][self.openCatagory][id]['email']
        url = self.data[self.CATAGORY_CONTAINER][self.openCatagory][id]['url']
        self.passwordWindowUi.Catagory.setText(f"Catagory:{self.openCatagory}")
        self.passwordWindowUi.lineEdit.setText(password)
        self.passwordWindowUi.email.setText(email)
        self.passwordWindowUi.Url.setText(url)

        self.passwordWindowUi.back.clicked.connect(self.passwordWindow.close)

        self.passwordWindow.show()

    # Opening category password
    def OpenCatagory(self):
        catagoryName = self.catagoryList.item(
            self.catagoryList.currentRow()).text()
        
        # Updating the Catagory label
        self.catagoryLabel.setText(f"Catagory:{catagoryName}")

        self.passwordList.clear()

        if self.data[self.CATEGORYPASSWORD_CONTAINER][catagoryName] == self.authWindowUi.passwordLineEdit.text():
            self.openCatagory = catagoryName
            for index, data in enumerate(self.data[self.CATAGORY_CONTAINER][catagoryName]):
                item_0 = QtWidgets.QTreeWidgetItem(self.passwordList)
                self.passwordList.topLevelItem(index).setText(
                    0, str(self.data[self.CATAGORY_CONTAINER][catagoryName][data]['id']))
                self.passwordList.topLevelItem(index).setText(
                    1, str(self.data[self.CATAGORY_CONTAINER][catagoryName][data]['tag']))
                self.passwordList.topLevelItem(index).setText(
                    2, str(self.data[self.CATAGORY_CONTAINER][catagoryName][data]['email']))
                self.passwordList.topLevelItem(
                    index).setText(3, "**************")
                self.passwordList.topLevelItem(index).setText(
                    4, str(self.data[self.CATAGORY_CONTAINER][catagoryName][data]['url']))
                self.authWindow.close() 

        else:
            self.dialogBox.Critical(title='Wrong Password',message="Worng Password!!")


        # close the auth window

    def OpenCatagoryByName(self, catagoryName):
        self.passwordList.clear()

        if self.data[self.CATEGORYPASSWORD_CONTAINER][catagoryName] == self.authWindowUi.passwordLineEdit.text():
            self.openCatagory = catagoryName
            for index, data in enumerate(self.data[self.CATAGORY_CONTAINER][catagoryName]):
                item_0 = QtWidgets.QTreeWidgetItem(self.passwordList)
                self.passwordList.topLevelItem(index).setText(
                    0, str(self.data[self.CATAGORY_CONTAINER][catagoryName][data]['id']))
                self.passwordList.topLevelItem(index).setText(
                    1, str(self.data[self.CATAGORY_CONTAINER][catagoryName][data]['tag']))
                self.passwordList.topLevelItem(index).setText(
                    2, str(self.data[self.CATAGORY_CONTAINER][catagoryName][data]['email']))
                self.passwordList.topLevelItem(
                    index).setText(3, "**************")
                self.passwordList.topLevelItem(index).setText(
                    4, str(self.data[self.CATAGORY_CONTAINER][catagoryName][data]['url']))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Manager"))
        self.catagoryLabel.setText(_translate("MainWindow", "Categories"))
        __sortingEnabled = self.catagoryList.isSortingEnabled()
        self.catagoryList.setSortingEnabled(False)
        self.catagoryList.setSortingEnabled(__sortingEnabled)
        self.searchPassword.setText(_translate("MainWindow", "Search"))
        self.search.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.addCatagoryButton.setText(_translate("MainWindow", "Add"))
        self.deleteCatagory.setText(_translate("MainWindow", "Delete"))
        self.addPassword.setText(_translate("MainWindow", "Add"))
        self.passwordList.headerItem().setText(0, _translate("MainWindow", "No"))
        self.passwordList.headerItem().setText(1, _translate("MainWindow", "Tag"))
        self.passwordList.headerItem().setText(2, _translate("MainWindow", "Email"))
        self.passwordList.headerItem().setText(3, _translate("MainWindow", "Password"))
        self.passwordList.headerItem().setText(4, _translate("MainWindow", "URL"))
        __sortingEnabled = self.passwordList.isSortingEnabled()
        self.passwordList.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
