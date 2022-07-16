'''
Crea una funcion encargada de converitr grados en fahrenheit a celsius 
'''
import os
os.system('clear')

#Fuincion para Fahrenheit
def fahrenheit_a_centi():
    fah = float(input('Por favor ingresa los fahrenheit: '))
    cel = ((fah-32)/1.8)
    print(f"La conversion es\nFahrenheti: {fah} a Celsius: {cel} ")
    

#Funcion para Celsius
def centri_a_fahre():
    cel = float(input('Por favor ingresa los cenritgratos: '))
    fah =((cel *1.8) + 32)
    print(f"La conversion es\nCelsius: {cel}  a Fahrenheti: {fah} ")


print('Bienvenido al convertidor escoge ')
var = int(input('1. Fahrenheit a Celcius\n2. Celcius a Fahrenheit\n3.Salir\nIngrese su opcion: '))

dato = False
while(dato == False):
    if(var == 1):
        fahrenheit_a_centi()
        pass
    
    elif(var ==2):
        centri_a_fahre()
        break

    elif(var == 3):
        print("Se esta saliendo del programa")
        dato = True 
        
    else:
        print("Ha ocurrido un error, intentelo de nuevo")





#Version 2 mas corta pero mas simple


def fa_a_cel():
    f = float(input('Grados a fahrenheit: '))
    c = (f-32)/1.8
    return c

print("El programa convierte f a c")
celci = fa_a_cel()
print(f'Celcius {celci :.2f}')

