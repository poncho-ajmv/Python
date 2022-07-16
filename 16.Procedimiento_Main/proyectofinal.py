'''
script en Python que implemente un programa para realizar las siguiente:
conversiones:
 -segundosaminutos:recibe segundos y devuelve minutos y egundos
 -segundosahoras:recibe segundos y regresa horas,minutos y segundos
 -minutosasegundos:recibe minutos y segundos y regresa segundos
 -minutosahoras:recibe minutos y segundos y regresa horas minutos y
   segundos
Además deberá implementarse un método para imprimir el menú de opciones
yla ejecución del programa debe comenzar desde el procedimiento"mair
El programa debe seguir en ejecución mientras el usuario no decida
salir.
'''
import os 
import time 

def seg_min_y_horas(seg):
    min = seg/60
    hora =seg /3600
    return min, hora


def min_a_seg(min):
    seg = min*60
    return seg

def min_todo():



def main():
    os.system('clear')
    print("Bienvenido a conversiones\n1. Segundos a minutos\n2. Segundos a horas\n3. minutos a segundos\n4. Minutos a holras\n5. Salir")
    opcion = int(input("Por favor ingresa la opcion a elegir: "))
    if(opcion ==1):
        seg = int(input('Por favor ingresa los segundos: '))
        minutos, hora = seg_min_y_horas(seg)
        minutos = str(minutos)
        minutos =minutos.replace(".", ':')
        print(f'El resultado es: {minutos} minutos')
        time.sleep(1)
        main()

    elif(opcion ==2):
        seg = int(input('Por favor ingresa los segundos: '))
        minutos, hora = seg_min_y_horas(seg)
        hora = str(hora)
        hora =hora.replace(".", ':')
        print(f'El resultado es: {hora} horas')
        time.sleep(1)
        main()
        
    elif(opcion ==3):
        min = float(input('Por favo ingresa los minutos: '))
        segundos = min_a_seg(min)
        print(f'El resultado es: {segundos:.0f} segundos')
        time.sleep(1)
        main()

    elif(opcion ==4):
        #Pendiente de implementar la funcion. 
        time.sleep(1)
        main()

    elif(opcion==5):
        print("El programa ha finalizado")
        exit()
    else:
        print("Ha ocurrido un error, intentelo de nuevo")
        time.sleep(1.5)
        main()


if __name__== "__main__":
    main()

