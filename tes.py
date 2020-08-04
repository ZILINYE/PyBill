from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt




class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQtChart Pie Chart")
        self.setGeometry(100,100, 1280,600)
        self.series = QPieSeries()
        self.show()

        self.create_piechart()
    def test(self,index):
        self.series.slices()[index].setExploded(True) 


    def create_piechart(self):

        self.series = QPieSeries()
        self.series.append("Python", 100)
        self.series.append("C++", 70)
        self.series.append("Java", 150)
        self.series.append("C#", 40)
        self.series.append("PHP", 30)
        self.series.setLabelsVisible(True)
        # series.slices()[1].doubleClicked.connect(self.test)
        for item in self.series.slices():
            index = self.series.slices().index(item)
            item.doubleClicked.connect(lambda : self.test(index))


        # #adding slice
        # slice = QPieSlice()
        # slice = series.slices()[1]
        # # slice.setExploded(True)
        # slice.setLabelVisible(True)
        # slice.setPen(QPen(Qt.darkGreen, 2))
        # slice.setBrush(Qt.green)
    




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

        self.setCentralWidget(chartview)





App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())