from utils.common import readTable
from gui.Table import Tableview
from core.check1 import *
from core.check2 import *
import numpy as np
def run(tableview:Tableview):
    check1 = Check1()
    # check1.set_data(readTable(tableview))
    #check1.init_test()
    # check1.test_process(check1.data)



    data = np.array([[10.89,12.31,12.89],[10.78,12.10,12.28],[10.98,11.79,12.61],[11.03,11.85,12.37],[10.93,12.12,11.85],[11.26,12.04,12.13],[10.54,12.04,12.70],[11.04,11.95,12.62],[11.00,12.80,12.86]])
    check1.set_data(data)
    check1.init_test()
    check1.test_process(check1.data)

def run1(tableview:Tableview,arg:dict):
    check2 = Check2()
    check2.set_data(readTable(tableview))
    check2.init_test(arg)
    # check2.pure_value(check2.data)
    # check2.uncertainty(check2.data)
