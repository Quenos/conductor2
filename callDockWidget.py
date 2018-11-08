import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore

from demoDockWidget import *

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtCore.Qt.darkGreen)
        self.setPalette(palette)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())