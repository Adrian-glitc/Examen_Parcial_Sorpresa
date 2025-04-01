from Punto import Punto
class Rectangulo:
    def __init__(self, punto_inicial=None, punto_final=None):
        # Si no se envían puntos, se crean en el origen por defecto
        self.punto_inicial = punto_inicial if punto_inicial else Punto(0, 0)
        self.punto_final = punto_final if punto_final else Punto(0, 0)

    def base(self):
        # La base es la diferencia en el eje x entre los dos puntos
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        # La altura es la diferencia en el eje y entre los dos puntos
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        # El área es base * altura
        return self.base() * self.altura()

