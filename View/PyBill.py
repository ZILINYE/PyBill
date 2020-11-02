# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yezil\Desktop\Project\pybill\Ui\PyBill.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(663, 741)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(663, 741))
        MainWindow.setMaximumSize(QtCore.QSize(663, 741))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(530, 620, 113, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        self.exit.setObjectName("exit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 50, 621, 561))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(120)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.Month = QtWidgets.QTextBrowser(self.centralwidget)
        self.Month.setGeometry(QtCore.QRect(190, 10, 271, 31))
        self.Month.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Month.setObjectName("Month")
        self.PreviousMonth = QtWidgets.QPushButton(self.centralwidget)
        self.PreviousMonth.setGeometry(QtCore.QRect(92, 10, 91, 29))
        self.PreviousMonth.setMinimumSize(QtCore.QSize(91, 29))
        self.PreviousMonth.setMaximumSize(QtCore.QSize(91, 29))
        self.PreviousMonth.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PreviousMonth.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.PreviousMonth.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/Icon/Previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PreviousMonth.setIcon(icon)
        self.PreviousMonth.setObjectName("PreviousMonth")
        self.NextMonth = QtWidgets.QPushButton(self.centralwidget)
        self.NextMonth.setGeometry(QtCore.QRect(470, 10, 91, 29))
        self.NextMonth.setMinimumSize(QtCore.QSize(91, 29))
        self.NextMonth.setMaximumSize(QtCore.QSize(91, 29))
        self.NextMonth.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.NextMonth.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.NextMonth.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/Icon/Forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NextMonth.setIcon(icon1)
        self.NextMonth.setObjectName("NextMonth")
        self.addRow = QtWidgets.QPushButton(self.centralwidget)
        self.addRow.setGeometry(QtCore.QRect(20, 620, 71, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/Icon/Add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addRow.setIcon(icon2)
        self.addRow.setObjectName("addRow")
        self.delRow = QtWidgets.QPushButton(self.centralwidget)
        self.delRow.setGeometry(QtCore.QRect(100, 620, 71, 31))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/Icon/Remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delRow.setIcon(icon3)
        self.delRow.setObjectName("delRow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.OpenNew = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/Icon/icons8-open-parcel-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OpenNew.setIcon(icon4)
        self.OpenNew.setObjectName("OpenNew")
        self.AddNew = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/Icon/icons8-new-copy-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddNew.setIcon(icon5)
        self.AddNew.setObjectName("AddNew")
        self.save_change = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/Icon/icons8-save-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_change.setIcon(icon6)
        self.save_change.setObjectName("save_change")
        self.edit_person = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/Icon/user (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_person.setIcon(icon7)
        self.edit_person.setObjectName("edit_person")
        self.edit_cate = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/Icon/list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_cate.setIcon(icon8)
        self.edit_cate.setObjectName("edit_cate")
        self.edit_owe = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/Icon/money-flow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_owe.setIcon(icon9)
        self.edit_owe.setObjectName("edit_owe")
        self.Calculate = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon/Icon/calculator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Calculate.setIcon(icon10)
        self.Calculate.setObjectName("Calculate")
        self.toolBar.addAction(self.AddNew)
        self.toolBar.addAction(self.OpenNew)
        self.toolBar.addAction(self.save_change)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.edit_person)
        self.toolBar.addAction(self.edit_cate)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.edit_owe)
        self.toolBar.addAction(self.Calculate)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyBill"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Spend"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Description"))
        self.PreviousMonth.setToolTip(_translate("MainWindow", "<html><head/><body><p>Previous Month</p></body></html>"))
        self.NextMonth.setToolTip(_translate("MainWindow", "<html><head/><body><p>Next Month</p></body></html>"))
        self.addRow.setToolTip(_translate("MainWindow", "<html><head/><body><p>Add New Record</p></body></html>"))
        self.addRow.setText(_translate("MainWindow", "Add"))
        self.delRow.setToolTip(_translate("MainWindow", "<html><head/><body><p>Remove Record</p></body></html>"))
        self.delRow.setText(_translate("MainWindow", "Delete"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.OpenNew.setText(_translate("MainWindow", "Open"))
        self.OpenNew.setToolTip(_translate("MainWindow", "Open New "))
        self.AddNew.setText(_translate("MainWindow", "AddNew"))
        self.AddNew.setToolTip(_translate("MainWindow", "Add New"))
        self.save_change.setText(_translate("MainWindow", "SaveChange"))
        self.save_change.setToolTip(_translate("MainWindow", "Save Change"))
        self.edit_person.setText(_translate("MainWindow", "EditPerson"))
        self.edit_person.setToolTip(_translate("MainWindow", "Edit Person"))
        self.edit_cate.setText(_translate("MainWindow", "EditCategory"))
        self.edit_cate.setToolTip(_translate("MainWindow", "EditCategory"))
        self.edit_owe.setText(_translate("MainWindow", "AddOwe"))
        self.edit_owe.setToolTip(_translate("MainWindow", "AddOwe"))
        self.Calculate.setText(_translate("MainWindow", "Calculate"))
        self.Calculate.setToolTip(_translate("MainWindow", "Calculate"))
from . import resource
