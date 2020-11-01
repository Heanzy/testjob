from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Table import Tableview
from utils.common import readTable
from Controller import run
import sys
from copyAction import selected_tb_text
class GUI1MainWindow(QWidget):
    start_signal = pyqtSignal(Tableview)
    def __init__(self):
        super(GUI1MainWindow,self).__init__()
        self.setObjectName("主窗口")
        self.setWindowTitle("check1")
        self.resize(700,600)
        self.tableView = Tableview(self)
        self.satrtButton = QtWidgets.QPushButton()
        self.satrtButton.setText("开始")
        self.satrtButton.clicked.connect(self.startSignal)
        self.initSignal()
        vlayout = QVBoxLayout(self)
        vlayout.addWidget(self.tableView)
        vlayout.addWidget(self.satrtButton)
    def initSignal(self):
        self.start_signal.connect(run)
    def startSignal(self):
        self.start_signal.emit(self.tableView)

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

if __name__ == "__main__":

    app = QApplication(sys.argv)
    gui = GUI1MainWindow()
    gui.show()
    sys.exit(app.exec_())