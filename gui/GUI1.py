from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Table import Tableview
from utils.common import readTable
import sys
class GUI1MainWindow(QWidget):
    def __init__(self):
        super(GUI1MainWindow,self).__init__()
        self.setObjectName("主窗口")
        self.setWindowTitle("check1")
        self.resize(700,600)
        self.tableView = Tableview(self)
        self.satrtButton = QtWidgets.QPushButton()
        self.satrtButton.clicked.connect(readTable)
        vlayout = QVBoxLayout(self)
        vlayout.addWidget(self.tableView)
        vlayout.addWidget(self.satrtButton)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    gui = GUI1MainWindow()
    gui.show()
    sys.exit(app.exec_())