def suma_n_numeros(lista_numeros):
    suma_pares = 0
    suma_impares = 0
    tamaño_lista = len(lista_numeros)

    for i in range(0, tamaño_lista):
        if i % 2 == 0:
            suma_pares += lista_numeros[i]
        else:
            suma_impares += lista_numeros[i]
    
    return suma_pares, suma_impares


def cuadrado_pares_impares(lista_numeros):

    valor_pares, valor_impares = suma_n_numeros(lista_numeros)
    return pow(valor_pares,2), pow(valor_impares,2)




pares, impares = suma_n_numeros([1,5,9,3,6,8,14,21,26])

print ("Suma pares: "+str(pares)) # 1 + 9 + 6 + 14 + 26 = 56
print ("Suma impares: "+str(impares)) # 5 + 3 + 8 + 21 = 37


potencia_pares, potencia_impares = cuadrado_pares_impares([1,5,9,3,6,8,14,21,26])

print("El resulado de elevar la suma de los pares: "+str(pares)+"^2 es: "+str(potencia_pares))
print("El resulado de elevar la suma de los impares: "+str(impares)+"^2 es: "+str(potencia_impares))