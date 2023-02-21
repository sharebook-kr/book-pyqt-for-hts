import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

title = [
    "Task Name",
    "detail",
    "progress",
]

class TableWindow(QWidget):

    def __init__(self, parent=None):
        super(TableWindow, self).__init__(parent)
        self.colcnt = len(title)
        self.rowcnt = 0
        self.tablewidget = QTableWidget(self.rowcnt, self.colcnt)
        self.progress_bar = []
        self.action_button = []

        vheader = QHeaderView(Qt.Orientation.Vertical)
        #vheader.setResizeMode(QHeaderView.ResizeToContents)
        self.tablewidget.setVerticalHeader(vheader)

        hheader = QHeaderView(Qt.Orientation.Horizontal)
        #hheader.setResizeMode(QHeaderView.ResizeToContents)
        self.tablewidget.setHorizontalHeader(hheader)
        self.tablewidget.setHorizontalHeaderLabels(title)

        self.random_button = QPushButton('&Add Task', self)
        self.add_button = QPushButton('&Add Progress Value', self)

        layout = QVBoxLayout()
        layout.addWidget(self.tablewidget)
        layout.addWidget(self.random_button)
        layout.addWidget(self.add_button)
        self.setLayout(layout)

        # event handling
        self.random_button.clicked.connect(self.random_click)
        self.add_button.clicked.connect(self.add_click)

    def random_click(self):
        # add row
        rowPosition = self.tablewidget.rowCount()
        self.tablewidget.insertRow(rowPosition)

        # dummy example
        self.tablewidget.setItem(rowPosition, 0, QTableWidgetItem('Random Task'))
        self.tablewidget.setItem(rowPosition, 1, QTableWidgetItem('calculating task..'))

        self.progress_bar.append(QProgressBar())
        self.tablewidget.setCellWidget(rowPosition, 2, self.progress_bar[rowPosition])


    def add_click(self):
        for progress_bar in self.progress_bar:
            progress_bar.setValue(progress_bar.value() + 10)

def main():
    app = QApplication(sys.argv)
    widget = TableWindow()
    widget.show()
    widget.raise_()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()