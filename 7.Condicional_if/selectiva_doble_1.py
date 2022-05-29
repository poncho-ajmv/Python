"""
EStructura selectriva doble
if else

if condicion
    instruciones
else:
    instruciones alternativas
"""
"""Crear un login a un usuaio pidiendole la contrasena"""

usuario = "Kenobi"
contra = "High Ground"

name = input("Por favor ingrese el usuario: ")
passw = input("Por favor ingresa la contrasnia: ")

if(name == usuario) and (passw == contra):
    print("Bienvenido al programa")
    print("Llevas la delantera. ")
else:
    print("Estas subestimando mi poder")
