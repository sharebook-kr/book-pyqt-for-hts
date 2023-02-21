# PyStock
# OrderBookWidget
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import random


class OrderBookWidget(QTableWidget):
    def __init__(self, width=300, depth=10):
        super().__init__()

        self.depth = depth

        self.resize(width, 0)
        self.setColumnCount(3)
        self.setRowCount(depth)

        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)

        self.setColumnWidth(0, int(self.width() * 0.4))
        self.setColumnWidth(1, int(self.width() * 0.2))
        self.setColumnWidth(2, int(self.width() * 0.4))

    def setPriceQuantity(self, index, price, quantity):
        # price
        ask_index = self.depth-index-1
        item = QTableWidgetItem(format(price, ","))
        item.setTextAlignment(int(Qt.AlignRight|Qt.AlignVCenter))
        self.setItem(ask_index, 1, item)

        # quantity
        widget = QWidget()
        layout = QVBoxLayout(widget)

        pbar = QProgressBar()
        pbar.setFixedHeight(20)
        pbar.setInvertedAppearance(True)
        pbar.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        pbar.setStyleSheet("""
            QProgressBar {background-color : rgba(0, 0, 0, 0%);border : 1}
            QProgressBar::Chunk {background-color : rgba(0, 0, 255, 20%);border : 1}
        """)

        layout.addWidget(pbar)
        layout.setAlignment(Qt.AlignVCenter)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setCellWidget(ask_index, 0, widget)

        # set data
        pbar.setRange(0, 200)
        pbar.setFormat(str(quantity))
        pbar.setValue(quantity)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 200, 320, 340)

        # orderbook widget
        self.orderbook = OrderBookWidget(width=300)
        self.set_orderbook()

        # vbox
        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(self.orderbook)

        widget = QWidget()
        widget.setLayout(vbox_layout)
        self.setCentralWidget(widget)

    def set_orderbook(self):
        for i in range(0, 10):
            price = 10000 + i * 100
            quantity = random.randint(1, 200)
            self.orderbook.setPriceQuantity(i, price, quantity)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()