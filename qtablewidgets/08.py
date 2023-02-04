import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QTableWidgetIconItem(QWidget):
    def __init__(self, text, text_color, icon_path):
        super().__init__()

        label1 = QLabel(text)
        label1.setStyleSheet(f"color: {text_color};")

        label2 = QLabel()
        label2.setPixmap(QPixmap(f"{icon_path}"))

        hbox_layout = QHBoxLayout(self)
        hbox_layout.addWidget(label1)
        hbox_layout.addWidget(label2)

        hbox_layout.setAlignment(Qt.AlignVCenter)
        hbox_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(hbox_layout)


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
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(5)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.setStyleSheet("gridline-color: white; border: 0px solid;")

        self.tableWidget.setItem(0, 0, QTableWidgetItem("국고채3년"))
        widget2 = QTableWidgetIconItem("3.18", "blue", "down.png")
        self.tableWidget.setCellWidget(0, 1, widget2)

        self.tableWidget.setItem(1, 0, QTableWidgetItem("회사채3년"))
        widget3 = QTableWidgetIconItem("4.17", "blue", "down.png")
        self.tableWidget.setCellWidget(1, 1, widget3)

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