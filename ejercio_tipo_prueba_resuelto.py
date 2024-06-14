#Ejercicio tipo prueba 3
import os,time
from funciones import *


while True:
    os.system('cls')
    print('Menú trabajador. ')
    print('1: Registrar trabajador. ')
    print('2: Listar todos los trabajadores. ')
    print('3: imprimir panilla de suedos ')
    print('4. Salir. ')
    opc=int(input('Ingrese una opción: '))
    os.system('cls')
    if opc==1:
        Registrar_trabajador()
    elif opc==2:
        Listar_trabajadores()
    elif opc==3:
        Exportar_archivo_txt()
    else:
        Salir()
    time.sleep(3) 