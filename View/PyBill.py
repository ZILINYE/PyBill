# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/PyBill.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.edit_person = QtWidgets.QPushButton(self.centralwidget)
        self.edit_person.setGeometry(QtCore.QRect(100, 480, 131, 51))
        self.edit_person.setObjectName("edit_person")
        self.Calculate = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate.setGeometry(QtCore.QRect(300, 480, 171, 51))
        self.Calculate.setObjectName("Calculate")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(670, 540, 113, 32))
        self.exit.setObjectName("exit")
        self.edit_cate = QtWidgets.QPushButton(self.centralwidget)
        self.edit_cate.setGeometry(QtCore.QRect(560, 480, 131, 51))
        self.edit_cate.setObjectName("edit_cate")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(90, 50, 620, 361))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(120)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.Month = QtWidgets.QTextBrowser(self.centralwidget)
        self.Month.setGeometry(QtCore.QRect(250, 10, 271, 31))
        self.Month.setObjectName("Month")
        self.PreviousMonth = QtWidgets.QPushButton(self.centralwidget)
        self.PreviousMonth.setGeometry(QtCore.QRect(182, 10, 61, 32))
        self.PreviousMonth.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("View/../../../Downloads/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PreviousMonth.setIcon(icon)
        self.PreviousMonth.setObjectName("PreviousMonth")
        self.NextMonth = QtWidgets.QPushButton(self.centralwidget)
        self.NextMonth.setGeometry(QtCore.QRect(530, 10, 61, 31))
        self.NextMonth.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("View/../../../Downloads/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NextMonth.setIcon(icon1)
        self.NextMonth.setObjectName("NextMonth")
        self.addRow = QtWidgets.QPushButton(self.centralwidget)
        self.addRow.setGeometry(QtCore.QRect(90, 420, 41, 31))
        self.addRow.setObjectName("addRow")
        self.delRow = QtWidgets.QPushButton(self.centralwidget)
        self.delRow.setGeometry(QtCore.QRect(140, 420, 41, 31))
        self.delRow.setObjectName("delRow")
        self.save_change = QtWidgets.QPushButton(self.centralwidget)
        self.save_change.setGeometry(QtCore.QRect(600, 420, 113, 32))
        self.save_change.setObjectName("save_change")
        self.cancel_change = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_change.setGeometry(QtCore.QRect(490, 420, 113, 32))
        self.cancel_change.setObjectName("cancel_change")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyBill"))
        self.edit_person.setText(_translate("MainWindow", "Edit Person"))
        self.Calculate.setText(_translate("MainWindow", "Calculate"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.edit_cate.setText(_translate("MainWindow", "Edit Category"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Description"))
        self.addRow.setText(_translate("MainWindow", "+"))
        self.delRow.setText(_translate("MainWindow", "-"))
        self.save_change.setText(_translate("MainWindow", "Save"))
        self.cancel_change.setText(_translate("MainWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
