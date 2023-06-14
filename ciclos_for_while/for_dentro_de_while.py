alumnos = ["Yan", "David", "Mari", "ElRodri"]
notas = [[8, 7, 9, 8], [9, 8, 7, 9], [7, 6, 8, 7], [9, 9, 9, 10]]

promedios = {}

i = 0
while i < len(alumnos):
    nombre = alumnos[i]
    notas_alumno = notas[i]
    
    suma = 0
    contador = 0

    for nota in notas_alumno:
        suma += nota
        contador += 1

    promedio = suma / contador
    promedios[nombre] = promedio

    i += 1

"""
promedios = {
    ["Yan"] = 8,
    ["David] = 8.25,
    ["Mari"] = 7,
    ["ElRodri"] = 9.25
}
"""

print("Promedios de los alumnos con for dentro de while:")
for nombre, promedio in promedios.items():
    print(f"{nombre}: {promedio:.2f}")



promedios = {}


for i in range(0, len(alumnos)):
    nombre = alumnos[i]
    notas_alumno = notas[i]
    
    suma = 0
    contador = 0
    j = 0

    while j < len(notas_alumno): 
        suma += notas_alumno[j]
        contador += 1
        j += 1

    promedio = suma / contador
    promedios[nombre] = promedio

    

"""
promedios = {
    ["Yan"] = 8,
    ["David] = 8.25,
    ["Mari"] = 7,
    ["ElRodri"] = 9.25
}
"""

print("Promedios de los alumnos con while dentro de for:")
for nombre, promedio in promedios.items():
    print(f"{nombre}: {promedio:.2f}")
