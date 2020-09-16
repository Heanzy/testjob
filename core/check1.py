import numpy as np
import scipy as sp
import scipy.stats as st
import utils.dixon as ud

data = np.array([10.89,10.78,10.98,11.03,10.93,11.26,10.54,11.04,11.00],
                [12.31,12.10,11.79,11.85,12.12,11.26,10.54,11.04,11.00],
                [10.89,10.78,10.98,11.03,10.93,11.26,10.54,11.04,11.00],
                [10.89,10.78,10.98,11.03,10.93,11.26,10.54,11.04,11.00],
                [10.89,10.78,10.98,11.03,10.93,11.26,10.54,11.04,11.00],
                [10.89,10.78,10.98,11.03,10.93,11.26,10.54,11.04,11.00])
is_pass_shapiro = [True] * len(data)
is_pass_dixon = [True] * len(data)
is_pass_cochran = [True] * len(data)
xa = [0] * len(data)
s = [0] * len(data)
xa_pass_dixon = True
xa_pass_shapiro = True
txa = 0
ts = 0
def shapiro_wilk_test(row):

    p=0.95
    Wnp = 0.829
    w, p = st.shapiro(row)
    return w > Wnp
def dixon_test(row):
    fa1 = 0.672
    fa5 = 0.564
    length = len(row)
    r1 = ud.r1(row)
    rn = ud.rn(row)
    if r1 > rn and r1 > fa1:
        np.delete(row, 0, 1)
        return False
    if rn > r1 and rn > fa1:
        np.delete(row, length - 1, 1)
        return False
    return True

def cochran_test(row):
    Camn = 0.3682
    temp = np.power(row,2)
    c = np.max(temp) / np.sum(temp)
    return c <= Camn
def test_process(data):
    for index,row in enumerate(data):
        if not shapiro_wilk_test(row):
            is_pass_shapiro[index] = False
            continue
        while not dixon_test(row) and len(row) >= 6:
            if not shapiro_wilk_test(row):
                is_pass_shapiro[index] = False
                break
        if not shapiro_wilk_test(row):
            continue
        if len(row) < 6:
            is_pass_dixon[index] = False
            continue
        xa[index] = np.mean(row)
        s[index] = np.std(row)
    if not cochran_test(s):
        is_pass_cochran[index] = False
        return False
    if not dixon_test(xa):
        global xa_pass_dixon
        xa_pass_dixon = False
        return False
    if not shapiro_wilk_test(xa):
        global xa_pass_shapiro
        xa_pass_shapiro = False
        return False
    global txa
    txa = np.mean(xa)
    global sa
    sa = np.std(s)
