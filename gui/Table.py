from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Tableview(QTableView):
    def __init__(self,arg=None):
        super(Tableview,self).__init__(arg)
        self.setWindowTitle("talbe test")
        self.resize(200,300)

        self.model= QStandardItemModel(20,20)
        self.setModel(self.model)