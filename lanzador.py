from Punto import Punto
from Rectangulo import Rectangulo


def imprimir_puntos():
    print(f"Punto A: {A}")
    print(f"Punto B: {B}")
    print(f"Punto C: {C}")
    print(f"Punto D: {D}")

def consultar_cuadrantes():
    print(f"Punto A está en el {A.cuadrante()}")
    print(f"Punto B está en el {B.cuadrante()}")
    print(f"Punto C está en el {C.cuadrante()}")
    print(f"Punto D está en el {D.cuadrante()}")

def consultar_vectores():
    print(f"Vector AB: {vector_AB}")
    print(f"Vector BA: {vector_BA}")

def consultar_distancias():
    print(f"Distancia entre A y B: {distancia_AB}")
    print(f"Distancia entre B y A: {distancia_BA}")

    if distancia_A_origen > distancia_B_origen and distancia_A_origen > distancia_C_origen:
        print("El punto A está más lejos del origen.")
    elif distancia_B_origen > distancia_A_origen and distancia_B_origen > distancia_C_origen:
        print("El punto B está más lejos del origen.")
    else:
        print("El punto C está más lejos del origen.")

def imprimir_resultados():
    print("Base del rectángulo:", rectangulo.base())
    print("Altura del rectángulo:", rectangulo.altura())
    print("Área del rectángulo:", rectangulo.area())
