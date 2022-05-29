"""
Crea un programa que muestre un menu con los nombres de
los paises y si seescoje una opcion se mostrara la capital
"""

print("Capitales\n1.Mexico\n2.Guatemala\n3.USA\n4.Argentina")
capital = input("Ingresa la capital: ")
capital = capital.lower()

if(capital == "mexico"):
    print("CDMX")
elif(capital == "guatemala"):
    print("Cuidad de Guatemala")
elif(capital == "usa"):
    print('Washington D. C.')
elif(capital == "argentina"):
    print("Buenos Aires")
else:
    print("Ingreso un dato invalido.")


