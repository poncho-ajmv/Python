import os
os.system("clear")

'''Crea un programa en python que muestre la tabal de multiplicada de un numero
ingresado por el usaurio. el usuari tamnbien odra ingresar hasta que valor llegar ala tabla de multiplicar.'''

tabla = int(input('INgrese el numero de la tabla de multiplicar: '))
limite = int(input('Ingrese el limite de la trabla: '))

for i in range(0, limite+1):
    print(f'{i} x {tabla} = {i*tabla}')
print('El programa ha finalizado muchas gracias')



