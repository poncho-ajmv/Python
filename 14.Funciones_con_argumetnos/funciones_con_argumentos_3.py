import os 
os.system('clear')

'''
script en Python que implemente una función que haga el cálculo del
IMC del usuario.La función debe recibir el pesoyla estatura del
usuarioycomo resultado regresa el valor de índice de masa corporal.
'''

def calcula_imc(peso, altura):
    res = peso / altura **2
    return res

peso = float(input('INgrese el pesopor favor: '))
altura = float(input("Ingrese la altura en cm por favor: "))
print(calcula_imc(peso, altura))

