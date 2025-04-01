import math

class Punto:
    def __init__(self, x=0, y=0):
         self.x = x
         self.y = y

    def __str__(self):
         return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "Origen"
        elif self.x == 0:
            return "Eje Y"
        elif self.y == 0:
            return "Eje X"
        elif self.x > 0 and self.y > 0:
            return "Cuadrante I"
        elif self.x < 0 and self.y > 0:
            return "Cuadrante II"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante III"
        elif self.x > 0 and self.y < 0:
            return "Cuadrante IV"

    def vector(self, otro_punto):
        return Punto(otro_punto.x - self.x, otro_punto.y - self.y)
    
    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)