print("Ciclo for usando diccionario: ")
#Calificaciones del 1 al 10
#5 alumnos
#Materias: Español, Matemáticas, Geografía, Historia, Literatura
alumno0 = [7.5, 6, 8, 10, 10]
alumno1 = [9, 4.5, 3, 6, 9.5]
alumno2 = [6, 6.5, 9, 10, 7.5]
alumno3 = [9.5, 10, 10, 10, 8.5]

#Indices-------[  0  ,    1   ,   2   ,     3    ]
nombreAlumnos = ["Yan", "David", "Mari", "ElRodri"]

"""
Diccionario en Python
listaAlumnos[clave] = valor
listaAlumnos[Yan] = [7.5, 6, 8, 10, 10]
listaAlumnos[David] = [9, 4.5, 3, 6, 9.5]
listaAlumnos[Mari] = [6, 6.5, 9, 10, 7.5]
listaAlumnos[ElRodri] = [9.5, 10, 10, 10, 8.5]
"""
listaAlumnos = {}
listaAlumnos[nombreAlumnos[0]] = alumno0
listaAlumnos[nombreAlumnos[1]] = alumno1
listaAlumnos[nombreAlumnos[2]] = alumno2
listaAlumnos[nombreAlumnos[3]] = alumno3


#Indices-------[     0    ,       1      ,      2     ,      3    ,       4     ] no se esta usando
listaMaterias = ["Español", "Matemáticas", "Geografia", "Historia", "Literatura"]

#Sacar el promedio de cada alumno mostrando su nombre:

for alumno, calificacion in listaAlumnos.items():
    suma = sum(calificacion)
    promedio = suma / 5
    print("Alumno: "+str(alumno)+" suma: "+str(suma) +" promedio: "+str(promedio))
    


