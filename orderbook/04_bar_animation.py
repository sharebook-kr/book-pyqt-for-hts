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
        self.default_max_quantity = max_quantity
        self.max_quantity = 0
        self.animation_list = []

        self.resize(width, 0)
        self.setColumnCount(3)
        self.setRowCount(depth)

        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)

        self.setColumnWidth(0, int(self.width() * 0.4))
        self.setColumnWidth(1, int(self.width() * 0.2))
        self.setColumnWidth(2, int(self.width() * 0.4))

        self.init_table_widget_items()

    def init_table_widget_items(self):
        for i in range(self.depth):
            # price
            item = QTableWidgetItem("")
            item.setTextAlignment(int(Qt.AlignRight|Qt.AlignVCenter))
            self.setItem(i, 1, item)

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
            self.setCellWidget(i, 0, widget)

            # animation
            ani = QPropertyAnimation(pbar, b"value")
            ani.setDuration(100)
            ani.setStartValue(0)
            self.animation_list.append(ani)

    def setPriceQuantity(self, index, price, quantity):
        # price
        ask_index = self.depth - index - 1
        price_item = self.item(ask_index, 1)
        price_item.setText(f"{price:,}")

        # quantitty
        widget = self.cellWidget(ask_index, 0)
        vbox = widget.findChildren(QVBoxLayout)[0]
        bar = vbox.itemAt(0).widget()
        max_quantity = self.max_quantity if self.max_quantity > 0 else self.default_max_quantity
        bar.setRange(0, int(max_quantity * 1.1))
        bar.setFormat(f"{quantity:,}")

        self.animation_list[ask_index].stop()
        self.animation_list[ask_index].setStartValue(bar.value())
        self.animation_list[ask_index].setEndValue(int(quantity))
        self.animation_list[ask_index].start()

        # update max quantity
        if quantity > self.max_quantity:
            self.max_quantity = quantity

class DataFeeder(QThread):
    updated = pyqtSignal(int, int, int)

    def run(self):
        while True:
            quantity = random.randint(1, 10000)
            index = random.randint(0, 9)
            prices = range(10000, 11000, 100)
            price = prices[index]

            self.updated.emit(index, price, quantity)
            time.sleep(0.1)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 200, 320, 340)

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

    @pyqtSlot(int, int, int)
    def update_orderbook(self, pos, price, quantity):
        self.orderbook.setPriceQuantity(pos, price, quantity)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()