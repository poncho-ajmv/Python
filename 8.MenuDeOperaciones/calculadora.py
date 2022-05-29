
#Se debe de crear un programa de calculadora 
print('''
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Division Entera
6) Modulo
7) Potenica
''')

print('\nBienvenido a la calculadora basic')
cal = int(input("Por favor ingrea la opcion a escojer:"))
num1 = int(input('Ingresa el primer dato: '))
num2 = int(input('Ingrese el segudno dato: '))

if(cal == 1):
    total = num1 + num2
    print(f"El resultado es {total}")
elif(cal ==2):
    total = num1 - num2
    print(f"El resultado es {total}")

elif(cal ==3):
    total = num1 * num2
    print(f"El resultado es {total}")

elif(cal ==4):
    total = num1 / num2
    print(f"El resultado es {total}")

elif(cal ==5):
    total = num1 // num2
    print(f"El resultado es {total}")

elif(cal ==6):
    total = num1 % num2
    print(f"El resultado es {total}")

elif(cal ==7):
    total = num1 ** num2
    print(f"El resultado es {total}")

else:
    print("Se ingreso una opcion no valida")