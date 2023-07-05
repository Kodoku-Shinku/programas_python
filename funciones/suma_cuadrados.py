def suma_cuadrados(numeros):
    cuadrados = []
    for numero in numeros:
        cuadrados.append(pow(numero, 2))
    
    resultado = sum(cuadrados)
    return print(resultado)


cantidad = int(input("Hola cuantos numero quieres sumar?: "))
lista = []

for i in range(cantidad):
    numero = int(input("Ingresa el numero: "))
    lista.append(numero)


suma_cuadrados(lista)


