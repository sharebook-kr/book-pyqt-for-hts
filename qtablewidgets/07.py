import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")

        label = QLabel("금리환율")
        # horizontal line
        hor_line = QFrame()
        hor_line.setFrameShape(QFrame.HLine)
        hor_line.setFrameShadow(QFrame.Sunken)

        widget = QWidget()
        vert_layout = QVBoxLayout(widget)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnWidth(1, 40)
        self.tableWidget.setRowCount(5)

        self.tableWidget.verticalHeader().setDefaultSectionSize(20)

        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalScrollBar().setDisabled(True)
        self.tableWidget.horizontalScrollBar().setDisabled(True)
        self.tableWidget.setStyleSheet("gridline-color: white; border: 0px solid;")

        self.tableWidget.setItem(0, 0, QTableWidgetItem("국고채3년"))
        item = QTableWidgetItem("3.18")
        item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        item.setForeground(QBrush(QColor(0, 0, 255)))
        self.tableWidget.setItem(0, 1, item)

        # icon
        icon = QIcon("down.png")
        item = QTableWidgetItem()
        item.setIcon(icon)
        self.tableWidget.setItem(0, 2, item)

        self.tableWidget.setItem(1, 0, QTableWidgetItem("회사채3년"))

        # icon
        icon = QIcon("down.png")
        item = QTableWidgetItem()
        item.setIcon(icon)
        self.tableWidget.setItem(1, 2, item)

        item = QTableWidgetItem("4.17")
        item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        item.setForeground(QBrush(QColor(0, 0, 255)))
        self.tableWidget.setItem(1, 1, item)

        # layout
        vert_layout.addWidget(label)
        vert_layout.addWidget(hor_line)
        vert_layout.addWidget(self.tableWidget)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()