from generador import Generador
from uniformidad import Uniformidad
from independencia import Independencia
import numpy as np


class Calcular:
    def __init__(self, x0, a, c, m, type = None):
        self.x0 = x0
        self.a = a
        self.c = c
        self.m = m
        self.type = type
        self.lista = []
        self.datos = []
          
    def generate(self):
        if (self.type[0] == "Lineal"):
            generador = Generador(self.x0, self.a, self.c, self.m).generadorLinealCongruente()
            self.lista = generador
        elif(self.type[0] == "Estandar Minimo"):
            generador = Generador(self.x0, self.a, self.c, self.m).generadorEstandarMinimo()
            self.lista = generador
        return generador
        
    def uniformity(self):
        if (self.type[1] == "Chi2"):
            uniformidad = Uniformidad(self.lista).chi2()
            self.datos = uniformidad
        elif(self.type[1] == "Kolmogorov"):
            uniformidad = Uniformidad(self.lista).kolmogorov_smirnov()
            self.datos = uniformidad
        return uniformidad
    
    def independence(self):
        if (self.type[2] == "Corridas"):
            independencia = Independencia(self.lista).runs()
            self.datos = independencia
        elif(self.type[2] == "Series"):
            independencia = Independencia(self.lista).series()
            self.datos = independencia
        elif(self.type[2] == "Poker"):
            independencia = Independencia(self.lista).poker()
            self.datos = independencia



           


