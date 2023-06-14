x = 0
y = 1

print("Primer ciclo while con 'continue'")
while (x < 20 and y < 15):
    if(y == 8):
        y = y + 1
        continue
        print("Valor de y = "+str(y)+ " U0001F600")
    else:
        print("Valor de y = "+str(y)+ " U0001F600")
        y = y + 1
print("Hola aqui ando")

y = 1

print("Segundo ciclo while con 'break'")
while x < 20 and y < 15:
    if(y == 8):
        y = y + 1
        break
        print("Valor de y = "+str(y)+ " U0001F600")
    else:
        print("Valor de y = "+str(y)+ " U0001F600")
        y = y + 1
print("Hola aqui ando\n")


n = 100

print("Ciclo for/while de la suma de los primeros "+str(n)+" numeros: ")

suma_con_for = 0
for i in range(1, n+1):
    suma_con_for += i

print("La suma con for desde 1 hasta "+str(n)+ " es: "+str(suma_con_for))

j = 1
suma_con_while = 0
while j < n+1:
    suma_con_while += j
    j += 1

print("La suma con while desde 1 hasta "+str(n)+ " es: "+str(suma_con_while))


print("Suma de los primeros" +str(n)+" numeros pares: ")

k = 2
suma_pares_while = 0
while k < n+1:
    suma_pares_while += k
    k += 2

print("La suma con while desde 2 hasta "+str(n)+ " de los numeros pares es: "+str(suma_pares_while)+"\n")   


print("Llenar un arreglo vacio con los primeros "+str(n)+ " numeros: ")

n = 200

arreglo_n_numeros = list(range(100))
x = 101
y = 0
while x <= n:
    arreglo_n_numeros[y] = x
    x += 1
    y += 1

print("El arreglo lleno tiene valores: "+str(arreglo_n_numeros))



"""
arreglo_gato = [[_ _ _], [_ _ _], [_ _ _]]
_ _ _
_ _ _
_ _ _
"""



    
    


    
