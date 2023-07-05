def suma_cuadrados(numeros):
    cuadrados = []
    for numero in numeros:
        cuadrados.append(pow(numero, 2))
    
    resultado = sum(cuadrados)
    print(resultado)




suma_cuadrados([1,2,34,5])


