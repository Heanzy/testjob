import numpy as np
import scipy as sp
import scipy.stats as st
import utils.dixon as ud
import utils.um as uu
class Check2:
    yuansu = {"C": 0.0008, "H": 0.00007, "F": 0.0000005, "N": 0.00007, "O": 0.0003, "S": 0.006, "Cl": 0.002}
    def __init__(self):
        pass
    def init_test(self,arg):
        self.Pnmr = 0
        self.s = 0
        self.u_ix_istd = 0
        self.u_mstd = 0
        self.u_mx = 0
        self.u_Pstd = 0
        self.u_Mx = 0
        self.u_Mstd = 0
        self.u_Pnmr = 0
        self.Mx = arg["Mx"]
        self.nx = arg["nx"]
        self.Pstd = arg["Pstd"]
        self.Mstd = arg["Mstd"]
        self.nstd = arg["nstd"]
        self.Ucrm = arg["Ucrm"]
        self.MxE = arg["MxE"]
        self.MstdE = arg["MstdE"]
        print("arg:",arg)

    def set_data(self,data):
        self.data = np.array(data)
        print("*****置入数据*****"+"\n",self.data)

    def pure_value(self,data):
        for row in data:
            Px = row[0] / row[1] * self.nstd / self.nx * self.Mx / self.Mstd * row[3] / row[2]
            row.append(Px)
        self.Pnmr = np.mean(data[0:][-1])
        self.s = np.std()
        print("Pnmr:",self.Pnmr)
        print("s:",self.s)


    def uncertainty(self,data):
        d = 2
        self.u_ix_istd = self.s
        self.u_mstd = self.u_mx = d / np.sqrt(3, 0.5)
        self.u_Pstd = self.Ucrm / 2
        self.u_Mx, self.u_Mstd = uu.um_value(self.MxE,self.MtdE,self.yuansu)
        def temp():
            return np.sqrt(np.sqrt(self.u_ix_istd/self.Pnmr,2)+
                           np.sqrt(self.u_Mx/self.Mx,2)+
                           np.sqrt(self.u_Mstd/self.Mstd)+
                           self.u_Mx**2+
                           self.u_Mstd**2+
                           (self.u_Pstd/self.Pstd)**2,0.5)
        self.u_Pnmr = self.Pnmr*temp()
        print("u_ix_istd:",self.u_ix_istd)
        print("u_mstd:", self.u_mstd)
        print("u_mx:", self.u_mx)
        print("u_Pstd:", self.u_Pstd)
        print("u_Mx:", self.u_Mx)
        print("u_Mstd:", self.u_Mstd)
        print("u_Pnmr:", self.u_Pnmr)