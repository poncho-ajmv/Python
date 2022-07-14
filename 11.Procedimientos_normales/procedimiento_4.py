'''procedimientos_4.py
script en Python que muestre un menú cíclico;dicho menú será
implementado en un procedimiento.
Esto es lo que hace es simular un meno de cuando uino compra un cd y debe de colocar los subtitulso 
'''
import os
import time 

ESP =1
ING =2 
NO_SUBS=3
SALIR =4

def mostrar_menu():
    print("Bienvenido al programa de subtitulos\n1. ESP =1\n2. ING=2\n3. NO_SUBS=3\n4. SALIR=4")

cont=True 

while cont:
    os.system("clear")
    mostrar_menu()
    dato = int(input('Por favor ingresa el dato a escoger: '))
    if(dato == 1):
        print('Se tomo la opcion de subtitulos en espaniol')
        time.sleep(1)
    elif(dato == 2):
        print('Se tomo la opcion de subtitulos en ingles')
        time.sleep(1)
    
    elif(dato == 3):
        print('Se tomo la opcion de ningun subtitulo')
        time.sleep(1)

    elif(dato == 4):
        print('Se esta saliendo de esta opcion.')
        cont=False
        time.sleep(1)
    else:
        print('La opcion a escoger no fue permitida intentelo de nuevo.')
