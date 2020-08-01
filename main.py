import sys
from time import strftime
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QComboBox,
    QLineEdit,
    QInputDialog,
)

from PyQt5 import QtCore
from datetime import datetime
from mongo import Mongo
from View.PyBill import Ui_MainWindow
from View.dialog_edit import Ui_Dialog


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


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        # Init Title
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
        self.currentm_index = self.month.index(current_month)
        self.month_index = self.currentm_index
        self.selectedYear = int(current_year)
        self.current_period = self.SetTitle()
        # Init Display
        self.GetRow()

        self.NextMonth.clicked.connect(self.monthChangeNext)
        self.PreviousMonth.clicked.connect(self.monthChangePrevious)
        self.addRow.clicked.connect(self.AddRow)
        self.delRow.clicked.connect(self.DelRow)
        self.save_change.clicked.connect(self.SaveChange)

        self.edit_person.clicked.connect(self.person_window)
        self.edit_cate.clicked.connect(self.cate_window)

        # Exit Program
        self.exit.clicked.connect(self.close)

    def SetTitle(self):

        selectedMonth = self.month[self.month_index]
        selectedYear = str(self.selectedYear)
        self.Month.setText(selectedMonth + "/" + selectedYear)
        self.Month.setAlignment(QtCore.Qt.AlignCenter)
        return selectedMonth + "/" + selectedYear

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
        self.dialog = EditDialog("Person")
        self.dialog.show()

    def cate_window(self):
        self.dialog = EditDialog("Category")
        self.dialog.show()

    # Display Data into list view
    def ListRow(self, data, person, cate):
        rowcount = len(data)
        self.tableWidget.setRowCount(rowcount)
        self.tableWidget.setColumnCount(5)

        for row_number, row_data in enumerate(data):
            for column_number, data in enumerate(row_data):
                if column_number < 2:
                    if column_number == 0:
                        personbox = QComboBox()
                        personbox.addItems(person)
                        personbox.setCurrentText(str(data))
                        self.tableWidget.setCellWidget(
                            row_number, column_number, personbox
                        )
                    else:

                        catebox = QComboBox()
                        catebox.addItems(cate)
                        catebox.setCurrentText(str(data))
                        personbox.setObjectName("cate" + str(row_number))
                        self.tableWidget.setCellWidget(
                            row_number, column_number, catebox
                        )

                else:
                    self.tableWidget.setItem(
                        row_number, column_number, QTableWidgetItem(str(data))
                    )

    # Retrive Data from DB
    def GetRow(self):
        person = ("Tobin", "Iris")
        cate = ("Shopping", "Eating", "Other")
        data = [
            ["Tobin", "Shopping", "2020/05/11", "148", "costco"],
            ["Tobin", "Shopping", "2020/05/12", "148", "costco"],
            ["Tobin", "Shopping", "2020/05/13", "148", "costco"],
            ["Tobin", "Eating", "2020/05/14", "148", "costco"],
            ["Tobin", "Shopping", "2020/05/15", "148", "costco"],
            ["Tobin", "Shopping", "2020/05/16", "148", "costco"],
            ["Iris", "Shopping", "2020/05/17", "148", "costco"],
            ["Tobin", "Shopping", "2020/05/18", "148", "costco"],
            ["Tobin", "Shopping", "2020/05/19", "148", "costco"],
            ["Iris", "Shopping", "2020/05/20", "148", "costco"],
            ["Tobin", "Shopping", "2020/05/21", "148", "costco"],
            ["Tobin", "Shopping", "2020/05/22", "148", "costco"],
        ]
        self.ListRow(data, person, cate)

    # Add New Row
    def AddRow(self):
        newrow = self.tableWidget.rowCount() + 1
        self.tableWidget.setRowCount(newrow)
        person = ("Tobin", "Iris")
        combobox = QComboBox()
        combobox.addItems(person)

        for i in range(5):
            # self.tableWidget.setItem(newrow, i, QTableWidgetItem(""))
            self.tableWidget.setCellWidget(newrow, i, combobox)

    def DelRow(self):
        selected = self.tableWidget.currentRow()
        self.tableWidget.removeRow(selected)

    def SaveChange(self):
        rows = self.tableWidget.rowCount()
        new_list = []
        for row in range(0, rows):
            row_item = []
            for i in range(5):
                if i < 2:
                    item = self.tableWidget.cellWidget(row, i)
                    item = item.currentText()
                else:
                    item = self.tableWidget.item(row, i).text()
                row_item.append(item)
            new_list.append(row_item)

    # def DiscardChange(self):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
