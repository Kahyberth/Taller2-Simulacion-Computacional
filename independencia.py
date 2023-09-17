import math
import scipy.stats as stats

class Independencia:
    
    def __init__(self, lista, intervalo = None):
        self.intervalo = intervalo
        self.lista = lista
        
    def obtenerIntervalo(self):
        save = []
        if (self.intervalo != None):
                ls = 0
                li = (1 / self.intervalo) + ls
                save.append([ls, li])
                for i in range(1, self.intervalo):
                    #print([ls, li])
                    ls = li
                    li = (1 / self.intervalo) + ls
                    save.append([ls, li])
        else:
            self.intervalo =  round(math.sqrt(len(self.lista)))
            ls = 0
            li = (1 / self.intervalo) + ls
            save.append([ls, li])
            for i in range(1, self.intervalo):
                #print([ls, li])
                ls = li
                li = (1 / self.intervalo) + ls
                save.append([ls, li])
        
        return save             

    def frecuenciaObservada(self):
        save = []
        for i in self.obtenerIntervalo():
            contador = 0
            for j in self.lista:
                if (j >= i[0] and j < i[1]):
                    contador += 1
            save.append(contador)
        return save

    def frecuenciaEsperada(self):
        save = []
        for i in self.frecuenciaObservada():
            save.append(len(self.lista) / self.intervalo)
        return save

    def estadistico(self):
        save = []
        for i in range(len(self.frecuenciaObservada())-1):
            save.append((self.frecuenciaEsperada()[i] - self.frecuenciaObservada()[i]) ** 2 / self.frecuenciaEsperada()[i])
        return save
    
    def sumaEstadistico(self):
        return sum(self.estadistico())
    
    def chiCuadrado(self):
        return stats.chi2.ppf((1 - 0.05), 9)