import sys
from PyQt5 import QtWidgets,QtGui


class DialogBox:

    def Information(self,title,message):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)
        msg.setIcon(QtWidgets.QMessageBox.Information)

        font = QtGui.QFont()
        font.setPointSize(9)
        msg.setFont(font)

        msg.setText(message)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        retval = msg.exec_()
    
    def Critical(self,title,message):

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle(title)

        font = QtGui.QFont()
        font.setPointSize(9)
        msg.setFont(font)
        msg.setText(message)

        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = msg.exec_()

    def Warnings(self,title,message):

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle(title)

        font = QtGui.QFont()
        font.setPointSize(9)
        msg.setFont(font)
        msg.setText(message)

        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        # msg.buttonClicked.connect(self.)
        retval = msg.exec_()

    def Question(self,title,message):

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setWindowTitle(title)

        font = QtGui.QFont()
        font.setPointSize(9)
        msg.setFont(font)
        msg.setText(message)

        msg.setStandardButtons(QtWidgets.QMessageBox.Ok  | QtWidgets.QMessageBox.No)
        msg.buttonClicked.connect(self.confirmation)
        retval = msg.exec_()

