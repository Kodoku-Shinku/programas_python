lista = ["azul", "rojo", "naranja", "morado", "verde", "amarillo"]

print("Lista inicial: "+str(lista)+"\n")

lista.append("rosa")

print("Lista despues de append('rosa'): "+str(lista)+"\n")

lista.insert(3, "gris")

print("Lista despues de insert(3, 'gris'): "+str(lista)+"\n")

indice = lista.index("verde", 0, len(lista))

print("Lista despues de index("'verde'", 0, len(lista)): "+str(indice)+"\n")


lista_nueva = ["cafe", "violeta", "blanco"]

lista.extend(lista_nueva)

print("Lista despues de lista.extend(lista_nueva): "+str(lista)+"\n")

lista.pop(1)

print("Lista despues de lista.pop(1): "+str(lista)+"\n")

lista.reverse()

print("Lista despues de list.reverse: "+str(lista)+"\n")

lista.sort()

print("Lista despues de list.sort: "+str(lista)+"\n")

num_ocurrencias =lista.count("morado")

print("Lista despues de list.count(morado): "+str(num_ocurrencias)+"\n")

lista.remove("gris")

print("Lista despues de list.remove('gris'): "+str(lista)+"\n")

valor_boleano = lista.__contains__("morado")

print("Lista despues de lista.__contains__('morado'): "+str(valor_boleano)+"\n")

lista.clear()

print("Lista despues de list.clear(): "+str(lista)+"\n")

