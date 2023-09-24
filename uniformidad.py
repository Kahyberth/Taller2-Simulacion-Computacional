import math
import scipy.stats as stats
class Uniformidad:
    
    def __init__(self, lista, intervalo = None):
        self.intervalo = intervalo
        self.lista = lista
        
    def obtenerIntervalo(self):
        save = []
        if (self.intervalo != None):
                li = 0
                ls = (1 / self.intervalo) + li
                save.append([li, ls])
                for i in range(1, self.intervalo):
                    #print([ls, li])
                    li = ls
                    ls = (1 / self.intervalo) + li
                    save.append([li, ls])
        else:
            self.intervalo =  10
            li = 0
            ls = (1 / self.intervalo) + li
            save.append([li, ls])
            for i in range(0, 9):
                #print([li, ls])
                li = ls
                ls = (1 / self.intervalo) + li
                save.append([li, ls])
        
        return save             

    def frecuenciaObservada(self):
        save = []
        intervalos = self.obtenerIntervalo()
        for i in range(0, len(intervalos)):
            contador = 0
            for j in self.lista:
                if (j >= intervalos[i][0] and j < intervalos[i][1]):
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
        for i in range(len(self.frecuenciaObservada())):
            save.append((self.frecuenciaEsperada()[i] - self.frecuenciaObservada()[i]) ** 2 / self.frecuenciaEsperada()[i])
        return save
    
    def sumaEstadistico(self):
        suma = sum(self.estadistico())
        return suma
    
    def chiCuadrado(self):
        return stats.chi2.ppf((1 - 0.05), 9)
    
    
    def frecuenciaObservadaAcumulada(self):
        frecuenciaObservada = self.frecuenciaObservada()
        save = [frecuenciaObservada[0]]
        for i in range(1, len(frecuenciaObservada)):
           save.append(save[i-1] + frecuenciaObservada[i])
        return save
    
    def probabilidadObservadaAcumulada(self):
        save = []
        for i in self.frecuenciaObservadaAcumulada():
            save.append(i / len(self.lista))
        return save
    
    def probabiliadEsperadaAcumulada(self):
        save = []
        fx = 1 / self.intervalo  # Probabilidad de un intervalo en una distribución uniforme
        acumulado = 0
    
        for i in range(len(self.obtenerIntervalo())):
            acumulado += fx
            save.append(acumulado)
    
        return save
    
    def diferenciaAbsoluta(self):
        save = []
        for i in range(len(self.obtenerIntervalo())-1):
            save.append(abs(self.probabiliadEsperadaAcumulada()[i] - self.probabilidadObservadaAcumulada()[i]))
        return save
        
    
    
    
  


    def kolmogorov_smirnov(self):
        intervalo = self.obtenerIntervalo()
        frecuenciaObservada = self.frecuenciaObservada()
        frecuencia_observada_acumulada = self.frecuenciaObservadaAcumulada()
        probabilidad_observada_acumulada = self.probabilidadObservadaAcumulada()
        probabilidad_esperada_acumulada = self.probabiliadEsperadaAcumulada()
        diferencia_absoluta = self.diferenciaAbsoluta()
        maximo = max(diferencia_absoluta)
        
        
        
        print("Máximo:", maximo)
        DM_critico = 1.36 / math.sqrt(len(self.lista))
        print("DM crítico:", DM_critico)
        if (maximo <= DM_critico):
            print("Se acepta la hipótesis de que los números son Uniformes")
        else:
            print("Se rechaza la hipótesis de que los números son Uniformes")
        
        return intervalo, frecuenciaObservada, frecuencia_observada_acumulada, probabilidad_esperada_acumulada, probabilidad_observada_acumulada, diferencia_absoluta



        
    
    def chi2(self):
        intervalo = self.obtenerIntervalo()
        frecuenciaObservada = self.frecuenciaObservada()
        frecuenciaEsperada = self.frecuenciaEsperada()
        estadistico = self.estadistico()
        sumaEstadistico = self.sumaEstadistico()
        chiCuadrado = self.chiCuadrado()
        print("Suma de estadísticos:", sumaEstadistico)
        print("Chi cuadrado:", chiCuadrado)
        if (sumaEstadistico <= chiCuadrado):
            print("Se acepta la hipótesis de que los números son Uniformes!!")
        else:
            print("Se rechaza la hipótesis de que los números son Uniformes!!")
        
        return intervalo, frecuenciaObservada, frecuenciaEsperada, estadistico
        
        