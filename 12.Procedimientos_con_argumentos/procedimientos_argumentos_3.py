

"""script en Python que implemente un procedimiento dentro del cual se
muestre la tabla de multiplicar de un número recibido como argumento.
El procedimiento contará con un segundo argumento que indicará hasta
qué múltiplo se mostrará la tabla de multiplicar.Ese segundo
argumento tendrá como valor por omisión el número 10.
"""
import os 
os.system('clear')

num_tabla = int(input('Por favor ingrese la tabla que necesita ver: '))
limite_tabla = int(input('Por favor ingrese el dato del limite de la tabla: '))


def tabla(num_tabla, limite_tabla):
    print(f'Bienvenidos a la tabla de multiplciar del {num_tabla}\n')
    for i in range(limite_tabla):
        res = num_tabla * i
        print(f'{i} * {num_tabla} = {res}')
        
print('\nEl programa ha finalizado.')
tabla(num_tabla, limite_tabla)
