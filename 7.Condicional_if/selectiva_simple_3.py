"""
Crear un programa que solicite la clasificacion y la asistenica de la persona
para que pueda ganar el curso.
"""

clasifi = int(input('\nIngresa la clasificacion final de la persona: '))
asiste = int(input('Ingresa a cuantas clases asistio el alumno: '))

if(clasifi >=60)and(asiste >=20):
    print("Usted paso la materia")
    if(clasifi >=95):
        print('Eres increible sigue asi')
else:
    print('La persona no paso la materia')