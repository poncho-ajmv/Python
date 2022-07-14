"""repetitiva_desde_e.py
script en Python que muestre un cronómetro en formato de 24 horas.
El despliegue seguirá el formatoh:m:s.El cronómetro deberá iniciar
en0:0:0ypodrá llegar hasta 23:59:59.Implementar retardos de
1segundoylimpieza de pantalla de forma tal que sólo se vea un
tiempo en pantalla."""

import os
import time #se importa toda la funcion
from time import localtime #Solamente es la funcion
os.system("clear")
#


for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            os.system("clear")
            print(f'{hora}:{minuto}:{segundo}')
            time.sleep(1)

