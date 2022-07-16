'''
script en Python que implemente un procedimiento para saludar al usuari
de manera personalizada;el procedimiento deberá recibir el nombre del
usuario como argumento.Se deberá crear otro procedimiento llamado
"main"desde el cual se inicie la ejecución del programaydentro del
cual se solicite el nombre del usuarioyse utilice el primer
procedimeinto descriot 
'''
import os 
os.system('clear')
def saludo_personalizado(nombre):
    print(f'Gusto de verte {nombre}')

def main():
     usuario = input('Hola como te llamas: ')
     saludo_personalizado(usuario)

if __name__ == '__main__':
    main()

'''
Procedimientos la cual no necesita el resultado de un valor

Funciones la que ayuda a realizar calculos, la cual da varios valores. 
'''

