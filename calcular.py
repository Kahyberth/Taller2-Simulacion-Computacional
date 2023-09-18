from generador import Generador
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
        if (self.type[0] == "Lineal Congruente"):
            generador = Generador(self.x0, self.a, self.c, self.m).generadorLinealCongruente()
            self.lista = generador
        elif(self.type[0] == "Estandar Minimo"):
            generador = Generador(self.x0, self.a, self.c, self.m).generadorEstandarMinimo()
            self.lista = generador
        return generador
        
    def independencia(self):
        if (self.type[1] == "Chi Cuadrado"):
            independencia = Independencia(self.lista).chi2()
            self.datos = independencia
        elif(self.type[1] == "Kolmogorov Smirnov"):
            independencia = Independencia(self.lista).kolmogorov_smirnov()
            self.datos = independencia
    



           


