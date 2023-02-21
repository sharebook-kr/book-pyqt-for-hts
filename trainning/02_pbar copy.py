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

class ProgressBar(QProgressBar):
    def update_value(self, value, animated=True):
        if animated:
            if hasattr(self, "animation"):
                self.animation.stop()
            else:
                self.animation = QPropertyAnimation(
                    targetObject=self, propertyName=b"value"
                )
                self.animation.setDuration(100)
            self.animation.setStartValue(self.value())
            self.animation.setEndValue(value)
            print(self.value(), value)
            self.animation.start()
        else:
            self.setValue(value)

def main():
    app = QApplication([])
    pbar = ProgressBar()
    pbar.setMinimum(0)
    pbar.setMaximum(100)
    pbar.show()

    progressBarUpdater = ProgressBarUpdater()
    progressBarUpdater.progressBarValue.connect(pbar.update_value)
    progressBarUpdater.start()

    app.exec_()

if __name__ == "__main__":
    main()