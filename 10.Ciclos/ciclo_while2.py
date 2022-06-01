'''
Escribe un script
script en Python que sume valores pares y multiplique valores impares
mientras el usuario no ingrese un 0. Se deberá utilizar la estructura
repetitiva"mientras"para solicitar al usuario un númeroy
dependiendo del número lo sumaolo multiplica.
 if(dato == 1):
        print('SUma')
        num = int(input('\nPor favor ingresa el primer dato: '))
    elif(dato==1):
        print('multiplicacion')
        num = int(input('\nPor favor ingresa el primer dato: '))

'''

num = int(input('\nPor favor ingresa el primer dato: '))

while(num != 0):
    dato = num%2
    print(dato)
    if(dato == 1):
        print('SUma')
        num = int(input('\nPor favor ingresa el primer dato: '))
    elif(dato==0):
        print('multiplicacion')
        num = int(input('\nPor favor ingresa el primer dato: '))

   