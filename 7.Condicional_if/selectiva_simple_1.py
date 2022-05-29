'''Estructura selectiva simple (IF)'''

#Esto ya es programacion estructurada
'''
if condicion:
    instrucciones
script en pyhton que solicite la edad del usuaio y si esa edad es myo o 
igual que 18 indicarle que ya es mayor de edad.
'''
#Este es un ejemplo del programa. 

edad = int(input('Ingresa tu edad: '))
if (edad>=18):
    print('La perseona es mayor de edad')
    print('Un gran poder conlleva una gran responsabilida.')
elif(edad<18):
    print('La persona es menor de edad')
else:
    print('Error dato invalido')