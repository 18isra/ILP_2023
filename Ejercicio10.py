#EJ  Pedir números enteros en un ciclo mientras sean positivos y en caso deque un número sea negativo cerrar el ciclo y al final promediar los números positivos ingresdos por el usuario.


numeros = []
numero = int(input("Ingrese un número entero positivo: "))

while numero >= 0:
    numeros.append(numero)
    numero = int(input("Ingrese un número entero positivo: "))

if numeros:
    average = sum(numeros) / len(numeros)
    print("El promedio de los números positivos ingresados es:", round(average,2))
else:
    print("No se ingresaron números positivos.")
