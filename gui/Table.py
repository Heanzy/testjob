from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Tableview(QTableView):
    def __init__(self,arg=None):
        super(Tableview,self).__init__(arg)
        self.setWindowTitle("talbe test")
        self.resize(200,300)

        self.model= QStandardItemModel(20,20)
        self.model.setHorizontalHeaderLabels(['标题1', '标题2', '标题3', '标题4'])
        self.model.setItem(0,0,QStandardItem("11234"))
        self.setModel(self.model)