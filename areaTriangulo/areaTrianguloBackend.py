import math


def calcular_area_triangulo(a, b, c):
    # Calcula el semiperímetro del triángulo
    s = (a + b + c) / 2

    # Calcula el área utilizando la fórmula de Herón
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return round(area, 3)
