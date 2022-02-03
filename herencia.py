class Punto2D:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    #metodos
    def coordenada2d(self):
        return [self.x, self.y]

class Color:
    rojo = "ROJO"
    negro = "NEGRO"
    verde = "VERDE"
    actual = None

    def __init__(self, color):
        self.actual = color

class Punto3D(Punto2D, Color):
    z = 0

    def __init__(self, x, y, z):
        Punto2D.__init__(self, x, y)
        Color.__init__(self, "Negro")
        self.z = z
        

    #metodos
    def coordenada2d(self):
        return [self.x, self.y, self.actual]

    def coordenada3d(self):
        return [self.x, self.y, self.z, self.actual]


p1 = Punto2D(1, 0)
p2 = Punto3D(1, 1, 5)

print(p1.coordenada2d())
print(p2.coordenada2d())
print(p2.coordenada3d())