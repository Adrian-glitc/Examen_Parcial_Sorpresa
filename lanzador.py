from Punto import Punto
from Rectangulo import Rectangulo
# Crear los puntos
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

# Consultar vectores
vector_AB = A.vector(B)
vector_BA = B.vector(A)

# Consultar distancias
distancia_AB = A.distancia(B)
distancia_BA = B.distancia(A)


# Determinar el punto más lejano del origen
distancia_A_origen = A.distancia(D)
distancia_B_origen = B.distancia(D)
distancia_C_origen = C.distancia(D)

# Crear un rectángulo con los puntos A=(2,3) y B=(5,5)
punto_a = Punto(2, 3)
punto_b = Punto(5, 5)
rectangulo = Rectangulo(punto_a, punto_b)
