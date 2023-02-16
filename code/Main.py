from PyQt5 import QtCore, QtGui, QtWidgets
from crateCatagory import CreateCatagoryMainWindow
from AddAccount import AddAccountWindow
from Login import AuthWindow
from Encryption import EncryptSystem
from Dialog import DialogBox
import sys
from EditAccount import AccountEditWindow

class MainWindow(object):
    def __init__(self) -> None:
        super().__init__()
        self.dialogBox = DialogBox()
        self.FILE_PATH = "data.axx"
        self.CATEGORY_CONTAINER = 'catagories'
        self.CATEGORYPASSWORD_CONTAINER = 'catagorypasswords'
        self.CATAGORYLIST_CONTAINER = "catagoryList"
        self.CATEGORY_ITEMHEADER = 'Catagory'
        self.INDEX_ITEMHEADER = 'No'
        self.encrypt = EncryptSystem(master_password="000")
        self.data = self.encrypt.loadJsonData(self.FILE_PATH)
        self.searchArea = ["username", "email", "tag"]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 734)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.deleteCatagory = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteCatagory.sizePolicy().hasHeightForWidth())
        self.deleteCatagory.setSizePolicy(sizePolicy)
        self.deleteCatagory.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deleteCatagory.setFont(font)
        self.deleteCatagory.setObjectName("deleteCatagory")
        self.gridLayout.addWidget(self.deleteCatagory, 5, 0, 1, 2)
        self.searchPassword = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.searchPassword.setFont(font)
        self.searchPassword.setObjectName("searchPassword")
        self.gridLayout.addWidget(self.searchPassword, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.catagoryList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catagoryList.sizePolicy().hasHeightForWidth())
        self.catagoryList.setSizePolicy(sizePolicy)
        self.catagoryList.setObjectName("catagoryList")
        self.verticalLayout.addWidget(self.catagoryList)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 2)
        self.search = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search.setFont(font)
        self.search.setInputMask("")
        self.search.setText("")
        self.search.setObjectName("search")
        self.gridLayout.addWidget(self.search, 0, 1, 1, 2)
        self.addCatagoryButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addCatagoryButton.sizePolicy().hasHeightForWidth())
        self.addCatagoryButton.setSizePolicy(sizePolicy)
        self.addCatagoryButton.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.addCatagoryButton.setFont(font)
        self.addCatagoryButton.setObjectName("addCatagoryButton")
        self.gridLayout.addWidget(self.addCatagoryButton, 4, 0, 1, 2)
        self.addPassword = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addPassword.sizePolicy().hasHeightForWidth())
        self.addPassword.setSizePolicy(sizePolicy)
        self.addPassword.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addPassword.setFont(font)
        self.addPassword.setObjectName("addPassword")
        self.gridLayout.addWidget(self.addPassword, 0, 3, 1, 1)
        self.deletePassword = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deletePassword.sizePolicy().hasHeightForWidth())
        self.deletePassword.setSizePolicy(sizePolicy)
        self.deletePassword.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deletePassword.setFont(font)
        self.deletePassword.setObjectName("deletePassword")
        self.gridLayout.addWidget(self.deletePassword, 2, 3, 1, 1)
        self.passwordList = QtWidgets.QTreeWidget(self.centralwidget)
        self.passwordList.setObjectName("passwordList")
        self.gridLayout.addWidget(self.passwordList, 2, 2, 4, 1)
        self.catagoryLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.catagoryLabel.setFont(font)
        self.catagoryLabel.setStyleSheet("background-color: rgb(173, 173, 173);")
        self.catagoryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.catagoryLabel.setObjectName("catagoryLabel")
        self.gridLayout.addWidget(self.catagoryLabel, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # add manually
        self.addCatagoryButton.clicked.connect(self.OpenCrateCatagoryWindow)
        self.deleteCatagory.clicked.connect(self.deleteCategory)
        self.addPassword.clicked.connect(self.OpenAddAccountWindow)

        # open selected password
        self.passwordList.itemDoubleClicked.connect(self.OpenPassword)
        self.passwordList.itemActivated.connect(
            self.OpenPassword)  # enter-key binding
        # delete selected password
        self.deletePassword.clicked.connect(self.deleteSelectedPassword)
        # open Catagory
        self.catagoryList.itemDoubleClicked.connect(self.OpenCategoryAuthWindow)
        self.catagoryList.itemActivated.connect(
            self.OpenCategoryAuthWindow)  # enter-key binding
        
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
        self.crateCatagoryWindowUi.cancel.clicked.connect(self.crateCatagoryWindow.close)
        self.crateCatagoryWindowUi.NamelineEdit.returnPressed.connect(self.addCatagory) # Enter key 
        self.crateCatagoryWindowUi.PasslineEdit.returnPressed.connect(self.addCatagory) # Enter key

        self.crateCatagoryWindow.show()

    def OpenAddAccountWindow(self):
        if self.openCatagory == None:
            self.dialogBox.Information(title="No catagory",message="Please open a catagory first or create a catagory")
            return
        self.addPasswordWindow = QtWidgets.QMainWindow()
        self.addPasswordWindowUi = AddAccountWindow()
        self.addPasswordWindowUi.setupUi(self.addPasswordWindow)

        # banding events to button
        self.addPasswordWindowUi.AddButton.clicked.connect(self.createPassword)
        self.addPasswordWindowUi.ExitButton.clicked.connect(
            self.addPasswordWindow.close)
        # showing the window
        self.addPasswordWindow.show()

    def OpenCategoryAuthWindow(self):
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
    
    def SwitchCategory(self,category:str):
        self.authWindow = QtWidgets.QMainWindow()
        self.authWindowUi = AuthWindow()
        self.authWindowUi.setupUi(self.authWindow)

        # banding events to button
        self.authWindowUi.Createlabel_3.clicked.connect(lambda : self.OpenCatagoryByName(category))
        self.authWindowUi.Exitlabel_3.clicked.connect(self.authWindow.close)
        self.authWindowUi.passwordLineEdit.returnPressed.connect(lambda : self.OpenCatagoryByName(category))
        self.authWindowUi.MasterPasswordlabel.setText(
            f"Password for {category}")

        self.authWindow.show()


    # Function for open account Password Window
    def OpenAccountEditWindow(self):
        self.accountEditWindow = QtWidgets.QMainWindow()
        self.accountEditWindowUi = AccountEditWindow()
        self.accountEditWindowUi.setupUi(self.accountEditWindow)

        # banding events to button
        self.accountEditWindowUi.SaveButton.clicked.connect(self.SaveAccount)
        self.accountEditWindowUi.ExitButton.clicked.connect(self.accountEditWindow.close)
        self.accountEditWindow.show()


    def addCatagory(self):
        if self.crateCatagoryWindowUi.NamelineEdit.text() != "" and self.crateCatagoryWindowUi.PasslineEdit.text() != "":
            item = QtWidgets.QListWidgetItem()
            item.setText(self.crateCatagoryWindowUi.NamelineEdit.text())
            self.catagoryList.addItem(item)

            self.data[self.CATEGORY_CONTAINER].update({

                f"{self.crateCatagoryWindowUi.NamelineEdit.text()}": {}
            }

            )
            self.data[self.CATEGORYPASSWORD_CONTAINER].update({
                f"{self.crateCatagoryWindowUi.NamelineEdit.text()}": f"{self.crateCatagoryWindowUi.PasslineEdit.text()}"
            })

            self.data[self.CATAGORYLIST_CONTAINER].append(
                self.crateCatagoryWindowUi.NamelineEdit.text())

            # updating the new dictionary
            self.encrypt.StoreJsonData(self.FILE_PATH,self.data)
            # closing the CreateCatagoryWindow
            self.crateCatagoryWindow.close()
        
        else:
            self.dialogBox.Information(title="Invalid",message="Invalid Credential")

    
    def deleteSelectedPassword(self):
        #we need to check if there is a catagory open
        if self.openCatagory != None:
            #we need to check if a password is selected
            if self.passwordList.selectedItems() != []:
                #we need to remove the password from the catagory
                self.data[self.CATEGORY_CONTAINER][self.openCatagory].pop(self.passwordList.selectedItems()[0].text(0))
                #we need to save the new data
                self.encrypt.StoreJsonData(self.FILE_PATH,self.data)
                #we need to clear the password list
                self.passwordList.clear()
                #we need to open the current catagory again
                self.OpenCatagoryByName(self.openCatagory)

            else:
                #if no password was selected we need to show an error message
                self.dialogBox.Information(title="No password",message="Please select a password first")
        else:
            #if no catagory was open we need to show an error message
            self.dialogBox.Information(title="No catagory",message="Please open a catagory first or create a catagory")


    def deleteCategory(self):
        if self.openCatagory != None:
            self.catagoryList.setCurrentItem(self.catagoryList.item(self.data[self.CATAGORYLIST_CONTAINER].index(self.openCatagory)))
            if self.openCatagory == self.catagoryList.item(self.catagoryList.currentRow()).text():
                
                self.catagoryList.takeItem(self.catagoryList.currentRow())
                del self.data[self.CATEGORY_CONTAINER][self.openCatagory]
                self.data[self.CATAGORYLIST_CONTAINER].remove(self.openCatagory)
                self.encrypt.StoreJsonData(self.FILE_PATH,self.data, )
                # updating the catagory list
                self.catagoryList.clear()
                self.loadCatagories()
                # clearing the passwords
                self.passwordList.clear()
                self.openCatagory = None
                self.catagoryLabel.setText(f"Catagory")
        
        else:
            self.dialogBox.Critical(title="No catagory selected",message="Please open a catagory first or create a catagory")



    def createPassword(self):
        label = self.addPasswordWindowUi.TaglineEdit.text()
        username = self.addPasswordWindowUi.UsernamelineEdit.text()
        email = self.addPasswordWindowUi.EmaillineEdit.text()
        password = self.addPasswordWindowUi.PasswordlineEdit_3.text()
        url = self.addPasswordWindowUi.URLlineEdit.text()
        catagory = self.openCatagory

        if label != "" and email != "" and password != "" and url != "":
            self.data[self.CATEGORY_CONTAINER][self.openCatagory].update({
                f'{str(len(self.data[self.CATEGORY_CONTAINER][self.openCatagory]) +1)}': {
                    "id": f'{len(self.data[self.CATEGORY_CONTAINER][self.openCatagory]) +1}',
                    "email": email,
                    "tag": label,
                    "password": password,
                    "url": url,
                    "username": username,
                    "catagory":catagory
                }
            })

            # updating the new dictionary
            self.encrypt.StoreJsonData(self.FILE_PATH,self.data)
            # close the AddAccountWindow
            self.addPasswordWindow.close()
        
        else:
            self.dialogBox.Critical(title="Invalid",message="Invalid Credential")


        # Reopening the password list
        self.OpenCatagoryByName(self.openCatagory)

    def Search(self):
        query = self.search.text().lower()
        result = []
        # check it the query is whitespace or empty
        if query.isspace() or query == "":
            self.dialogBox.Critical(title="Empty query",message="Search cannot be empty")
            return

        # Searching for the query in [tag,username,email]
        for catagory in self.data[self.CATAGORYLIST_CONTAINER]:
            for i in self.data[self.CATEGORY_CONTAINER][catagory]:
                for j in self.data[self.CATEGORY_CONTAINER][catagory][i]:
                    # j is the item headers [id,tag,username,password,email,url]
                    if j in self.searchArea:
                        if str(self.data[self.CATEGORY_CONTAINER][catagory][i][j]).lower().find(query) != -1:
                            if self.data[self.CATEGORY_CONTAINER][catagory][i] not in result:
                                result.append(self.data[self.CATEGORY_CONTAINER][catagory][i])
        
        # display the result in password list
        self.passwordList.clear()
        if len(result) > 0:
            for index, data in enumerate(result):

                item_0 = QtWidgets.QTreeWidgetItem(self.passwordList)
                self.passwordList.topLevelItem(index).setText(
                    0, str(data['id']))
                self.passwordList.topLevelItem(index).setText(
                    1, str(data['tag']))
                self.passwordList.topLevelItem(index).setText(
                    2, str(data['username']))
                self.passwordList.topLevelItem(index).setText(
                    3, str(data['email']))
                self.passwordList.topLevelItem(
                    index).setText(4, "**************")
                self.passwordList.topLevelItem(index).setText(
                    5, str(data['url']))
                self.passwordList.topLevelItem(index).setText(
                    6, str(data['catagory']))
        else:
            self.dialogBox.Information(title="Nothing Found",message=f"No result found for '{query}'")


    def SaveAccount(self, id, catagory):
        label = self.accountEditWindowUi.tagLineEdit.text()
        username = self.accountEditWindowUi.userNameLineEdit.text()
        email = self.accountEditWindowUi.emailLineEdit.text()
        password = self.accountEditWindowUi.passwordLintEdit.text()
        url = self.accountEditWindowUi.URLlineEdit.text()

        # changing the data
        self.data[self.CATEGORY_CONTAINER][catagory][id]['tag'] = label
        self.data[self.CATEGORY_CONTAINER][catagory][id]['username'] = username
        self.data[self.CATEGORY_CONTAINER][catagory][id]['email'] = email
        self.data[self.CATEGORY_CONTAINER][catagory][id]['password'] = password
        self.data[self.CATEGORY_CONTAINER][catagory][id]['url'] = url
        # store the data
        self.encrypt.StoreJsonData(self.FILE_PATH,self.data)
        # exit the window
        self.accountEditWindow.close()


    def OpenPassword(self):

        id = self.passwordList.currentItem().text(0)
        catagory = self.passwordList.currentItem().text(6)

        if catagory == self.openCatagory:

            password = self.data[self.CATEGORY_CONTAINER][self.openCatagory][id]['password']
            email = self.data[self.CATEGORY_CONTAINER][self.openCatagory][id]['email']
            url = self.data[self.CATEGORY_CONTAINER][self.openCatagory][id]['url']
            username = self.data[self.CATEGORY_CONTAINER][self.openCatagory][id]['username']
            tag = self.data[self.CATEGORY_CONTAINER][self.openCatagory][id]['tag']


            self.accountEditWindow = QtWidgets.QMainWindow()
            self.accountEditWindowUi = AccountEditWindow()
            self.accountEditWindowUi.setupUi(self.accountEditWindow)
            # setting the data
            self.accountEditWindowUi.tagLineEdit.setText(tag)
            self.accountEditWindowUi.userNameLineEdit.setText(username)
            self.accountEditWindowUi.emailLineEdit.setText(email)
            self.accountEditWindowUi.passwordLintEdit.setText(password)
            self.accountEditWindowUi.URLlineEdit.setText(url)


            # banding events to button
            self.accountEditWindowUi.SaveButton.clicked.connect(lambda: self.SaveAccount(id,catagory))
            self.accountEditWindowUi.ExitButton.clicked.connect(self.accountEditWindow.close)
            self.accountEditWindow.show()

        else:
            self.SwitchCategory(catagory)


    # Opening category password
    def OpenCatagory(self):
        # getting the catagory name
        catagoryName = self.catagoryList.item(self.catagoryList.currentRow()).text()
        
        print(catagoryName)
            

        #  checking if the password is correct
        if self.data[self.CATEGORYPASSWORD_CONTAINER][catagoryName] == self.authWindowUi.passwordLineEdit.text():
            # Updating the Catagory label
            self.catagoryLabel.setText(f"Catagory:{catagoryName}")
            # clear opened password list
            self.passwordList.clear()
            self.openCatagory = catagoryName
            for index, data in enumerate(self.data[self.CATEGORY_CONTAINER][catagoryName]):
                item_0 = QtWidgets.QTreeWidgetItem(self.passwordList)
                self.passwordList.topLevelItem(index).setText(
                    0, str(self.data[self.CATEGORY_CONTAINER][catagoryName][data]['id']))
                self.passwordList.topLevelItem(index).setText(
                    1, str(self.data[self.CATEGORY_CONTAINER][catagoryName][data]['tag']))
                self.passwordList.topLevelItem(index).setText(
                    2, str(self.data[self.CATEGORY_CONTAINER][catagoryName][data]['username']))
                self.passwordList.topLevelItem(index).setText(
                    3, str(self.data[self.CATEGORY_CONTAINER][catagoryName][data]['email']))
                self.passwordList.topLevelItem(
                    index).setText(4, "**************")
                self.passwordList.topLevelItem(index).setText(
                    5, str(self.data[self.CATEGORY_CONTAINER][catagoryName][data]['url']))
                self.passwordList.topLevelItem(index).setText(
                    6, str(self.data[self.CATEGORY_CONTAINER][catagoryName][data]['catagory']))
            # close the auth window
            self.authWindow.close() 

        else:
            self.dialogBox.Critical(title='Wrong Password',message="Wrong Password!!")



    def OpenCatagoryByName(self, catagoryName):
        self.passwordList.clear()
        #  checking if the password is correct
        if self.data[self.CATEGORYPASSWORD_CONTAINER][catagoryName] == self.authWindowUi.passwordLineEdit.text():
            self.openCatagory = catagoryName
            self.catagoryLabel.setText(f"Catagory:{catagoryName}")
            
            for index, data in enumerate(self.data[self.CATEGORY_CONTAINER][catagoryName]):
                item_0 = QtWidgets.QTreeWidgetItem(self.passwordList)
                self.passwordList.topLevelItem(index).setText(
                    0, str(self.data[self.CATEGORY_CONTAINER][catagoryName][data]['id']))
                self.passwordList.topLevelItem(index).setText(
                    1, str(self.data[self.CATEGORY_CONTAINER][catagoryName][data]['tag']))
                self.passwordList.topLevelItem(index).setText(
                    2, str(self.data[self.CATEGORY_CONTAINER][catagoryName][data]['username']))
                self.passwordList.topLevelItem(index).setText(
                    3, str(self.data[self.CATEGORY_CONTAINER][catagoryName][data]['email']))
                self.passwordList.topLevelItem(
                    index).setText(4, "**************")
                self.passwordList.topLevelItem(index).setText(
                    5, str(self.data[self.CATEGORY_CONTAINER][catagoryName][data]['url']))
                self.passwordList.topLevelItem(index).setText(
                    6, str(self.data[self.CATEGORY_CONTAINER][catagoryName][data]['catagory']))
            # close the auth window
            self.authWindow.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Manager"))
        # MainWindow.setWindowTitle(_translate("MainWindow", "Password Manager - Made by mhEarth on fiverr for osama988"))
        self.catagoryLabel.setText(_translate("MainWindow", "Categories"))
        __sortingEnabled = self.catagoryList.isSortingEnabled()
        self.catagoryList.setSortingEnabled(False)
        self.catagoryList.setSortingEnabled(__sortingEnabled)
        self.searchPassword.setText(_translate("MainWindow", "Search"))
        self.search.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.addCatagoryButton.setText(_translate("MainWindow", "Add"))
        self.deleteCatagory.setText(_translate("MainWindow", "Delete"))
        self.addPassword.setText(_translate("MainWindow", "Add"))
        self.deletePassword.setText(_translate("MainWindow", "Delete"))

        self.passwordList.headerItem().setText(0, _translate("MainWindow", self.INDEX_ITEMHEADER))
        self.passwordList.headerItem().setText(1, _translate("MainWindow", "Tag"))
        self.passwordList.headerItem().setText(2, _translate("MainWindow", "Username"))
        self.passwordList.headerItem().setText(3, _translate("MainWindow", "Email"))
        self.passwordList.headerItem().setText(4, _translate("MainWindow", "Password"))
        self.passwordList.headerItem().setText(5, _translate("MainWindow", "URL"))
        self.passwordList.headerItem().setText(6, _translate("MainWindow", self.CATEGORY_ITEMHEADER))
        __sortingEnabled = self.passwordList.isSortingEnabled()
        self.passwordList.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
