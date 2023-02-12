#arreglos(array) conjunto o coleecion de valores de uno o mas tipos de datos




#entrada de datos
nombres=["israel", "ivan", "angel", "david"]
#indice     0         1       2        3
edades=[   18,       20,      30,      23]
#indice     0         1        2        3
arreglo_general =[0, 2.6, "Hola", True]

#procesos
#funciones con arreglos
#agregar un elemento
nombres.append("eduardo")
edades.append(31)
arreglo_general.append("adios")

#modificar un elemento
nombres[0]= "israel"
edades[0]=19

#eliminar un elemento
arreglo_general.pop(2)

#vaciar o limpiar el arreglo
#nombres.clear()
#edades.clear()
#arreglo_general.clear()

#ordenar los elementos del arreglo
#orden asc
nombres.sort(reverse=False)
edades.sort(reverse=False)
#orden desc
nombres.sort(reverse=True)
edades.sort(reverse=True)

#salida de datos
print("nombres:", nombres)
print("edades:",edades)
print("arreglo:",arreglo_general)
