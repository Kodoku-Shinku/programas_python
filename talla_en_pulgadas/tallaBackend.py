def convertir_pulgadas_a_centimetros(pulgadas):
    # Convertir pulgadas a centímetros (1 pulgada = 2.54 cm)
    centimetros = pulgadas * 2.54
    return round(centimetros, 2)


def convertir_pies_a_centimetros(pies):
    # Convertir pies a pulgadas (1 pie = 12 pulgadas)
    pulgadas = pies * 12
    # Llamar a la función para convertir pulgadas a centímetros
    centimetros = convertir_pulgadas_a_centimetros(pulgadas)
    return round(centimetros, 2)
