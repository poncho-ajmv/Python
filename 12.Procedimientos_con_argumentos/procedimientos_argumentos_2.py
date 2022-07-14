'''

script en Python que implemente un procedimiento que reciba el nombrey
la edad del usuario y en caso que la edad sea mayor o igual que 18 le
indique que ya es mayor de edad;en caso contrario le indique que es
menor de edad.
'''
import os

os.system("clear")

name = input('Por favor ingresa tu nombre: ')
age = int(input('Por favor ingresa tus anios: ')) 


def verificacion(nombre, anios):
    if anios>=18:
        print(f'{nombre} es mayor de edad')
    elif(anios<18 and anios>=0):
        print(f'{nombre} es menor de edad')
    else:
        print("LA OPCION ESTA INCORRECTA")
    

verificacion(name, age)
