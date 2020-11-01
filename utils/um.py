import numpy as np
import scipy as sp
import scipy.stats as st

def um_value(MxE:dict,MtdE:dict,yuansu):
    sum_MxE = 0
    sum_MstdE = 0
    for key,value in MxE.items():
        sum_MxE += pow(value*yuansu[key],2)
    for key,value in MtdE.items():
        sum_MstdE += pow(value*yuansu[key],2)
    return pow(sum_MxE,0.5),pow(sum_MstdE,0.5)