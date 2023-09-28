import math

import numpy
from prettytable import PrettyTable


class Indepedence:

    def __init__(self, data_list):
        self.list = data_list

    def count(self):
        data_list = self.list
        positive = ""
        negative = ""
        runs = numpy.array([])

        for i in range(1, len(data_list)):
            if data_list[i] > data_list[i - 1]:
                positive += "+"
                if negative != "":
                    runs = numpy.append(runs, negative)
                    negative = ""
            else:
                negative += "-"
                if positive != "":
                    runs = numpy.append(runs, positive)
                    positive = ""
        return runs

    def runs(self):
        data_list = self.list
        average = ( ((2 * len(data_list)) - 1) / 3)
        variance = ( ((16 * len(data_list)) - 29) / 90)
        count = self.count()
        z = (len(count) - average) / math.sqrt(variance)
        x = PrettyTable()
        x.field_names = ["CONTEO","MEDIA", "VARIANZA", "Z","INDEPENDENCIA"]
        if -1.96 <= z and z < 1.96:
            x.add_row([len(count), average, variance, z, True])
        else:
            x.add_row([len(count), average, variance, z, False])

        print(x)
