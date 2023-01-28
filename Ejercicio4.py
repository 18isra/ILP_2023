#Ej. Pedir la cantidad de grados y convertirlos a °C, °F y K.

#entrada 
GRADOSCELCIUS=float(input("cantidad grados: "))

#proceso
grados_f = (GRADOSCELCIUS*1.8)+32
grados_k= GRADOSCELCIUS+273.15




#salida
print("los grados son:",GRADOSCELCIUS, "°c")
print("los grados son:", grados_f, "°f")
print("los grados son:", grados_k, "°k")



