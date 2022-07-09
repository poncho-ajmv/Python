import os
import random

os.system('clear')
'''
IMplemente el juego de adivinar un numero aleatorio del 1 al 100
Debe de ser en un modo competitivo.
DEbe de ser  intelignete el juego se realizara por turnos primero la mquina
y despues para ganar el juego se realizara por turnos, la maquina y 
despues el usuario y por cada intento la computadora respondera si 
el es mayor o menor que el secreto.
'''

print('Bienvenidos al juego aleatrorio')
print('Cada jugador tiene un turno el que le atine es el ganador\n')

inferior = 1
superior = 100
secreto = random.randint(1,100)
usuario = -1
maquina = -1

os.system("clear")
while usuario != secreto and maquina != secreto:
    maquina = random.randint(inferior, superior)
    
    print("===========================\n")
    print(f"DATO A ENCONTRAR: {secreto}")
    print(f"USuario: {usuario}")
    print(f'MAquina: {maquina}')
    print(f"Inferior: {inferior}\nSuerior: {superior}")


    if maquina < secreto:
        print("El numero es menor")
        inferior = maquina + 1
    elif maquina > secreto:
        print("EL numero es mayor")
        superior = maquina -1
    else:
        print(" HA ganado la maquina")


    if maquina != secreto:
        usuario = int(input("Ingresa el numero: "))
        if(usuario < secreto):
            print("EL numeor es menor")
            if usuario > inferior:
                inferior = usuario +1
        elif(usuario > secreto):
            print("Tu numero es mayor")
            if (usuario < inferior):
                superior = usuario - 1
        else:
            print("El usuario ha ganado")

         #   5:3