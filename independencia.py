import math
import numpy as np
class Independencia:
    
    def __init__(self, lst) -> None:
        self.lst = lst
        self.data = np.array([])
        
    def number_of_runs(self):
        lst = self.lst;
        positive = ""
        negative = ""
        runs = np.array([])
        current_value = lst[0]
        for i in lst[1:]:
            if current_value <= i:
                positive += "+"
                if negative != "": 
                    runs = np.append(runs, negative)
                    negative = ""
                current_value = i
            else:
                negative += "-"
                if positive != "":
                    runs = np.append(runs, positive)
                    positive = ""
                current_value = i
        self.data = np.append(self.data, len(runs)+1)
        return len(runs)+1


    def avarange(self):
        self.data = np.append(self.data, ((2 * len(self.lst)) - 1) / 3)

    def variance(self):
        self.data = np.append(self.data, ((16 * len(self.lst)) - 29) / 90)
    
    def z(self):
        if ( len(self.lst) > 20):
            z = (self.data[0] - self.data[1]) / math.sqrt(self.data[2])
            self.data = np.append(self.data, z)

    def runs(self):
        self.number_of_runs()
        self.avarange()
        self.variance()
        self.z()
        
        if ( self.data[3] >= -1.96 and self.data[3] <= 1.96):
            print("Es independiente")
            return  self.data
        else:
            print("No es independiente")
            return self.data
    