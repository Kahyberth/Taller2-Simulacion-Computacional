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
                for i in range(1, self.intervalo + 1):
                    #print([ls, li])
                    ls = li
                    li = (1 / self.intervalo) + ls
                    save.append([ls, li])
        else:
            self.intervalo =  round(math.sqrt(len(self.lista)))
            ls = 0
            li = (1 / self.intervalo) + ls
            save.append([ls, li])
            for i in range(1, self.intervalo + 1):
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
        suma = sum(self.estadistico())
        return suma
    
    def chiCuadrado(self):
        return stats.chi2.ppf((1 - 0.05), 9)
    
    
    def frecuenciaObservadaAcumulada(self):
        save = []
        for i in self.frecuenciaObservada():
            save.append(i + sum(save))
        return save
    
    def probabilidadObservadaAcumulada(self):
        save = []
        for i in self.frecuenciaObservadaAcumulada():
            save.append(i / len(self.lista))
        return save
    
    def probabiliadEsperadaAcumulada(self):
        save = []
        if self.intervalo is None:
            self.intervalo =  round(math.sqrt(len(self.lista)))
            fx = (1 / self.intervalo)
            for i in range(1,self.intervalo):
                save.append(fx * (i))
        elif self.intervalo != None:
            fx = 1 / self.intervalo
            for i in range(self.intervalo):
                save.append(fx * (i + 1))
        return save
    
    
    def diferenciaAbsoluta(self):
        save = []
        for i in range(len(self.probabilidadObservadaAcumulada())-1):
            save.append(abs(self.probabiliadEsperadaAcumulada()[i] - self.probabilidadObservadaAcumulada()[i]))
        return save
        
    
    
    
    def kolmogorov_smirnov(self):
    # Llama a los métodos y almacena los resultados
        self.obtenerIntervalo()
        frecuencia_observada = self.frecuenciaObservada()
        frecuencia_acumulada = self.frecuenciaObservadaAcumulada()
        probabilidad_acumulada = self.probabilidadObservadaAcumulada()
        probabilidad_esperada_acumulada = self.probabiliadEsperadaAcumulada()
        diferencia_absoluta = self.diferenciaAbsoluta()

        # Realiza la comparación
        max_diferencia_absoluta = max(diferencia_absoluta)
        if max_diferencia_absoluta <= (1.36 / math.sqrt(len(self.lista))):
            print(max_diferencia_absoluta)
            print("Se acepta la hipotesis de que los numeros son independientes")
        else:
            print(max_diferencia_absoluta)
            print("Se rechaza la hipotesis de que los numeros son independientes")

        
    
    
    def chi2(self):
        intervalos = []
        frecuenciaObservada = []
        frecuenciaEsperada = []
        estadistico = []
        sumaEstadistico = []
        chiCuadrado = []
        intervalos.append(self.obtenerIntervalo())
        frecuenciaObservada.append(self.frecuenciaObservada())
        frecuenciaEsperada.append(self.frecuenciaEsperada())
        estadistico.append(self.estadistico())
        sumaEstadistico.append(self.sumaEstadistico())
        chiCuadrado.append(self.chiCuadrado())
        
        return [intervalos, frecuenciaObservada, frecuenciaEsperada, estadistico, sumaEstadistico, chiCuadrado]
        
        