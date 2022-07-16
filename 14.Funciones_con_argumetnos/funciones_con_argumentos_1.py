import os 
os.system('clear')

'''
def identificador(argumentos):
    instrucciones
    return valor_retorno
'''

'''
script en Python que implemente una función para calcular el área de un
triángulo.Dicha función deberá recibir como argumentos el valor de
la baseyla alturayregresará el área calculada.
'''

def area_traingulo(dato1, dato2):
    res = (dato1 * dato2)/2
    return res

base = float(input('Ingresa la base: '))
altura = float(input('Ingresa la alatura: '))
print(f'El area de un trinagulo es: {area_traingulo(base, altura)}')
