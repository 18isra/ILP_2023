#EJ Obtener un número y determinar lo siguiente:
# si es negativo y mayor a -100 imprimir los números impares de forma DESCENDENTE
# si es positivo y menor a 100 mostrar los números pares de forma ASCENDENTE
# en otro caso imprimir No Válido
#datos entrada
numero=int(input("ingresa un numero: "))

#procesos 
if numero<0 and numero>-100:
    print("numeros impares descendentes: ")
    for i in range(abs(numero),0,-2):
     print(i*1)

elif numero>0 and numero<100:
    print("numeros pares ascendentes: ")
    for i in range(0,numero+1,2):
        print(i)

else:
    print ("no valido: ")

