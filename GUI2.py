from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Table import Tableview
from PyQt5.QtGui import *
from utils.common import readTable
from Controller import run1
import sys
from copyAction import selected_tb_text
from common import readYuansu
class GUI2MainWindow(QWidget):
    start_signal = pyqtSignal(Tableview,dict)
    def __init__(self):
        super(GUI2MainWindow,self).__init__()
        self.initSignal()
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
        self.tableView.model.setHorizontalHeaderLabels(["Ix","Istd","mx","mstd"])
        self.satrtButton = QtWidgets.QPushButton()
        self.satrtButton.setText("开始")

        self.secondButton = QtWidgets.QPushButton()

        #天平最小分度
        self.TianPingLabel = QLabel()
        self.TianPingLabel.setText("天平最小分度:")
        self.TianPingLine = QLineEdit()

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

        hlayout5 = QHBoxLayout()
        hlayout5.addWidget(self.TianPingLabel)
        hlayout5.addWidget(self.TianPingLine)

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

        self.vlayout = QVBoxLayout()
        self.vlayout.addLayout(hlayout1)
        self.vlayout.addLayout(hlayout2)
        self.vlayout.addWidget(self.tableView)
        self.vlayout.addWidget(self.satrtButton)
        self.vlayout.addLayout(hlayout5)
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

        self.arg["Mx"] = float(self.MxQLine.text()) if self.MxQLine.text() else 0
        self.arg["nx"] =float(self.nxQLine.text()) if self.nxQLine.text() else 0
        self.arg["Pstd"] = float(self.PstdQLine.text()) if self.PstdQLine.text() else 0
        self.arg["Mstd"] = float(self.MstdQLine.text()) if self.MstdQLine.text() else 0
        self.arg["nstd"] = float(self.nstdQLine.text()) if self.nstdQLine.text() else 0
        self.arg["Ucrm"] = float(self.UcrmQLine.text()) if self.UcrmQLine.text() else 0
        self.arg["TP"] = float(self.TianPingLine.text()) if self.TianPingLine.text() else 0
        self.arg["MxE"],self.arg["MstdE"] = self.getyuansu()
        return self.arg
    def getyuansu(self):
        MxE = {}
        MxE["C"] = int(self.CLine.text()) if self.CLine.text() else 0
        MxE["H"] = int(self.HLine.text()) if self.HLine.text() else 0
        MxE["O"] = int(self.OLine.text()) if self.OLine.text() else 0
        MxE["N"] = int(self.NLine.text()) if self.NLine.text() else 0
        MxE["S"] = int(self.SLine.text()) if self.SLine.text() else 0
        MxE["F"] = int(self.FLine.text()) if self.FLine.text() else 0
        MxE["Cl"] = int(self.ClLine.text()) if self.ClLine.text() else 0
        if self.OtherlLine.text():
            MxE.update(readYuansu(self.OtherlLine.text()))
        MstdE = {}
        MstdE["C"] = int(self.CLine1.text()) if self.CLine1.text() else 0
        MstdE["H"] = int(self.HLine1.text()) if self.HLine1.text() else 0
        MstdE["O"] = int(self.OLine1.text()) if self.OLine1.text() else 0
        MstdE["N"] = int(self.NLine1.text()) if self.NLine1.text() else 0
        MstdE["S"] = int(self.SLine1.text()) if self.SLine1.text() else 0
        MstdE["F"] = int(self.FLine1.text()) if self.FLine1.text() else 0
        MstdE["Cl"] = int(self.ClLine1.text()) if self.ClLine1.text() else 0
        if self.OtherlLine1.text():
            MstdE.update(readYuansu(self.OtherlLine1.text()))
        return MxE,MstdE
    def keyPressEvent(self, event):  # 重写键盘监听事件
        # 监听 CTRL+C 组合键，实现复制数据到粘贴板
        if (event.key() == Qt.Key_C) and QApplication.keyboardModifiers() == Qt.ControlModifier:
            text = selected_tb_text(self.tableView)  # 获取当前表格选中的数据
            if text:
                try:
                    clipboard = QApplication.clipboard()
                    clipboard.setText(text)  # 复制到粘贴板
                except BaseException as e:
                    print(e)
        if (event.key() == Qt.Key_V) and QApplication.keyboardModifiers() == Qt.ControlModifier:
            clipboard = QApplication.clipboard()
            rows = clipboard.text().split("\n")
            for i,item in enumerate(rows):
                rows[i] = item.split("\t")
            indexes = self.tableView.selectedIndexes()
            row = indexes[0].row()
            colmn = indexes[0].column()
            for row_item in rows:
                for column in row_item:
                    self.tableView.model.setItem(row,colmn,QStandardItem(column))
                    colmn += 1
                row += 1
                colmn = indexes[0].column()
    def warn(self):
        QMessageBox.information(self,"提示","计算失败，请检查输入")
    def success(self):
        QMessageBox.information(self, "提示", "成功")



if __name__ == "__main__":

    app = QApplication(sys.argv)
    gui = GUI2MainWindow()
    gui.show()
    sys.exit(app.exec_())