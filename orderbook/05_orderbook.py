# PyStock
# OrderBookWidget
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
import random
import time


class OrderBookWidget(QTableWidget):
    def __init__(self, width=300, depth=10, max_quantity=1000):
        super().__init__()

        self.depth = depth
        self.total_depth = depth * 2
        self.default_max_quantity = max_quantity
        self.max_quantity = 0
        self.animation_list = []

        self.resize(width, 0)
        self.setColumnCount(3)
        self.setRowCount(self.total_depth)

        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)

        self.setColumnWidth(0, int(self.width() * 0.4))
        self.setColumnWidth(1, int(self.width() * 0.2))
        self.setColumnWidth(2, int(self.width() * 0.4))

        self.init_table_widget_items()

    def init_table_widget_items(self):
        for side in range(2):       # side(0): ask, side(1): bid
            for i in range(self.depth):
                # price
                pos = side * self.depth + i
                item = QTableWidgetItem("")
                item.setTextAlignment(int(Qt.AlignRight|Qt.AlignVCenter))
                self.setItem(pos, 1, item)

                # quantity
                widget = QWidget()
                layout = QVBoxLayout(widget)

                pbar = QProgressBar()
                pbar.setFixedHeight(20)
                if side == 0:
                    pbar.setInvertedAppearance(True)
                pbar.setAlignment(Qt.AlignRight|Qt.AlignVCenter)

                if side == 0:
                    pbar.setStyleSheet("""
                        QProgressBar {background-color : rgba(0, 0, 0, 0%);border : 1}
                        QProgressBar::Chunk {background-color : rgba(0, 0, 255, 20%);border : 1}
                    """)
                else:
                    pbar.setStyleSheet("""
                        QProgressBar {background-color : rgba(0, 0, 0, 0%);border : 1}
                        QProgressBar::Chunk {background-color : rgba(255, 0, 0, 20%);border : 1}
                    """)

                layout.addWidget(pbar)
                layout.setAlignment(Qt.AlignVCenter)
                layout.setContentsMargins(0, 0, 0, 0)

                col_index = 0 if side == 0 else 2
                self.setCellWidget(pos, col_index, widget)

                # animation
                ani = QPropertyAnimation(pbar, b"value")
                ani.setDuration(100)
                ani.setStartValue(0)
                self.animation_list.append(ani)

    def setPriceQuantity(self, side, index, price, quantity):
        # price
        # [ 0] ask10
        # [ 1] ask9
        # [  ] ...
        # [ 9] ask1
        # [  ] ----
        # [10] bid1
        # [11] bid2
        # [ . ] ...
        # [19] bid10
        if side == 0:
            index2 = self.depth - index - 1
        else:
            index2 = self.depth + index

        price_item = self.item(index2, 1)
        price_item.setText(f"{price:,}")

        # quantitty
        col_index = 0 if side == 0 else 2
        widget = self.cellWidget(index2, col_index)

        vbox = widget.findChildren(QVBoxLayout)[0]
        bar = vbox.itemAt(0).widget()
        max_quantity = self.max_quantity if self.max_quantity > 0 else self.default_max_quantity
        bar.setRange(0, int(max_quantity * 1.1))
        bar.setFormat(f"{quantity:,}")

        #
        self.animation_list[index2].stop()
        self.animation_list[index2].setStartValue(bar.value())
        self.animation_list[index2].setEndValue(int(quantity))
        self.animation_list[index2].start()

        # update max quantity
        if quantity > self.max_quantity:
            self.max_quantity = quantity

class DataFeeder(QThread):
    updated = pyqtSignal(int, int, int, int)

    def run(self):
        while True:
            side = random.randint(0, 1)
            quantity = random.randint(1, 10000)
            index = random.randint(0, 9)
            prices = range(9000, 11000, 100)

            if side == 0: # ask
                index2 = 10 + index
            else:         # bid
                index2 = 10 - index - 1

            price = prices[index2]
            self.updated.emit(side, index, price, quantity)
            time.sleep(0.05)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OrderBookWidget")
        self.setGeometry(800, 200, 340, 680)

        # orderbook widget
        self.orderbook = OrderBookWidget(width=300)

        # vbox
        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(self.orderbook)

        widget = QWidget()
        widget.setLayout(vbox_layout)
        self.setCentralWidget(widget)

        # thread
        self.feeder = DataFeeder()
        self.feeder.updated.connect(self.update_orderbook)
        self.feeder.start()

    @pyqtSlot(int, int, int, int)
    def update_orderbook(self, side, index, price, quantity):
        self.orderbook.setPriceQuantity(side, index, price, quantity)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()