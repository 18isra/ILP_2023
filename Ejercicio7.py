#EJ 7. Pedir el nivel del agua en metros de una cisterna

#entrada
nivel_agua=int(input("nivel de agua: "))

#procesos
if nivel_agua <0:
    print("fuga de cisterna")
elif nivel_agua ==0:
    print("encender bomba de agua")
elif nivel_agua>=0 and nivel_agua<2:
    print("acelerar bomba de agua")
elif nivel_agua>=2 and nivel_agua<4:
    print("bomba trabajando""!")
elif nivel_agua>=4 and nivel_agua<6:
    print("desacelerar bomba")
elif nivel_agua==6:
    print("apagar la bomba")
#else
elif nivel_agua>6:
    print("desabordamiento de agua en cisterna")
