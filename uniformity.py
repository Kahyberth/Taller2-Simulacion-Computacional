import math
import numpy
from prettytable import PrettyTable
class Uniformity:
    
    def __init__(self, data_list, range = 10):
        self.range = range
        self.list = data_list


    def chi_cuadrado(self):
        data_list = self.list
        number_of_classes = self.range
        chi = 0
        x = PrettyTable()
        x.field_names = ["RANGO", "FO", "FE", "ESTADÍSTICO"]
        for i in range(number_of_classes):
            FO = len(list(filter(lambda dato: i / number_of_classes <= dato < (i + 1) / number_of_classes, data_list)))
            FE = len(data_list) / number_of_classes
            DI = (math.pow((FO-FE),2)) / FE
            chi += DI
            x.add_row([f"[{(i+1)/number_of_classes},{(i+1)/number_of_classes}]",FO,FE,DI])
        print(x)

        return chi






