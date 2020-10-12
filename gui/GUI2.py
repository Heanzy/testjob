from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Table import Tableview
from utils.common import readTable
from core.Controller import run,run1
import sys
class GUI2MainWindow(QWidget):
    start_signal = pyqtSignal(Tableview,dict)
    def __init__(self):
        super(GUI2MainWindow,self).__init__()

        self.setObjectName("主窗口")
        self.setWindowTitle("check2")
        self.resize(700,600)
        #第一行标签
        self.MxLable = QLabel()
        self.MxLable.setText("Mx")
        self.nxLable = QLabel()
        self.nxLable.setText("nx")
        self.PstdLable = QLabel()
        self.PstdLable.setText("Pstd")

        # 第二行标签
        self.MstdLable = QLabel()
        self.MstdLable.setText("Mstd")
        self.nstdLable = QLabel()
        self.nstdLable.setText("nstd")
        self.UcrmLable = QLabel()
        self.UcrmLable.setText("Ucrm")

        #输入行
        self.MxQLine = QLineEdit()
        self.nxQLine = QLineEdit()
        self.PstdQLine = QLineEdit()
        self.MstdQLine = QLineEdit()
        self.nstdQLine = QLineEdit()
        self.UcrmQLine = QLineEdit()


        #第一行布局
        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(self.MxLable)
        hlayout1.addWidget(self.MxQLine)
        hlayout1.addWidget(self.nxLable)
        hlayout1.addWidget(self.nxQLine)
        hlayout1.addWidget(self.PstdLable)
        hlayout1.addWidget(self.PstdQLine)

        #第二行布局
        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(self.MstdLable)
        hlayout2.addWidget(self.MstdQLine)
        hlayout2.addWidget(self.nstdLable)
        hlayout2.addWidget(self.nstdQLine)
        hlayout2.addWidget(self.UcrmLable)
        hlayout2.addWidget(self.UcrmQLine)

        self.tableView = Tableview()

        self.satrtButton = QtWidgets.QPushButton()

        self.secondButton = QtWidgets.QPushButton()

        #MxE分子式标签
        self.MxELabel = QLabel()
        self.MxELabel.setText("Mx分子式")
        self.CLabel = QLabel()
        self.CLabel.setText("C:")
        self.CLine = QLineEdit()

        self.HLabel = QLabel()
        self.HLabel.setText("H:")
        self.HLine = QLineEdit()

        self.OLabel = QLabel()
        self.OLabel.setText("O:")
        self.OLine = QLineEdit()

        self.NLabel = QLabel()
        self.NLabel.setText("N")
        self.NLine = QLineEdit()

        self.SLabel = QLabel()
        self.SLabel.setText("S")
        self.SLine = QLineEdit()

        self.FLabel = QLabel()
        self.FLabel.setText("F")
        self.FLine = QLineEdit()

        self.ClLabel = QLabel()
        self.ClLabel.setText("Cl")
        self.ClLine = QLineEdit()

        self.OtherLabel = QLabel()
        self.OtherLabel.setText("其他")
        self.OtherlLine = QLineEdit()

        # MstdE分子式标签
        self.MstdELabel = QLabel()
        self.MstdELabel.setText("Mstd分子式")

        self.CLabel1 = QLabel()
        self.CLabel1.setText("C")
        self.CLine1 = QLineEdit()

        self.HLabel1 = QLabel()
        self.HLabel1.setText("H")
        self.HLine1 = QLineEdit()

        self.OLabel1 = QLabel()
        self.OLabel1.setText("O")
        self.OLine1 = QLineEdit()

        self.NLabel1 = QLabel()
        self.NLabel1.setText("N")
        self.NLine1 = QLineEdit()

        self.SLabel1 = QLabel()
        self.SLabel1.setText("S")
        self.SLine1 = QLineEdit()

        self.FLabel1 = QLabel()
        self.FLabel1.setText("F")
        self.FLine1 = QLineEdit()

        self.ClLabel1 = QLabel()
        self.ClLabel1.setText("Cl")
        self.ClLine1 = QLineEdit()

        self.OtherLabel1 = QLabel()
        self.OtherLabel1.setText("其他")
        self.OtherlLine1 = QLineEdit()

        hlayout3 = QHBoxLayout()
        hlayout3.addWidget(self.CLabel)
        hlayout3.addWidget(self.CLine)
        hlayout3.addWidget(self.HLabel)
        hlayout3.addWidget(self.HLine)
        hlayout3.addWidget(self.OLabel)
        hlayout3.addWidget(self.OLine)
        hlayout3.addWidget(self.NLabel)
        hlayout3.addWidget(self.NLine)
        hlayout3.addWidget(self.SLabel)
        hlayout3.addWidget(self.SLine)
        hlayout3.addWidget(self.FLabel)
        hlayout3.addWidget(self.FLine)
        hlayout3.addWidget(self.ClLabel)
        hlayout3.addWidget(self.ClLine)
        hlayout3.addWidget(self.OtherLabel)
        hlayout3.addWidget(self.OtherlLine)

        hlayout4 = QHBoxLayout()
        hlayout4.addWidget(self.CLabel1)
        hlayout4.addWidget(self.CLine1)
        hlayout4.addWidget(self.HLabel1)
        hlayout4.addWidget(self.HLine1)
        hlayout4.addWidget(self.OLabel1)
        hlayout4.addWidget(self.OLine1)
        hlayout4.addWidget(self.NLabel1)
        hlayout4.addWidget(self.NLine1)
        hlayout4.addWidget(self.SLabel1)
        hlayout4.addWidget(self.SLine1)
        hlayout4.addWidget(self.FLabel1)
        hlayout4.addWidget(self.FLine1)
        hlayout4.addWidget(self.ClLabel1)
        hlayout4.addWidget(self.ClLine1)
        hlayout4.addWidget(self.OtherLabel1)
        hlayout4.addWidget(self.OtherlLine1)



        self.satrtButton.clicked.connect(self.startSignal)
        self.initSignal()
        self.vlayout = QVBoxLayout()
        self.vlayout.addLayout(hlayout1)
        self.vlayout.addLayout(hlayout2)
        self.vlayout.addWidget(self.tableView)
        self.vlayout.addWidget(self.satrtButton)
        self.vlayout.addWidget(self.MxELabel)
        self.vlayout.addLayout(hlayout3)
        self.vlayout.addWidget(self.MstdELabel)
        self.vlayout.addLayout(hlayout4)
        self.vlayout.addWidget(self.secondButton)
        self.setLayout(self.vlayout)

        self.arg = {}
    def initSignal(self):
        self.start_signal.connect(run1)
    def startSignal(self):
        self.start_signal.emit(self.tableView,self.getarg())

    def getarg(self):
        self.arg["Mx"] = float(self.MxQLine.text()) if self.MxQLine.text() else None
        self.arg["nx"] =float(self.nxQLine.text()) if self.MxQLine.text() else None
        self.arg["Pstd"] = float(self.PstdQLine.text()) if self.MxQLine.text() else None
        self.arg["Mstd"] = float(self.MstdQLine.text()) if self.MxQLine.text() else None
        self.arg["nstd"] = float(self.nstdQLine.text()) if self.MxQLine.text() else None
        self.arg["Ucrm"] = float(self.UcrmQLine.text()) if self.MxQLine.text() else None
        self.arg["MxE"] = None
        self.arg["MstdE"] = None
        return self.arg
    def getyuansu(self):
        pass




if __name__ == "__main__":

    app = QApplication(sys.argv)
    gui = GUI2MainWindow()
    gui.show()
    sys.exit(app.exec_())