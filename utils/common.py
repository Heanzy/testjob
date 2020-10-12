
from PyQt5.QtWidgets import *
from gui.Table import Tableview

def readTable(tableview:Tableview):
    rowsCount = tableview.model.rowCount()
    columnCount = tableview.model.columnCount()
    data = [[0]*columnCount for _ in range(columnCount)]
    datafinal = []
    for row in range(rowsCount):
        for column in range(columnCount):
            data[row][column] = float(tableview.model.item(row,column).text()) if tableview.model.item(row,column) is not None else None
        a = [x for x in data[row] if x is not None]
        if a:
            datafinal.append(a)
    print(datafinal)
    return datafinal

