import numpy as np
import scipy as sp
import scipy.stats as st

def um_value(MxE,MtdE,yuansu):
    sum_MxE = 0
    sum_MstdE = 0
    for key,value in MxE:
        sum_MxE += np.sqrt(value*yuansu[key],2)
    for key,value in MtdE:
        sum_MstdE += np.sqrt(value*yuansu[key],2)
    return np.sqrt(sum_MxE,0.5),np.sqrt(sum_MstdE,0.5)