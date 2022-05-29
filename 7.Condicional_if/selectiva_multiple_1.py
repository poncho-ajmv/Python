"""
EStructura selectiva multiple
(if  elif else)
"""
"""
if condicion
    instruciones
elif condicion
    instruciones alter
else condicon   #Si se agruega un else siempre tiene que ser el ultimo
    instruciones final
"""

'''Se tiene que crear un programa que ingrese la edad, nombre, notas y asistencia.
El programa tiene que indicar si aprobo o no y un minimo de asistenicas.
USted debe de poner ese limite, solamente son aceptados los numeros del 1 al 100'''

# Nota  minima 61
# Asistenia minima 50%

from xml.dom.minidom import Notation


print("\nBienvenido al programa")

#name  = input("Ingresa tu nomrbe: ")
#edad = input("Ingresa la edad: ")

nota = int(input("INgrese cunto fue su nota: "))
asist = int(input("INgrese cunto fue su asistenica: "))

if(nota >=0 and nota <=100)and(asist >=0 and asist <=100):
    if(nota>=61) and (asist >=10):
        print("Felicitaciones, tines esperanza")
    elif((nota<=61) and (asist <=10)):
        print("TIenes que ponerte las pilas")
    else:
        print("FAllaste en una de las dos, mejora!")
else:
    print("Los datos introducios son incorrectos intentelo de nuevo")



