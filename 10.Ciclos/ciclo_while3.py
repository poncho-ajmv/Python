'''
repetitiva_mientras_3.py
script en Python que simule el sistema de validación de datos de una
plataforma digital.Se le solicitará al usuario su nombrey
contraseña mientras la información proporcionada no coincida con la
información previamente registrada.
'''
import os #Libreria para poder jugar con la terminal 
os.system("clear")#Esto le manda a la consola que se limpie como un terminal comun en GNU


var = False
while(var == False):
    name = input("\nPor favor ingresa tu nombre: ")
    passw = input("Por favor ingresa tu contrasenia: ")
    if(name == "Kenobi") and (passw == "2003"):
        print('Contrasenia correcta')
        var = True
    elif(name != "Kenobi") and (passw != "2003"):
        print('Contasenia incorecta')
        var = False
    else:
        print('HA ocurido un error intentelo de nuevo')
        var = False
print('El programa ha finalizado felicitaciones')

