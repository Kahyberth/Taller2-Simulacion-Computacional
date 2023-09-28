import math

class Generate:

    def __init__(self, x0, a, c, m):
        self.x0 = x0
        self.a = a
        self.c = c
        self.m = m

    def congruentLinearGenerator(self, n=None):
        x = self.x0
        a = self.a
        c = self.c
        m = self.m
        data = []
        for i in range(n):
          x = (a * x + c) % m
          data.append(x / m)
        return data

    def minimumStandardGenerator(self):
        q = math.floor(self.m / self.a)
        r = (self.m % self.a)
        xn_1 = self.x0
        data = []
        self.m = self.a * q + r
        while True:
            if (self.a * (xn_1 % q) - r * math.floor(xn_1 / q)) >= 0:
                modulo = (self.a * (xn_1 % q) - r * math.floor(xn_1 / q)) % self.m
            else:
                modulo = (self.a * (xn_1 % q) - r * math.floor(xn_1 / q) + self.m) % self.m
            xn_1 = modulo

            if xn_1 in data:
                break
            else:
                data.append(xn_1)
        return data



