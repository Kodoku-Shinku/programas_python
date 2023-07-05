def factorial(n):
    """
    Esta función calcula el factorial de un número entero no negativo.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)



# n = 2 , n = 1, n = 0


# Pedir al usuario que ingrese un número
numero = int(input("Ingresa un número entero no negativo: "))

# Validar que el número sea no negativo
if numero < 0:
    print("El número debe ser no negativo.")
else:
    resultado = factorial(numero)
    print("El factorial de", numero, "es", resultado)
