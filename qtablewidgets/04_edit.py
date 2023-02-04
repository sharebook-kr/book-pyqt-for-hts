import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 200, 300, 300)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.resize(290, 290)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(5)
        column_labels = ["종목명", "현재가"]
        self.tableWidget.setHorizontalHeaderLabels(column_labels)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("삼성전자"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("63,900"))

        self.tableWidget.setItem(1, 0, QTableWidgetItem("SK하이닉스"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("92,100"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()