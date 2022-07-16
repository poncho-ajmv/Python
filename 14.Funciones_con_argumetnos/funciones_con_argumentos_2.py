import os 
os.system('clear')

'''
Calcula el IMC de una persona con una funcion con argumentos
'''


peso = float(input('Por favor ingresa tu peso: '))
altura = float(input('Por favor ingresa tu altura: '))

def calculo_imc(peso, altura):
    res = peso / altura **2
    return res

print(f'El resultado del IMC es: {calculo_imc(peso, altura)}')
