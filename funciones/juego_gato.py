tablero_gato = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def imprime_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

def verifica_ganador(tablero, marca):
    # Verificar filas
    for fila in tablero:
        if all(marca == simbolo for simbolo in fila):
            return True

    # Verificar columnas
    for columna in range(3):
        if all(marca == tablero[fila][columna] for fila in range(3)):
            return True

    # Verificar diagonales
    if (marca == tablero[0][0] == tablero[1][1] == tablero[2][2]) or (marca == tablero[0][2] == tablero[1][1] == tablero[2][0]):
        return True

    return False

victoria = False
turnos = 1

while not victoria:
    marca = input("Ingresa X o O para empezar a jugar: ").upper()

    if marca not in ["X", "O"]:
        print("Marca no válida. Solo se permiten las marcas X o O.")
        continue

    fila = int(input("Ingresa la posicion de la fila: "))
    columna = int(input("Ingresa la posicion de la columna: "))

    if tablero_gato[fila][columna] == "-":
        tablero_gato[fila][columna] = marca
        turnos += 1
    else:
        print("Posicion ocupada, por favor ingrese una nueva posicion")

    imprime_tablero(tablero_gato)

    if turnos > 9:
        print("Juego empatado!!")
        break
    elif verifica_ganador(tablero_gato, marca):
        print("¡Has ganado la partida!")
        break
