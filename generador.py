import math
import numpy as np
from scipy.stats import chi2
class Generador:
    
    def __init__(self, x0, a, c, m):
        self.x0 = x0
        self.a = a
        self.c = c
        self.m = m
    
    def generadorLinealCongruente(self, n = None):
        xn = self.x0
        dato = []
        while n > 0 if n != None else True:
            xn = (self.a * xn + self.c) % self.m
            rn = xn / self.m
            if rn in dato:
                break
            dato.append(rn)
            
        return dato







