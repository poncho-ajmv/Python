'''
script en Python que implemente una función encargada de convertir una
cantidad de segundosaminutosysegundos.La función deberá recibir
como argumento una cantidad de segundosydeberá regresar la cantidad
de minutosysegundos equivalente.
'''
import os 
os.system('clear')


def minutos_seg(min):
    seg = min *60
    return seg #Se puede tomar en cuenta que se pueden de poner varios return 

def seg_minutos(seg):
    min = seg/60
    return min


print("Bienvenido a convertidor")
print('1. segundos a minutos\n2. minutos a segundos')
esc = int(input('Ingrese la opcion a escoger: '))

if (esc == 1):
    min = int(input('Por favor ingresa los minutos: '))
    minutos_seg(min)
    print(f"Los minutos serian {min} y los segundos serian {minutos_seg(min) :.2f}")

elif(esc ==2):
    seg = int(input('Por favor ingresa los segundos: '))
    seg_minutos(seg)
    print(f"Los segundos serian {seg} y los minutos serian {seg_minutos(seg) :.2f}")
else:
    print("la opcion no es valida, intentelo de nuevo")