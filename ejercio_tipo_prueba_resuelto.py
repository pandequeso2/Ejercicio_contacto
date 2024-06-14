#Ejercicio tipo prueba 3
import os,time

trabajadores = []
cargos =tuple("CEO",'Desarrollador'," Analista")#0: CEO,1: Desarrollador,2: Analista
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
        print('1: REGISTRAR TRABAJADORS')
        nombre_apellido=input('Ingrese nombre y apellido: ')
        cargo=int(input('Ingrese cargo(1.CEO 2. Desarrollador 3. Analista): '))
        sueldo_bruto=int(input('Ingrese suledo bruto: '))
        desc_salud=int(sueldo_bruto * 7/100)
        desc_afp=int(sueldo_bruto * 12/100)
        sueldo_liquido=sueldo_bruto - desc_salud - desc_afp
        trabajador=[nombre_apellido,cargos[cargo- 1],sueldo_bruto,desc_salud,desc_afp,sueldo_liquido]
        trabajadores.append(trabajador)
    elif opc==2:
        pass
    elif opc==3:
        pass
    else:
        print('Adioos') 
    time.sleep(3) 