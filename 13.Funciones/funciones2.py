import os 
os.system('clear')


def puntuacion(alu_1, alu_2, alu_3):
    #Funcion que pida los dato para el promedio
    return (alu_1 + alu_2 + alu_3) /3

media = puntuacion(7,8,9) 

print(f'La puntuacion del alumno es: {media}')