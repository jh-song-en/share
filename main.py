import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from sub_form import sub_form

class main_form(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        # Setting the position and size of the UI
        self.ui = uic.loadUi(os.path.abspath('sample.ui'), self)
        self.ui.show()
        # Search tab
    @pyqtSlot()
    def browse(self):
        self.foo = sub_form()


    def closeEvent(self, event):
        print("closed")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_form()

    sys.exit(app.exec())