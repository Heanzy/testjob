from utils.common import readTable
from gui.Table import Tableview
from core.check1 import *
from core.check2 import *
from PyQt5.QtGui import *
import numpy as np
def run(tableview:Tableview):
    check1 = Check1()
    data = readTable(tableview)
    check1.set_data(data)
    check1.init_test()
    txa,ts,tc,output = check1.test_process(check1.data)
    print("output:",output)
    rowcount = len(data)
    columncount = len(data[0])
    title = {0:"W",1:"r1",2:"rn",3:"平均值",4:"标准偏差"}
    title1 = {0:"总平均值",1:"总标准偏差",2:"C"}
    for i in range(columncount):
        for j in range(5):
            tableview.model.setItem(rowcount+j,i,QStandardItem(title[j]+"="+format(output[i][j],".4f")))
    rowcount += 5
    tableview.model.setItem(rowcount + 0, 0, QStandardItem(title1[0] + "=" + format(txa, ".4f")))
    tableview.model.setItem(rowcount + 1, 0, QStandardItem(title1[1] + "=" + format(ts, ".4f")))
    tableview.model.setItem(rowcount + 2, 0, QStandardItem(title1[2] + "=" + format(tc, ".4f")))





    # data = np.array([[10.89,12.31,12.89],[10.78,12.10,12.28],[10.98,11.79,12.61],[11.03,11.85,12.37],[10.93,12.12,11.85],[11.26,12.04,12.13],[10.54,12.04,12.70],[11.04,11.95,12.62],[11.00,12.80,12.86]])
    # check1.set_data(data)
    # check1.init_test()
    # check1.test_process(check1.data)

def run1(tableview:Tableview,arg:dict):
    check2 = Check2()
    data = readTable(tableview)
    check2.set_data(data)
    check2.init_test(arg)
    Pnmr, s, output =  check2.pure_value(check2.data)
    column = len(data[0])
    row = len(data)
    for i in range(row):
        tableview.model.setItem(i, column, QStandardItem("Px" + "=" + format(output[i], ".6f")))

    tableview.model.setItem(row, column, QStandardItem("Pnmr" + "=" + format(Pnmr, ".6f")))
    tableview.model.setItem(row + 1, column, QStandardItem("S" + "=" + format(s, ".6f")))
    u_ix_istd,u_mstd,u_mx,u_Pstd,u_Mx,u_Mstd,u_Pnmr = check2.uncertainty(check2.data)
    tableview.model.setItem(row + 2, column, QStandardItem("u(Ix/Istd)" + "=" + format(u_ix_istd, ".6f")))
    tableview.model.setItem(row + 3, column, QStandardItem("u(mstd)" + "=" + format(u_mstd, ".6f")))
    tableview.model.setItem(row + 4, column, QStandardItem("u(mx)" + "=" + format(u_mx, ".6f")))
    tableview.model.setItem(row + 5, column, QStandardItem("u(Pstd)" + "=" + format(u_Pstd, ".6f")))
    tableview.model.setItem(row + 6, column, QStandardItem("u(Mx)" + "=" + format(u_Mx, ".6f")))
    tableview.model.setItem(row + 7, column, QStandardItem("u(Mstd)" + "=" + format(u_Mstd, ".6f")))
    tableview.model.setItem(row + 8, column, QStandardItem("u(Pnmr)" + "=" + format(u_Pnmr, ".6f")))