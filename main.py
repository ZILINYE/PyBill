import sys
import time
from time import strftime
import json
import calendar
import sqlite3
from pymongo import MongoClient
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QComboBox,
    QLineEdit,
    QInputDialog,
    QDateEdit,
    QDateTimeEdit,
    QDialog,
    QFileDialog

)


from PyQt5.QtCore import QDateTime, QDate, Qt, QEvent
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5 import QtCore
from datetime import datetime

from View.PyBill import Ui_MainWindow
from View.dialog_edit import Ui_Dialog
from View.addowe import Add_owe
from View.Report import Report_Ui
from View.Create_storage import Ui_NewStorage
from View.ErrorDisplay import Ui_ErrorMsg
from View.SucessDisplay import Ui_SucessMsg

from datachan import Storage
from loadconf import Conf
from calculate import Calculator

# Ignore mouse wheel event on ComboBox


class CustomQCB(QComboBox):
    def wheelEvent(self, e):
        if e.type() == QEvent.Wheel:
            e.ignore()


class EditDialog(QMainWindow, Ui_Dialog):
    def __init__(self, dialog):
        super(EditDialog, self).__init__()
        self.dialog_title = dialog
        self.setupUi(self)
        self.setWindowTitle(self.dialog_title)
        self.GetPerson()
        # Gesture Actions
        self.add.clicked.connect(self.AddPerson)
        self.remove.clicked.connect(self.DelPerson)
        self.save.clicked.connect(self.Save)
        self.listWidget.itemDoubleClicked.connect(self.EditItem)
        self.cancelsave.clicked.connect(self.close)

    def EditItem(self, lstItem):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)

        if item is not None:
            string, ok = QInputDialog.getText(
                self,
                "Person Dialog",
                "Enter Person Name",
                QLineEdit.Normal,
                item.text(),
            )
            if ok and string is not None:
                item.setText(string)

    def GetPerson(self):
        connection = Storage(self.dialog_title)
        data = connection.Selec_Ui()
        self.listWidget.addItems(data)

    def AddPerson(self):
        row = self.listWidget.currentRow()
        text, ok = QInputDialog.getText(
            self, "Person Dialog", "Enter Person Name")

        if ok and text is not None:
            self.listWidget.insertItem(row, text)

    def DelPerson(self):
        listItem = self.listWidget.selectedItems()
        if not listItem:
            return
        for item in listItem:
            self.listWidget.takeItem(self.listWidget.row(item))

    def Save(self):
        save_list = []
        items_count = self.listWidget.count()
        for i in range(items_count):
            save_list.append(self.listWidget.item(i).text())

        connection = Storage(self.dialog_title, save_list)
        data = connection.Selec_DB()

        msg = "Sucessfully Saved !"
        s = SuShow(msg)
        s.exec_()

        self.close()


class EditOweDialog(QMainWindow, Add_owe):
    def __init__(self, person_list, year, month, month_index, max_date, min_date):
        super(EditOweDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Owe Record")

        self.person_list = person_list
        self.year = year
        self.month = month
        self.max_date = max_date
        self.min_date = min_date
        self.month_Number = month_index+1
        self.select_period = self.month + '/'+str(self.year)

        self.GetOwe()

        self.AddOwe.clicked.connect(self.AddRecord)
        self.DelOwe.clicked.connect(self.DelRecord)
        self.SaveOwe.clicked.connect(self.SaveRecord)

    def AddRecord(self):
        newrow = self.tableWidget1.rowCount() + 1
        self.tableWidget1.setRowCount(newrow)
        combobox1 = QComboBox()
        combobox1.addItems(self.person_list)
        combobox2 = QComboBox()
        combobox2.addItems(self.person_list)
        datebox = QDateEdit()
        datebox.setMinimumDate(self.min_date)
        datebox.setMaximumDate(self.max_date)
        datebox.setCalendarPopup(True)
        # Loop with ['person1','person2','Date','Spend','Description']
        for i in range(5):
            if i == 0:
                self.tableWidget1.setCellWidget(newrow-1, i, combobox1)
            elif i == 1:
                self.tableWidget1.setCellWidget(newrow-1, i, combobox2)
            elif i == 2:
                self.tableWidget1.setCellWidget(newrow-1, i, datebox)
            else:
                self.tableWidget1.setItem(newrow, i, QTableWidgetItem(""))

    def DelRecord(self):
        selected = self.tableWidget1.currentRow()
        self.tableWidget1.removeRow(selected)

    def SaveRecord(self):
        rows = self.tableWidget1.rowCount()
        new_list = []
        for row in range(0, rows):
            row_item = []
            for i in range(5):
                if i < 2:
                    item = self.tableWidget1.cellWidget(row, i)
                    item = item.currentText()
                elif i == 2:
                    item = self.tableWidget1.cellWidget(row, i)
                    item = item.text()
                elif i == 3:
                    item = self.tableWidget1.item(row, i).text()
                else:
                    item = self.tableWidget1.item(row, i)
                    if item is not None:
                        item = item.text()
                    else:
                        item = ''
                row_item.append(item)
            new_list.append(row_item)

        record = Storage('OweRecord', new_list, self.select_period)
        record1 = record.Record_DB()
        msg = "Sucessfully Saved !"
        s = SuShow(msg)
        s.exec_()
        self.close()

    def GetOwe(self):
        connection = self.MongoConnect()
        data = connection.Record_Ui()
        rowcount = len(data)
        self.tableWidget1.setRowCount(rowcount)
        self.tableWidget1.setColumnCount(5)
        for row_number, row_data in enumerate(data):
            for column_number, data in enumerate(row_data):
                if column_number < 3:
                    if column_number < 2:
                        personbox = QComboBox()
                        personbox.addItems(self.person_list)
                        personbox.setCurrentText(str(data))
                        self.tableWidget1.setCellWidget(
                            row_number, column_number, personbox
                        )
                    else:
                        datebox = QDateEdit()
                        date = QDate()
                        try:
                            yy = int(data.split('/')[0])
                            mm = int(data.split('/')[1])
                            dd = int(data.split('/')[2])
                        except:
                            yy = int(data.split('-')[0])
                            mm = int(data.split('-')[1])
                            dd = int(data.split('-')[2])
                        date.setDate(yy, mm, dd)
                        datebox.setDate(date)

                        datebox.setMinimumDate(self.min_date)
                        datebox.setMaximumDate(self.max_date)
                        datebox.setCalendarPopup(True)

                        self.tableWidget1.setCellWidget(
                            row_number, column_number, datebox
                        )

                else:
                    self.tableWidget1.setItem(
                        row_number, column_number, QTableWidgetItem(str(data))
                    )

    def MongoConnect(self):

        connection = Storage("OweRecord", savelist=None,
                             select_period=self.select_period)
        return connection


class Report(QMainWindow, Report_Ui):
    def __init__(self, total_cost, avageCost, SpendByPerson, SpendByCate, SolutionList):
        super(Report, self).__init__()
        self.setupUi(self)

        self.total_cost = total_cost
        self.avageCost = avageCost
        self.SpendByPerson = SpendByPerson
        self.SpendByCate = SpendByCate
        self.SolutionList = SolutionList
        self.series = QPieSeries()
        self.SetText()
        self.SetTable()
        self.SetChart()

    def SetText(self):
        self.totalSpend.setText(str(self.total_cost))
        self.averageSpend.setText(str(self.avageCost))

    def SetTable(self):
        rowcount = len(self.SpendByPerson)
        self.table2Widget.setRowCount(rowcount)
        self.table2Widget.setColumnCount(2)

        for i in range(rowcount):
            name = list(self.SpendByPerson.keys())[i]
            cost = list(self.SpendByPerson.values())[i]
            self.table2Widget.setItem(i, 0, QTableWidgetItem(str(name)))
            self.table2Widget.setItem(i, 1, QTableWidgetItem(str(cost)))
        slist = list(x[0] + ' 欠 ' + x[1]+' : '+x[2] for x in self.SolutionList)
        self.list2Widget.addItems(slist)

    def SetChart(self):
        for key, value in self.SpendByCate.items():
            self.series.append(key, value)
        self.series.setLabelsVisible(True)
        chart = QChart()
        chart.legend().hide()
        chart.addSeries(self.series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Monthly Summary")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        self.chartLayout.addWidget(chartview)


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.person_dialog = 'Person'
        self.cate_dialog = 'Category'

        # Set Up Title and DateBox Default Value
        current_month = strftime("%B")
        current_year = strftime("%Y")
        self.month = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        self.min_date = None
        self.max_date = None
        self.currentm_index = self.month.index(current_month)
        self.month_index = self.currentm_index
        self.selectedYear = int(current_year)
        self.current_period = self.SetTitle()
        self.select_period = self.current_period

        # Get Default Date Value and Get Last Day of Selected Month
        self.Cal_month()
        # Init Display
        self.GetRow()

        # Button Function
        self.NextMonth.clicked.connect(self.monthChangeNext)
        self.PreviousMonth.clicked.connect(self.monthChangePrevious)
        self.addRow.clicked.connect(self.AddRow)
        self.delRow.clicked.connect(self.DelRow)

        # Tools Bar
        self.save_change.triggered.connect(self.SaveChange)
        self.Calculate.triggered.connect(self.GetReport)
        self.edit_person.triggered.connect(self.person_window)
        self.edit_cate.triggered.connect(self.cate_window)
        self.edit_owe.triggered.connect(self.owe_window)
        self.OpenNew.triggered.connect(self.Open_New)

        # Exit Program
        self.exit.clicked.connect(self.close)

    def Open_New(self):

        self.dialog = NewStorage()

        self.dialog.show()
        i = self.dialog.exec_()

        if i == 1:

            self.close()
            self.__init__()
            self.show()
        else:
            x = ErrShow('Could not open file or cannot connect to database')
            x.show()

    def Add_New(self):

        self.dialog = NewStorage()
        self.dialog.show()
        i = self.dialog.exec_()
        if i == 1:
            self.close()
            self.__init__()
            self.show()
        else:
            x = ErrShow('Could not open file or cannot connect to database')
            x.show()

    def GetReport(self):
        x = Calculator(self.select_period)

        total_cost, avagcost, allpersonCost, cateCost, solutionList = x.returnData()
        self.dialog = Report(total_cost, avagcost,
                             allpersonCost, cateCost, solutionList)
        self.dialog.show()

    def SetTitle(self):

        selectedMonth = self.month[self.month_index]
        selectedYear = str(self.selectedYear)
        self.Month.setText(selectedMonth + " , " + selectedYear)
        self.Month.setAlignment(QtCore.Qt.AlignCenter)
        self.Month.setFontWeight(15)
        self.select_period = selectedMonth + "/" + selectedYear
        self.Cal_month()
        self.GetRow()

        return self.select_period

    def monthChangeNext(self):
        self.month_index += 1
        if self.month_index == 12:
            self.month_index = 0
            self.selectedYear += 1
        self.SetTitle()

    def monthChangePrevious(self):
        self.month_index -= 1
        if self.month_index < 0:
            self.month_index = 11
            self.selectedYear -= 1
        self.SetTitle()

    def person_window(self):
        self.dialog = EditDialog(self.person_dialog)
        self.dialog.show()

    def cate_window(self):
        self.dialog = EditDialog(self.cate_dialog)
        self.dialog.show()

    def owe_window(self):
        person = Storage(self.person_dialog)
        person1 = person.Selec_Ui()
        self.dialog = EditOweDialog(
            person1, self.selectedYear, self.month[self.month_index], self.month_index, self.max_date, self.min_date)
        self.dialog.show()

    def Cal_month(self):
        year = self.selectedYear
        mon = self.month_index + 1
        max_day = calendar.monthrange(year, mon)[1]
        self.min_date = QDate()
        self.min_date.setDate(year, mon, 1)
        self.max_date = QDate()
        self.max_date.setDate(year, mon, max_day)

    # Display Data into list view

    def ListRow(self, data, person, cate):
        rowcount = len(data)
        self.tableWidget.setRowCount(rowcount)
        self.tableWidget.setColumnCount(5)

        for row_number, row_data in enumerate(data):
            for column_number, data in enumerate(row_data):
                if column_number < 3:
                    if column_number == 0:
                        personbox = CustomQCB()

                        personbox.addItems(person)
                        personbox.setCurrentText(str(data))
                        self.tableWidget.setCellWidget(
                            row_number, column_number, personbox
                        )

                    elif column_number == 1:

                        catebox = CustomQCB()

                        catebox.addItems(cate)
                        catebox.setCurrentText(str(data))
                        self.tableWidget.setCellWidget(
                            row_number, column_number, catebox
                        )
                    else:
                        datebox = QDateEdit()
                        date = QDate()
                        try:
                            yy = int(data.split('/')[0])
                            mm = int(data.split('/')[1])
                            dd = int(data.split('/')[2])
                        except:
                            yy = int(data.split('-')[0])
                            mm = int(data.split('-')[1])
                            dd = int(data.split('-')[2])
                        date.setDate(yy, mm, dd)
                        datebox.setDate(date)

                        datebox.setMinimumDate(self.min_date)
                        datebox.setMaximumDate(self.max_date)
                        datebox.setCalendarPopup(True)

                        self.tableWidget.setCellWidget(
                            row_number, column_number, datebox
                        )

                else:
                    self.tableWidget.setItem(
                        row_number, column_number, QTableWidgetItem(str(data))
                    )

    # Retrive Data from DB
    def GetRow(self):

        person = Storage('Person', self.person_dialog)
        cate = Storage('Category', self.cate_dialog)
        record = Storage('BillRecord', savelist=None,
                         select_period=self.select_period)

        record1 = record.Record_Ui()

        person1 = person.Selec_Ui()
        cate1 = cate.Selec_Ui()

        self.ListRow(record1, person1, cate1)

    # Add New Row
    def AddRow(self):
        # Set up New Row with Combobox and DateBox
        person = Storage('Person', self.person_dialog)
        cate = Storage('Category', self.cate_dialog)
        cate1 = cate.Selec_Ui()
        person1 = person.Selec_Ui()
        newrow = self.tableWidget.rowCount() + 1
        self.tableWidget.setRowCount(newrow)
        combobox1 = QComboBox()
        combobox1.addItems(person1)
        combobox2 = QComboBox()
        combobox2.addItems(cate1)
        datebox = QDateEdit()
        datebox.setMinimumDate(self.min_date)
        datebox.setMaximumDate(self.max_date)
        datebox.setCalendarPopup(True)
        # Loop with ['Name','Cate','Date','Spend','Description']
        for i in range(5):
            if i == 0:
                self.tableWidget.setCellWidget(newrow-1, i, combobox1)
            elif i == 1:
                self.tableWidget.setCellWidget(newrow-1, i, combobox2)
            elif i == 2:
                self.tableWidget.setCellWidget(newrow-1, i, datebox)

            else:
                self.tableWidget.setItem(newrow, i, QTableWidgetItem(""))

    def DelRow(self):
        selected = self.tableWidget.currentRow()
        self.tableWidget.removeRow(selected)

    def SaveChange(self):
        rows = self.tableWidget.rowCount()
        new_list = []
        try:
            for row in range(0, rows):
                row_item = []
                for i in range(5):
                    if i < 2:
                        item = self.tableWidget.cellWidget(row, i)
                        item = item.currentText()
                    elif i == 2:
                        item = self.tableWidget.cellWidget(row, i)
                        item = item.text()
                    elif i == 3:
                        item = self.tableWidget.item(row, i).text()
                        item = float(item)

                    else:
                        item = self.tableWidget.item(row, i)
                        if item is not None:
                            item = item.text()
                        else:
                            item = ''
                    row_item.append(item)
                new_list.append(row_item)
        except ValueError:

            msg = "Cost can only be Integer or Float!"
            errorshow = ErrShow(msg)
            errorshow.exec_()

        else:
            record = Storage('BillRecord', new_list, self.select_period)
            record1 = record.Record_DB()
            msg = "Sucessfully Saved !"
            s = SuShow(msg)
            s.exec_()


class ErrShow(QDialog, Ui_ErrorMsg):
    def __init__(self, ErrMsg):

        super(ErrShow, self).__init__()
        self.setupUi(self)
        self.ErrorShow.setText(ErrMsg)
        self.setWindowTitle('Error')
        self.ErrorShow.setAlignment(Qt.AlignCenter)
        self.show()


class SuShow(QDialog, Ui_SucessMsg):
    def __init__(self, SuMsg):

        super(SuShow, self).__init__()
        self.setupUi(self)
        self.SucessShow.setText(SuMsg)
        self.setWindowTitle('Sucess')
        self.show()


class NewStorage(QDialog, Ui_NewStorage):
    def __init__(self, parent=None):
        super(NewStorage, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Choose Storage")
        self.Save.clicked.connect(self.SaveConfig)
        self.cancel.clicked.connect(self.Cancel)
        self.db_button_open.clicked.connect(self.ChooseDB)
        self.db_button_new.clicked.connect(self.CreateDB)

    def CreateDB(self):
        creator = QFileDialog()
        filename = creator.getSaveFileName(
            filter="*.db *.sqlite *.sqlite3 *.db3")
        self.sql_filename.setText(filename[0])

    def ChooseDB(self):
        select = QFileDialog()
        filename = select.getOpenFileName(
            filter="*.db *.sqlite *.sqlite3 *.db3")
        self.sql_filename.setText(filename[0])

    def GetConfig(self):
        sql_filename = ''
        mongo_ip = ''
        mongo_uname = ''
        mongo_pass = ''
        mongo_dbname = ''
        err = False
        if (self.sqlite.isChecked()):
            RecordType = "sqlite"
            sql_filename = self.sql_filename.text()

            if len(sql_filename) == 0:
                self.box = self.Sql_err1
                self.ShowError()
                err = True
            else:
                self.box = self.Sql_err0
                self.CleanError()

            if err != True:
                try:
                    conn = sqlite3.connect(sql_filename)
                    cur = conn.cursor()
                    person = '''CREATE TABLE "Person" (
            "person_id"	INTEGER NOT NULL UNIQUE,
            "person_name"	TEXT NOT NULL,
            PRIMARY KEY("person_id" AUTOINCREMENT)
        )'''
                    cate = '''CREATE TABLE "Category" (
        "cate_id"	INTEGER NOT NULL UNIQUE,
        "cate_name"	TEXT NOT NULL,
        PRIMARY KEY("cate_id" AUTOINCREMENT)
    )'''
                    owe = '''CREATE TABLE "OweRecord" (
        "owe_id"	INTEGER NOT NULL UNIQUE,
        "Name"	TEXT NOT NULL,
        "Cate"	TEXT NOT NULL,
        "Date"	TEXT NOT NULL,
        "Spend"	TEXT NOT NULL,
        "Description"	TEXT,
        "Period"	TEXT NOT NULL,
        PRIMARY KEY("owe_id" AUTOINCREMENT)
    )'''
                    bill = '''CREATE TABLE "BillRecord" (
        "bill_id"	INTEGER NOT NULL UNIQUE,
        "Name"	TEXT NOT NULL,
        "Cate"	TEXT NOT NULL,
        "Date"	INTEGER NOT NULL,
        "Spend"	TEXT NOT NULL,
        "Description"	TEXT,
        "Period"	TEXT NOT NULL,
        PRIMARY KEY("bill_id" AUTOINCREMENT)
    )'''
                    cur.execute(person)
                    cur.execute(cate)
                    cur.execute(owe)
                    cur.execute(bill)
                except:
                    pass
        else:
            RecordType = "mongo"
            mongo_ip = self.mongo_ip.text()
            mongo_uname = self.mongo_username.text()
            mongo_pass = self.mongo_password.text()
            mongo_dbname = self.mongo_dbname.text()
            checklist = [mongo_ip, mongo_dbname]
            boxlist = [self.Mongo_err0, self.Mongo_err1]
            b = 0
            for item in checklist:
                if len(item) == 0:
                    self.box = boxlist[b]
                    self.ShowError()
                    err = True
                else:
                    self.box = boxlist[b]
                    self.CleanError()
                b += 1
        if err != True:
            data = {}
            data['RecordType'] = RecordType
            data['sqlite'] = {
                "FileName": sql_filename
            }
            data['mongo'] = {
                "DBName": mongo_dbname,
                "ServerIP": mongo_ip,
                "Username": mongo_uname,
                "Password": mongo_pass
            }
            saveconfig = Conf(data)
            result = saveconfig.Save_config()
            return result
        else:
            return False

    def ShowError(self):
        self.box.setText('*Filed Cannot Be Empty')
        self.box.setStyleSheet("color : red")

    def CleanError(self):
        self.box.setText('')

    def SaveConfig(self):
        result = self.GetConfig()
        if result:
            self.close()
            self.accept()

    def Cancel(self):
        self.close()
        self.reject()


class TryConnect:
    def __init__(self, DBname, fname_ip, username=None, password=None):
        self.dbname = DBname
        self.fnameorip = fname_ip
        self.username = username
        self.password = password

    def connect_mongo(self):
        try:
            mongo_client = MongoClient(self.fnameorip, 27017)
            dbnames = mongo_client.database_names()
            if self.dbname in dbnames:
                return True
            else:
                return False
        except:
            return False

    def connect_sqlite(self):
        try:

            sqlite3.connect(self.fnameorip)
            return True
        except:
            return False


def main():
    app = QApplication(sys.argv)
    i = 1
    while i == 1:
        confdata = Conf()
        is_exist = confdata.Check_file()
        if is_exist:
            data = confdata.Get_config()
            storageT = data['RecordType']
            try:
                if storageT == "sqlite":
                    testconnect = TryConnect('', data['sqlite']['FileName'])
                    result = testconnect.connect_sqlite()
                    if result:
                        myWin = MyMainForm()
                        myWin.show()
                        i = 0
                    else:
                        x = ErrShow(
                            'Something wrong with the open sqlite Database File')
                        x.exec_()
                elif storageT == "mongo":
                    testconnect = TryConnect(data['mongo']['DBName'], data['mongo']
                                             ['ServerIP'], data['mongo']['Username'], data['mongo']['Password'])
                    result = testconnect.connect_mongo()
                    if result:
                        myWin = MyMainForm()
                        myWin.show()
                        i = 0
                    else:
                        x = ErrShow(
                            'Something wrong with the mongo connection')
                        x.exec_()

                else:
                    x = ErrShow('configuration FIle Wrong')
                    x.exec_()

                    newstorage = NewStorage()
                    newstorage.show()
                    i = newstorage.exec_()

            except Exception as e:
                err = str(e)
                x = ErrShow(err)
                x.show()
                newstorage = NewStorage()
                newstorage.show()
                i = newstorage.exec_()
        else:

            newstorage = NewStorage()
            newstorage.show()
            i = newstorage.exec_()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
