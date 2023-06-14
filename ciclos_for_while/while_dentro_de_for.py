import random

palabras = ['manzana', 'banana', 'pera', 'uva', 'melon', 'sandia', 'guayaba', 'mango']
random.shuffle(palabras)
intentos_maximos = 3

aciertos_correctos = 0
aciertos_incorrectos = 0

for palabra in palabras:
    letras_adivinadas = ['_'] * len(palabra)
    letra_mostrada = random.choice(palabra)
    letras_adivinadas[palabra.index(letra_mostrada)] = letra_mostrada
    
    print("Adivina la palabra:")
    print(' '.join(letras_adivinadas))

    intentos = 0
    while intentos < intentos_maximos:
        respuesta = input("Ingresa tu respuesta: ")
        
        if respuesta.lower() == palabra:
            print("¡Correcto!")
            aciertos_correctos += 1
            break
        else:
            print("Incorrecto. Inténtalo nuevamente.")
            aciertos_incorrectos += 1
        
        intentos += 1

    print("La palabra era:", palabra)
    print()

print("Aciertos correctos:", aciertos_correctos)
print("Aciertos incorrectos:", aciertos_incorrectos)
