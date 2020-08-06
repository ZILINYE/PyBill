import sys
from time import strftime
import calendar
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QComboBox,
    QLineEdit,
    QInputDialog,
    QDateEdit,
    QDateTimeEdit,

)
from PyQt5.QtCore import QDateTime,QDate
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from datetime import datetime
from mongo import Mongo
from View.PyBill import Ui_MainWindow
from View.dialog_edit import Ui_Dialog
from View.addowe import Add_owe
from View.Report import Report_Ui
from View.ErrorDisplay import ErrorMsg
from calculate import Calculator

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
        connection = Mongo("pybill", self.dialog_title)
        data = connection.selectionUi()
        self.listWidget.addItems(data)

    def AddPerson(self):
        row = self.listWidget.currentRow()
        text, ok = QInputDialog.getText(self, "Person Dialog", "Enter Person Name")

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

        connection = Mongo("pybill", self.dialog_title, save_list)
        data = connection.selectionMongo()
        self.close()

class EditOweDialog(QMainWindow,Add_owe):
    def __init__(self,person_list,year,month,month_index,max_date,min_date):
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
            elif i ==1:
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

        record = Mongo("pybill", 'OweRecord',new_list,self.select_period)
        record1 = record.recordMongo()
        self.close()

    def GetOwe(self):
        connection = self.MongoConnect()
        data = connection.recordUi()
        rowcount = len(data)
        self.tableWidget1.setRowCount(rowcount)
        self.tableWidget1.setColumnCount(5)
        for row_number, row_data in enumerate(data):
            for column_number, data in enumerate(row_data):
                if column_number < 3:
                    if column_number < 2 :
                        personbox = QComboBox()
                        personbox.addItems(self.person_list)
                        personbox.setCurrentText(str(data))
                        self.tableWidget1.setCellWidget(
                            row_number, column_number, personbox
                        )
                    else:
                        datebox = QDateEdit()
                        date = QDate()
                        yy = int(data.split('/')[0])
                        mm = int(data.split('/')[1])
                        dd = int(data.split('/')[2])
                        date.setDate(yy,mm,dd)
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
        
        connection = Mongo("pybill","OweRecord",savelist=None,select_period=self.select_period)
        return connection

class Report(QMainWindow,Report_Ui):
    def __init__(self, total_cost, avageCost,SpendByPerson,SpendByCate,SolutionList):
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
        self.averageSpend.setText(str(self.avageCost ))
    def SetTable(self):
        rowcount = len(self.SpendByPerson)
        self.table2Widget.setRowCount(rowcount)
        self.table2Widget.setColumnCount(2)

        for i in range(rowcount):
            name = list(self.SpendByPerson.keys())[i]
            cost = list(self.SpendByPerson.values())[i]
            self.table2Widget.setItem(i,0,QTableWidgetItem(str(name)))
            self.table2Widget.setItem(i,1,QTableWidgetItem(str(cost)))
        self.list2Widget.addItems(self.SolutionList)
    def SetChart(self):
        for key,value in self.SpendByCate.items():
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
        self.save_change.clicked.connect(self.SaveChange)
        self.Calculate.clicked.connect(self.GetReport)
        self.edit_person.clicked.connect(self.person_window)
        self.edit_cate.clicked.connect(self.cate_window)
        self.edit_owe.clicked.connect(self.owe_window)

        # Exit Program
        self.exit.clicked.connect(self.close)
    def GetReport(self):
        x = Calculator(self.select_period)
        
        total_cost,avagcost,allpersonCost,cateCost,solutionList = x.returnData()


        # print(total_cost,avagcost,allpersonCost,cateCost,solutionList )
        self.dialog = Report(total_cost,avagcost,allpersonCost,cateCost,solutionList )
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
        person = Mongo("pybill", self.person_dialog)
        person1 = person.selectionUi()
        self.dialog = EditOweDialog(person1,self.selectedYear,self.month[self.month_index],self.month_index,self.max_date,self.min_date)
        self.dialog.show()
   
    def Cal_month(self):
        year = self.selectedYear
        mon = self.month_index + 1
        max_day = calendar.monthrange(year,mon)[1]
        self.min_date = QDate()
        self.min_date.setDate(year,mon,1)
        self.max_date = QDate()
        self.max_date.setDate(year,mon,max_day)


    # Display Data into list view
    def ListRow(self, data, person, cate):
        rowcount = len(data)
        self.tableWidget.setRowCount(rowcount)
        self.tableWidget.setColumnCount(5)

        for row_number, row_data in enumerate(data):
            for column_number, data in enumerate(row_data):
                if column_number < 3:
                    if column_number == 0:
                        personbox = QComboBox()
                        personbox.addItems(person)
                        personbox.setCurrentText(str(data))
                        self.tableWidget.setCellWidget(
                            row_number, column_number, personbox
                        )
                    elif column_number == 1 :

                        catebox = QComboBox()
                        catebox.addItems(cate)
                        catebox.setCurrentText(str(data))
                        self.tableWidget.setCellWidget(
                            row_number, column_number, catebox
                        )
                    else:
                        datebox = QDateEdit()
                        date = QDate()
                        yy = int(data.split('/')[0])
                        mm = int(data.split('/')[1])
                        dd = int(data.split('/')[2])
                        date.setDate(yy,mm,dd)
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
        person = Mongo("pybill", self.person_dialog)
        cate = Mongo("pybill", self.cate_dialog)
        record = Mongo("pybill", 'BillRecord',savelist=None,select_period = self.select_period)
        record1 = record.recordUi()
        person1 = person.selectionUi()
        cate1 = cate.selectionUi()
        self.ListRow(record1, person1, cate1)

    # Add New Row
    def AddRow(self):
        # Set up New Row with Combobox and DateBox
        person = Mongo("pybill", self.person_dialog)
        cate = Mongo("pybill", self.cate_dialog)
        cate1 = cate.selectionUi()
        person1 = person.selectionUi()
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
            elif i ==1:
                self.tableWidget.setCellWidget(newrow-1, i, combobox2)
            elif i == 2:
                self.tableWidget.setCellWidget(newrow-1, i, datebox)
            # elif i == 3:
            #     item = QTableWidgetItem()
            
            #     self.tableWidget.setItem()
            #     self.tableWidget.setItem(newrow, i, item)
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
            self.dialog = ErrShow(msg)
            self.dialog.show()
        
        else:
            record = Mongo("pybill", 'BillRecord',new_list,self.select_period)
            record1 = record.recordMongo()

    # def DiscardChange(self):

class ErrShow(QMainWindow,ErrorMsg):
    def __init__(self,ErrMsg):
        super(ErrShow, self).__init__()
        self.setupUi(self)
   
        self.ErrorShow.setText(ErrMsg)
        self.setWindowTitle('Error')
        self.ErrorShow.setAlignment(Qt.AlignCenter)



        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
