from math import lcm, gcd


class Fraccion:
    def __init__(self, num, den):
        if den == 0:
            raise ZeroDivisionError("Estas dividiendo por zero crack")

        self.num = num // gcd(num, den)
        self.den = den // gcd(num, den)

    def __add__(self, otra):
        den = lcm(self.den, otra.den)
        num = (den // otra.den * otra.num + den // self.den * self.num)
        return Fraccion(num, den)

    def __mul__(self, otra):
        num = self.num * otra.num
        den = self.den * otra.den
        return Fraccion(num, den)

    def __sub__(self, otra):
        return self + (otra * Fraccion(-1, 1))

    def __truediv__(self, otra):
        return self * (Fraccion(otra.den, otra.num))

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraccion({self.num}, {self.den})"


a = Fraccion(3, 4)
b = Fraccion(8, 5)

print(a + b)
print(a * b)
print(a - b)
print(a / b)
