# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View\ErrorDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ErrorMsg(object):
    def setupUi(self, ErrorMsg):
        ErrorMsg.setObjectName("ErrorMsg")
        ErrorMsg.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ErrorMsg.sizePolicy().hasHeightForWidth())
        ErrorMsg.setSizePolicy(sizePolicy)
        ErrorMsg.setMinimumSize(QtCore.QSize(400, 300))
        ErrorMsg.setMaximumSize(QtCore.QSize(400, 300))
        self.ErrorShow = QtWidgets.QTextBrowser(ErrorMsg)
        self.ErrorShow.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.ErrorShow.setObjectName("ErrorShow")

        self.retranslateUi(ErrorMsg)
        QtCore.QMetaObject.connectSlotsByName(ErrorMsg)

    def retranslateUi(self, ErrorMsg):
        _translate = QtCore.QCoreApplication.translate
        ErrorMsg.setWindowTitle(_translate("ErrorMsg", "Dialog"))
        self.ErrorShow.setHtml(_translate("ErrorMsg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ErrorMsg = QtWidgets.QDialog()
    ui = Ui_ErrorMsg()
    ui.setupUi(ErrorMsg)
    ErrorMsg.show()
    sys.exit(app.exec_())