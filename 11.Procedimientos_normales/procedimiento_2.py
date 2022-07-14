#crea una funcion que solicite el nombre del usuairo y saludde de una manera pesonalizada\
import os
os.system("clear")

def saludo_pesonalizado():
    name = input('Cual es tu nombre: ')
    print(f"Bienvenido al programa, {name}")

saludo_pesonalizado()