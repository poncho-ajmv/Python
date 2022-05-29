"""
Crea un programa en python que inidaca el termomento y si el valor se encuentra  entre 18 a 27 grados
"""

print("Bienvenido al programa")
temp = int(input("Ingresa la temperatura por favor: "))

if(temp >=18) and (temp <=27):
    print("La temperatura ambiente es agradable")
elif(temp <=18) or (temp >=27):
    print("La temperaruta no es agradable")
else:
    print("OCurrio un error")
