'''
Implemente un sistema de redondeo de clasificaciones.
El usuairo es el cargado de ingresar su calsificaion, si le faltan 4 unidades
o menos para el siguiente muiltiplide 10, entonces su clasificaion sera 
redondeada al siguiente multiplo de 10 en caso contrario la clasificacion no es
modificada.

SE debe de redondear. 
'''

clasificacion = int(input("INgrese su clasificacion: "))
residuo = clasificacion % 10

if(clasificacion >= 6):
    clasificacion = clasificacion + (10 - residuo)
    print(f'La clasificacion final es: {clasificacion}')
else:
    print(f'LA clasificacion es: {clasificacion}')