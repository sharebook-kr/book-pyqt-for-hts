import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        layout = QVBoxLayout(widget)

        # image
        label_img = QLabel()
        label_img.setPixmap(QPixmap())

        layout.addWidget(btn)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()