class Rectangulo:

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):

    def __init__(self,lado):
        super().__init__(lado,lado)

r = Rectangulo(5,10)
c = Cuadrado(5)

print(f"El area del Rectangulo es: {r.area()}")
print(f"El area del Cuadrado es: {c.area()}")




