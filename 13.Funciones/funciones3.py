#"Programa con funciones que calucle la masa corporal de la persona"
#se debe de realizar con funciones y enviandole argumentos 

#'IMC = PESO/ESTATURA^2'

'''
#version1
def masa_corporal(peso, se):
    res = peso / (estatura * estatura)
    return res


print('Bienvenido al calculo de masa corporal')
peso = float(input('Por favor ingresa tu peso'))
estatura = float(input('Por favor ingresa tu altura'))

print(masa_corporal(peso, estatura))
'''

#version 2

def calcular_IMC():
    pe = float(input('Por favor ingresa tu peso: '))
    sta = float(input('Por favor ingresa tu altura: '))
    resultado = pe / (sta **2)
    return resultado

imc = calcular_IMC()
print(f'El resultado del IMC de la persona es: {imc :.2f}')#Esto es para limitar cuantos puntos decimales se desean ver.


