import numpy as np
import scipy as sp
import scipy.stats as st
import utils.dixon as ud
class Check1:


    def __init__(self):
        pass
    def init_test(self):
        self.is_pass_shapiro = [True] * len(self.data)
        self.is_pass_dixon = [True] * len(self.data)
        self.is_pass_cochran = [True] * len(self.data)
        self.xa = [0] * len(self.data)
        self.s = [0] * len(self.data)
        self.xa_pass_dixon = True
        self.xa_pass_shapiro = True
        self.txa = 0
        self.ts = 0
        self.output = {}
        self.tc = 0
    def set_data(self,data):
        self.data = np.array(data)
        self.data = self.data.T
        print("*****置入数据*****"+"\n",self.data)
    def shapiro_wilk_test(self,row):
        P=0.95
        Wnp = 0.829
        w, p = st.shapiro(row)
        return w,Wnp,p > 0.05
    def dixon_test(self,row):
        if len(row) <3:
            print("dixon检验试验次数必须大于3")
            return False
        fa1 = 0.672
        fa5 = 0.564
        length = len(row)
        r1 = ud.r1(row)
        rn = ud.rn(row)
        if r1 > rn and r1 > fa1:
            del row[0]
            #np.delete(row, 0)
            return False
        if rn > r1 and rn > fa1:
            del row[length - 1]
            #np.delete(row, length - 1)
            return False
        return r1,rn,True

    def cochran_test(self,row):
        Camn = 0.801
        temp = np.power(row,2)
        c = np.max(temp) / np.sum(temp)
        return c,c <= Camn
    #W W() r1 rn rf c txa ts
    def test_process(self,data):
        for index,row in enumerate(data):
            if not self.shapiro_wilk_test(row)[-1]:
                print("本组数据不符合正太分布1")
                self.is_pass_shapiro[index] = False
                continue
            else:
                self.output[index] = [self.shapiro_wilk_test(row)[0],]
            while not self.dixon_test(row)[-1] and len(row) >= 6:
                if not self.shapiro_wilk_test(row)[-1]:
                    print("本组数据不符合正太分布2")
                    self.is_pass_shapiro[index] = False
                    break
            if not self.shapiro_wilk_test(row)[-1]:
                print("本组数据不符合正太分布3")
                continue
            if len(row) < 6:
                print("本组数据不符合迪克逊检验且数据小于6了")
                self.is_pass_dixon[index] = False
                continue
            else:
                self.output[index].append(self.dixon_test(row)[0])
                self.output[index].append(self.dixon_test(row)[1])
            self.xa[index] = np.mean(row)
            self.output[index].append(self.xa[index])
            self.s[index] = np.std(row,ddof=1)
            self.output[index].append(self.s[index])
        #TODO 不等精度 循环检验 组数必须大约等于2
        if not self.cochran_test(self.s)[-1]:
            print("整体不等精度")
            self.is_pass_cochran[index] = False
        if not self.dixon_test(self.xa)[-1]:
            print("整体不通过迪克逊检验")
            self.xa_pass_dixon = False
        # if not self.shapiro_wilk_test(self.xa):
        #     self.xa_pass_shapiro = False
        #     return False
        self.tc = self.cochran_test(self.s)[0]
        self.txa = np.mean(self.xa)
        self.ts = np.std(self.xa,ddof=1)
        print(self.txa,self.ts,self.tc)
        return self.txa,self.ts,self.tc,self.output
