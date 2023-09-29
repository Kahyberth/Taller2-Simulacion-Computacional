import math
import numpy
from prettytable import PrettyTable


class Uniformity:

    def __init__(self, data_list, limit=10):
        self.range = limit
        self.list = data_list

    def chi_cuadrado(self):
        data_list = self.list
        number_of_classes = self.range
        chi = 0
        x = PrettyTable()
        x.field_names = ["RANGO", "fo", "fe", "ESTADÍSTICO"]
        for i in range(number_of_classes):
            fo = len(list(filter(lambda dato: i / number_of_classes <= dato < (i + 1) / number_of_classes, data_list)))
            fe = len(data_list) / number_of_classes
            di = (math.pow((fo - fe), 2)) / fe
            chi += di
            x.add_row([f"[{(i + 1) / number_of_classes},{(i + 1) / number_of_classes}]", fo, fe, di])
        print(x)

        return chi

    def kolmogorov(self):
        data_list = self.list
        number_of_classes = self.range
        xcal = numpy.array([])
        foa = 0
        x = PrettyTable()
        x.field_names = ["RANGO", "FO", "FOA", "POA", "PEA", "| PEA - POA |"]
        for i in range(number_of_classes):
            fo = len(list(filter(lambda dato: i / number_of_classes <= dato < (i + 1) / number_of_classes, data_list)))
            foa = fo + foa
            poa = foa / len(data_list)
            pea = (i + 1) / number_of_classes
            xcal = numpy.append(xcal, math.fabs(pea - poa))
            x.add_row([f"[{i/ number_of_classes},{(i + 1) / number_of_classes}]", fo, foa, poa, pea,
                       math.fabs(pea - poa)])

        print(x)
