#ej.1  Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.

#entrada de datos
calificacion_1= int(input("escribir calificacion1: "))
calificacion_2= int(input("escribir calificacion2: "))
calificacion_3= int(input("escribir calificacion3: "))

#procesos
suma= calificacion_1 + calificacion_2 + calificacion_3
promedio= suma/3


#salida de datos 
print("Promedio de calificacion es:", round(promedio, 2))
