"""matriz_nxn = [
            [1, 4, 7, 4], 
            [5, 9, 1, 6],
            [3, 2, 8, 11],
            [10,12, 18, 3]
            ]"""


def matriz(matriz):
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            print("matriz("+str(i)+","+str(j)+") = "+str(matriz[i][j]), end =" ")
        print("")



matriz_nxn = [
            [1, 4, 7, 4], 
            [5, 9, 1, 6],
            [3, 2, 8, 11],
            [10,12, 18, 3]
            ]

matriz(matriz_nxn)