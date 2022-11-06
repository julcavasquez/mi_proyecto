import math
class Figura:
    def __init__(self, lados):
        self.lados = lados

    def area(self):
        pass


class Circulo(Figura):
    def __init__(self, radio):
        super().__init__(0)
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__(3)
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura)/2


class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__(4)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)



circulo = Circulo(1)
print(circulo.area())
print(circulo.lados)
triangulo = Triangulo(10,2)
print(triangulo.area())
print(triangulo.lados)
rectangulo = Rectangulo(10,2)
print(rectangulo.area())
print(rectangulo.lados)
cuadrado = Cuadrado(10)
print(cuadrado.area())
print(cuadrado.lados)