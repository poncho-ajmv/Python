from ctypes.wintypes import HLOCAL
import os
os.system('clear')

"""Se debe de ingresar una palabra e imprimir como el ejemplo
Hola >>
H
o
l
a
"""

frase = input('Ingrese una frase o palabra: ')

print('Los simbolos de lo ingresado es: ')

for i in frase:
    print(f'{i}')
print('\nEl programa ha finalizado. ')