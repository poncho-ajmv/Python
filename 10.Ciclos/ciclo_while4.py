import os 
os.system("clear")

'''
script en Python que muestre un menú con distintos personajes de un
videojuego.Si el usuario selecciona alguno de los personajes,se le
mostrarán sus características.El menú será cíclicoyse mostrará
mientras el usuario no indique que desea salir.
'''
var = False
while(var == False):
    print('\nBienvenido al menu\n1. Para personajes\n2. Para salir')
    num = int(input("Ingrese su opcion: "))
    if(num==1):
        print('\n1. Mago \n3.Caballero \n3. Arquero\n4. Terminar el programa')
        dato = int(input("Indica que personaje necesitas: "))
        if(dato ==1):
            print("Se selecciono el mago")
        elif(dato ==2):
            print("Se selecciono el CAballero")
        elif(dato == 3):
            print("Se seleciono el arquero")
        elif(dato ==4 ):
            print('El programa esta finalizando')
            var = True
        else:
            print('Se tuvo un error intentlo de nuevo')

    elif(num==2):
        print('\nSe regresara al menu')
    else:
        print('Se debe a un error')
