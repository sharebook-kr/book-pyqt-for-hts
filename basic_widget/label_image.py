import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        layout = QVBoxLayout(widget)

        # image
        label_img = QLabel()
        label_img.setPixmap(QPixmap('python-logo.png'))

        layout.addWidget(label_img)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()