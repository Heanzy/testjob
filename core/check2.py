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
        self.TP = arg["TP"]
        self.output = []
    def set_data(self,data):
        self.data = np.array(data)
        print("*****置入数据*****"+"\n",self.data)

    def pure_value(self,data):
        for i,row in enumerate(data):
            Px = row[0] / row[1] * self.nstd / self.nx * self.Mx / self.Mstd * row[3] / row[2]*self.Pstd
            self.output.append(Px)
        self.Pnmr = np.mean(self.output)
        self.s = np.std(self.output,ddof=1)
        print("Pnmr:",self.Pnmr)
        print("s:",self.s)
        return self.Pnmr,self.s,self.output


    def uncertainty(self,data):
        d = self.TP
        self.u_ix_istd = self.s
        self.u_mstd = self.u_mx = d / pow(3, 0.5)
        self.u_Pstd = self.Ucrm / 2
        self.u_Mx, self.u_Mstd = uu.um_value(self.MxE,self.MstdE,self.yuansu)
        def temp():
            return pow(pow(self.u_ix_istd/self.Pnmr,2)+
                           pow(self.u_Mx/self.Mx,2)+
                           pow(self.u_Mstd/self.Mstd,2)+
                           self.u_Mx**2+
                           self.u_Mstd**2+
                           (self.u_Pstd/self.Pstd)**2,0.5)
        self.u_Pnmr = self.Pnmr*temp()
        return self.u_ix_istd,self.u_mstd,self.u_mx,self.u_Pstd,self.u_Mx,self.u_Mstd,self.u_Pnmr