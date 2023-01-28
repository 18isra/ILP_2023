# Ej.  Obtener valores para: a, b y c. Calcular la fórmula general.
import math as m

#entrada 
valor_a=float(input("obtener valor a: "))
valor_b=float(input("obtener valor b: "))
valor_c=float(input("obtener valor c: "))



#procesos 
valor_b_cuadrada= pow(valor_b,2); raiz= m.sqrt(valor_b_cuadrada-(4*valor_a*valor_c))/2*valor_a


#salidas
print("variable x1 es:", (((-valor_b-raiz)/2*valor_a)))
print("variable x2 es:", (((-valor_b+raiz)/2*valor_a)))







