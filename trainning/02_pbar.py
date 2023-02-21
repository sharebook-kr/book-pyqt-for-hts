import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ProgressBarUpdater(QThread):
    progressBarValue = pyqtSignal(int)

    def run(self):
        value: int = 0
        while value <= 100:
            time.sleep(0.5)
            self.progressBarValue.emit(value)
            value += 5

def main():
    app = QApplication([])
    pbar = QProgressBar()
    pbar.setMinimum(0)
    pbar.setMaximum(100)
    pbar.show()

    @pyqtSlot(int)
    def progressbar_update(value: int):
        pbar.setValue(value)

    progressBarUpdater = ProgressBarUpdater()
    progressBarUpdater.progressBarValue.connect(progressbar_update)
    progressBarUpdater.start()

    app.exec_()

if __name__ == "__main__":
    main()