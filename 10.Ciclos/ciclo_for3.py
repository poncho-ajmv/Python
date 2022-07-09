'''
Crea un programa que muestre una cuenta regresiva usando un ciclo for y esperando un segunod entre cada numero'''

import os
import time
os.system('clear')
print("Desarma la bomba o vas a morir")
for i in range(10, 0, -1): #10 donde incicia a contar, 0 donde acaba de contar(mitad), -1 como se va restando 
    print(i)
    time.sleep(1)


print('Boom!!!')