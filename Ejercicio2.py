# Ejercicio 2 Calcular el área y perímetro de un círculo.

#entrada de datos 
radio= float(input("escribe radio: "))
area= 0
perimetro= 0

#constante
PI=3.14



#procesos 
area= (PI)*(radio**2)
perimetro= 2*PI*radio

#salidas 
print("escribe area circulo: ", area)
print("escribe perimetro circulo: ", perimetro)
