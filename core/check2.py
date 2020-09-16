import numpy as np
import scipy as sp
import scipy.stats as st
import utils.dixon as ud
import utils.um as uu
Pnmr = 0
s = 0
yuansu = {"C": 0.0008, "H": 0.00007, "F": 0.0000005, "N": 0.00007, "O": 0.0003, "S": 0.006, "Cl": 0.002}
u_ix_istd = 0
u_mstd = 0
u_mx = 0
u_Pstd = 0
u_Mx = 0
u_Mstd = 0
u_Pnmr = 0
Mx = 1
nx = 2
Pstd = 3
Mstd = 4
nstd = 5
Ucrm = 6


def pure_value(data):
    global Mx, nx, Pstd, Mstd, nstd, Ucrm
    global Pnmr
    global s
    for row in data:
        Px = row[0] / row[1] * nstd / nx * Mx / Mstd * row[3] / row[2]
        row.append(Px)
    Pnmr = np.mean(row[-1])
    s = np.std()


def uncertainty(data):
    MxE = {"C": 18, "H": 24, "F": 1, "N": 3, "O": 6, "S": 1, "Cl": 0}#TODO 输入
    MtdE = {"C": 18, "H": 24, "F": 1, "N": 3, "O": 6, "S": 1, "Cl": 0}#TODO 输入
    d = 2
    global u_ix_istd, u_mstd, u_mx, u_Pstd, u_Mx, u_Mstd, u_Pnmr, Pnmr
    u_ix_istd = s
    u_mstd = u_mx = d / np.sqrt(3, 0.5)
    u_Pstd = Ucrm / 2
    u_Mx, u_Mstd = uu.um_value(MxE,MtdE,yuansu)
    def temp():
        nonlocal u_ix_istd,Pnmr,u_Mx,Mx,u_Mstd,u_Mstd,Mstd,u_Mx,u_Mstd,u_Pstd,Pstd
        return np.sqrt(np.sqrt(u_ix_istd/Pnmr,2)+
                       np.sqrt(u_Mx/Mx,2)+
                       np.sqrt(u_Mstd/Mstd)+
                       u_Mx**2+
                       u_Mstd**2+
                       (u_Pstd/Pstd)**2,0.5)
    u_Pnmr = Pnmr*temp()