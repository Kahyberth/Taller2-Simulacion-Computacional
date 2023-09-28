import math

class Generador:

    def __init__(self, x0, a, c, m):
        self.x0 = x0
        self.a = a
        self.c = c
        self.m = m

    def generadorLinealCongruente(self, n=None):
        xn = self.x0
        dato = []
        while n > 0 if n != None else True:
            xn = (self.a * xn + self.c) % self.m
            rn = xn / self.m
            if rn in dato:
                break
            dato.append(rn)

        return dato

    def generadorEstandarMinimo(self, n=None):
        q = math.floor(self.m / self.a)
        r = (self.m % self.a)
        xn_1 = self.x0
        dato = []
        self.m = self.a * q + r
        while True:
            if (self.a * (xn_1 % q) - r * math.floor(xn_1 / q)) >= 0:
                modulo = (self.a * (xn_1 % q) - r * math.floor(xn_1 / q)) % self.m
            else:
                modulo = (self.a * (xn_1 % q) - r * math.floor(xn_1 / q) + self.m) % self.m
            xn_1 = modulo

            if xn_1 in dato:
                break
            else:
                dato.append(xn_1)
        return dato







