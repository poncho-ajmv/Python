'''
Crea un scrip en python qeu dentro de un procedimiento soliucite el nombre y la edad
 del usuario y en caso de ser mayor o igual que 18 le indique que es mayuor de edad, en caso 
 contrario indicarle que aun es menor
'''



def comprobacion():
    name = input('Por favor ingrese el nombre de la persona: ')
    edad = int(input("POr favor ingrese la edad de la persona: "))
 
    if (edad >=18):
        print(f'{name} es mayor de edad, ENTRADA ACEPTADA')
    elif (edad <18 and edad>=0):
        print(f'{name} es menor de edad, ENTRADA DECLINADA')
    else:
        print("RESPUESTA NO VALIDA")


comprobacion()

