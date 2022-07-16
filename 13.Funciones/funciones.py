'''
def ideantificador():
    instrucciones
    return valor_retorno

    Las funciones tienen un valor de retornio.
'''
import os
os.system('clear')

print('Area de un triangulo')

#Version 1

def area_triangulo():
    base = float(input("INgrese la base del triangulo: "))
    altura = float(input('Ingresa la altura del triangulo: '))
    area = base * altura / 2
    return area 

print(f'El area es igual a {area_triangulo()}')


#Version2 

base = float(input("INgrese la base del triangulo: "))
altura = float(input('Ingresa la altura del triangulo: '))
def area(dato, sa):
    area = base * altura / 2
    return area 

print(area(base, altura))

