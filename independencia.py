import math
import numpy as np
class Independencia:
    
    def __init__(self, lst) -> None:
        self.lst = lst
        self.data = np.array([])
        
    def number_of_runs(self):
        lst = self.lst
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
        

    def poker(self):
        return print(f"{self.poker_3()}  {self.poker_5()}") 
        

    def poker_3(self):
        n = len(self.lst)
        counts = {
            "TD": 0,
            "1P": 0,
            "T": 0
        }

        for number in self.lst:
            decimal_digits = [int(digit) for digit in str(number)[2:5]]
            unique_digits = set(decimal_digits)

            if len(unique_digits) == 3:
                counts["TD"] += 1
            elif len(unique_digits) == 2:
                counts["1P"] += 1
            elif len(unique_digits) == 1:
                counts["T"] += 1
            #print(number, unique_digits, decimal_digits, counts)

        # Asegurémonos de que la suma de todas las categorías sea igual al total de números
        print("-----------------------------------------------------------------")
        print(sum(counts.values()))
        print(n)
        print("-----------------------------------------------------------------")
        print(counts)
        

        FE = {"TD": 0.72*n, "1P": 0.27*n, "T": 0.01*n}


        chi_square = 0
        for i in FE:
            chi_square += ((FE[i] - counts[i]) ** 2) / FE[i] 

        critical_value = 5.991  # Valor crítico para un nivel de significancia del 0.05 (para 2 grados de libertad)

        if chi_square <= critical_value:
            print("La secuencia es independiente (PÓKER DE 3)")
            print(f"{chi_square} <= {critical_value}")
            return chi_square
        else:
            print("La secuencia no es independiente (PÓKER DE 3)")
            print(f"{chi_square} > {critical_value}")
            return chi_square

    #----------------------------------------------------------------------

    def poker_5(self):
        n = len(self.lst)
        counts = {
            "TD": 0,
            "1P": 0,
            "2P": 0,
            "T": 0,
            "TP": 0,
            "P": 0, 
            "Q": 0
        }


        for number in self.lst:
            decimal_digits = [int(digit) for digit in str(number)[2:7]]
            unique_digits = set(decimal_digits)

            if len(unique_digits) == 5:
                counts["TD"] += 1
            elif len(unique_digits) == 4:
                counts["1P"] += 1
            elif len(unique_digits) == 3:
                for digit in unique_digits:
                    if decimal_digits.count(digit) == 3:
                        counts["T"] += 1
                        break
                    elif decimal_digits.count(digit) == 2:
                        counts["2P"] += 1
                        break
            elif len(unique_digits) == 2:
                for digit in unique_digits:
                    if decimal_digits.count(digit) == 4:
                        counts["P"] += 1
                        break
                    elif decimal_digits.count(digit) == 3 or decimal_digits.count(digit) == 2:
                        counts["TP"] += 1
                        break

            elif len(unique_digits) == 1:
                counts["Q"] += 1


        
        # Asegurémonos de que la suma de todas las categorías sea igual al total de números
        print("-----------------------------------------------------------------")
        print(sum(counts.values()), "total de numeros en las categorias")
        print(n , "total de numeros de la lista")
        print("-----------------------------------------------------------------")
        print(counts)
        

        FE = {"TD": 0.3024*n, "1P": 0.5040*n, "2P": 0.1080*n, "TP": 0.0090*n, "P": 0.0045*n, "Q": 0.0001*n}


        chi_square = 0
        for i in FE:
            chi_square += ((FE[i] - counts[i]) ** 2) / FE[i] 

        critical_value = 12.592  # Valor crítico para un nivel de significancia del 0.05 (para 2 grados de libertad)

        if chi_square <= critical_value:
            print(f"La secuencia es independiente (PÓKER DE 3) {chi_square} <= {critical_value}")
            return chi_square
        else:
            print(f"La secuencia no es independiente (PÓKER DE 3) porque {chi_square} > {critical_value}")
            return chi_square

    