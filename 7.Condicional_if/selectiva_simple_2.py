'''
Un programa que genere un numero aleatorio entre 1 y 10
y le pida al usuario que intente adivinarlo.
'''
#Aqui se agrega la libreria.
import random
sec = random.randint(1,10)

num = int(input("Por favor ingresa el numero: "))
if(num == sec):
    print("El numero es el mismo felicidades")
else:
    print("El numero esta equivocado")
