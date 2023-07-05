def perimetro_circulo(radio):
    pi = valor_pi()
    perimetro = 2 * pi * radio
    return perimetro


def area_circulo(radio):
    pi = valor_pi()
    area = pi * pow(radio, 2)
    return area


def valor_pi():
    return 3.1416




p = perimetro_circulo(5)

a = area_circulo(5)

print("Perimetro del circulo: "+str(p))

print("Area del circulo: "+str(a))
