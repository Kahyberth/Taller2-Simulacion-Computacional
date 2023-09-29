import math

import numpy
from prettytable import PrettyTable


class Independence:

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

    def poker(self, pk):
        data_list = self.list
        x = PrettyTable()
        x.field_names = ["CLASES", "FO", "FE", "(FE-FO)^2 / 2"]
        if pk == 3:
            all_different = 0.72 * len(data_list)
            even = 0.27 * len(data_list)
            third = 0.01 * len(data_list)
            pks = self.count_similarities(3)
            pk3 = pks.count(3)
            pk2 = pks.count(2)
            pk1 = len(data_list) - len(pks)


            x.add_row(["3 CARTAS IGUALES", f"{pk3}",f"{third}", f"{math.pow((third - pk3), 2) / third}"])
            x.add_row(["1 PAR", f"{pk2}", f"{even}", f"{math.pow((even - pk2),2) / even}"])
            x.add_row(["TODAS DIFERENTES", f"{pk1}", f"{all_different}", f"{math.pow((all_different - pk1),2)/all_different}"])

            print(x)
        elif pk == 4:
            all_different = 0.5040 * len(data_list)
            even = 0.4320 * len(data_list)
            two_even = 0.0270 * len(data_list)
            third = 0.0360 * len(data_list)
            poker = 0.0010 * len(data_list)
            pks = self.count_similarities(4)
            pk4 = pks.count(4)
            pk3 = pks.count(3)
            pk2 = pks.count(2)
            pk1 = len(data_list) - len(pks)

            x.add_row(["TODAS DIFERENTES", f"{pk1}", f"{all_different}", f"{math.pow((all_different - pk1),2) / all_different}"])
            x.add_row(["1 PAR", f"{pk2}", f"{even}", f"{math.pow((even - pk2),2)/even}" ])
            x.add_row(["2 PARES" ])
            x.add_row(["TERCIA", ])
            x.add_row(["POKER", ])



    def count_similarities(self, pk):
        data_list = self.list
        digits = []
        for i in data_list:
            digit = str(i)[2:]
            for j in digit:
                count = digit.count(j)
                if count >= 2:
                    digits.append(count)
                    break
        return digits






