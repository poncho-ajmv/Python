"""
Es cuando ponemos una estructura de control adentro de otra estructura de control 
Crea un programa que simula un juego de preguntasy respuestas 
el usuario contesta correctamente una preguna puede continuar 
con la siguente en cas ode fgallar se le indica que ha perdido,
Si contesta se le feclicita.
"""

print("\nBienvenido al program")
resp = input("Por favor ingresa la palabra 1")
if(resp == '1'):
	print('Respuesta correcta')
	resp = input("Por favor ingresa la palabra 2")
	if(resp == '2'):
		print('Respuesta correcta')
		resp = input("Por favor ingresa la palabra 3")
		if(resp == '3'):
			print('Respuesta correcta')
			

		else:
			print("La respuesta fue incorrecta")
	else:
		print("La respuesta fue incorrecta")
else:
	print("La respuesta fue incorrecta")
