'''
def identifiacdor(por_posicion, *args, **kwargs):
    isntrucciones
'''
'''
def suma(*args #args): #Esto se pone como argumetnop == args #El asterisco dice al interprete de python que esta funcion puede tener ene cantidad de argumentos
#Esto lo convierte en una tupla 
    print(argumetno)
    print(type(argumento)) #Esto nos dice que tipo de dato es. 

res = suma(10, 50, 60)
print(res)
'''

#Ejemplo 1
#UN * nos regresa una tupla


def suma(*args):
    resultado = 0
    for i in args:
        resultado = resultado + i
    return resultado


resultado = suma(1,2,3,4,5,6,7,8,9)
print(resultado)

#Ejemplo 2
#**nos devuelve un dicionario

def suma(**kwargs):
    valor = kwargs.get('valor', No contiene el valor)
    print(valor)

res = suma(valor = 'Eduardo', x = 3, y = 9, z = True)
print(resultado)


#recordatorio 

*  --> n valores -> Tuplas
** --> n valores -> dicionarios