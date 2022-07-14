'''
Procedimeintos 
def identificador(argumetnos):
    instruciiones
'''
import os 
os.system("clear")

def saludo(nombre):#Esto se vuelve una variable local de esta funcion
    print(f'Hola {nombre} gusto  de conocerte')



name = input("Bienvenido ingresa cual es tu nombre: ")
saludo(name)
