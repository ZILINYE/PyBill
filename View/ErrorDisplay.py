# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yezil\Desktop\Project\pybill\Ui\ErrorDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ErrorMsg(object):
    def setupUi(self, ErrorMsg):
        ErrorMsg.setObjectName("ErrorMsg")
        ErrorMsg.resize(300, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ErrorMsg.sizePolicy().hasHeightForWidth())
        ErrorMsg.setSizePolicy(sizePolicy)
        ErrorMsg.setMinimumSize(QtCore.QSize(300, 200))
        ErrorMsg.setMaximumSize(QtCore.QSize(300, 200))
        self.ErrorShow = QtWidgets.QTextBrowser(ErrorMsg)
        self.ErrorShow.setEnabled(True)
        self.ErrorShow.setGeometry(QtCore.QRect(0, 70, 300, 130))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ErrorShow.sizePolicy().hasHeightForWidth())
        self.ErrorShow.setSizePolicy(sizePolicy)
        self.ErrorShow.setMinimumSize(QtCore.QSize(300, 130))
        self.ErrorShow.setMaximumSize(QtCore.QSize(300, 130))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ErrorShow.setFont(font)
        self.ErrorShow.setStyleSheet("image: url(:/NotifyWindow/Icon/correcct.png);")
        self.ErrorShow.setObjectName("ErrorShow")
        self.ErrorShow_2 = QtWidgets.QTextBrowser(ErrorMsg)
        self.ErrorShow_2.setEnabled(True)
        self.ErrorShow_2.setGeometry(QtCore.QRect(0, 0, 300, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ErrorShow_2.sizePolicy().hasHeightForWidth())
        self.ErrorShow_2.setSizePolicy(sizePolicy)
        self.ErrorShow_2.setMinimumSize(QtCore.QSize(300, 70))
        self.ErrorShow_2.setMaximumSize(QtCore.QSize(300, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ErrorShow_2.setFont(font)
        self.ErrorShow_2.setStyleSheet("image: url(:/NotifyWindow/Icon/correcct.png);")
        self.ErrorShow_2.setObjectName("ErrorShow_2")

        self.retranslateUi(ErrorMsg)
        QtCore.QMetaObject.connectSlotsByName(ErrorMsg)

    def retranslateUi(self, ErrorMsg):
        _translate = QtCore.QCoreApplication.translate
        ErrorMsg.setWindowTitle(_translate("ErrorMsg", "Dialog"))
        self.ErrorShow.setHtml(_translate("ErrorMsg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.ErrorShow_2.setHtml(_translate("ErrorMsg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icon/Icon/error.png\" /></p></body></html>"))
from . import Icon_rc
