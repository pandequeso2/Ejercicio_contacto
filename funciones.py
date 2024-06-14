# funciones



trabajadores = []
cargos =tuple("CEO",'Desarrollador'," Analista")#0: CEO,1: Desarrollador,2: Analista
def Registrar_trabajador():
    print('1: REGISTRAR TRABAJADORS')
    nombre_apellido=input('Ingrese nombre y apellido: ')
    cargo=int(input('Ingrese cargo(1.CEO 2. Desarrollador 3. Analista): '))
    sueldo_bruto=int(input('Ingrese suledo bruto: '))
    desc_salud=int(sueldo_bruto * 7/100)
    desc_afp=int(sueldo_bruto * 12/100)
    sueldo_liquido=sueldo_bruto - desc_salud - desc_afp
    trabajador=[nombre_apellido,cargos[cargo- 1],sueldo_bruto,desc_salud,desc_afp,sueldo_liquido]
    trabajadores.append(trabajador)


def Listar_trabajadores():
    print('LISTAR TRABAJADORES. ')
    if len(trabajadores)==0:
        print('Lista vacia, registre un trabajador en la opcion 1.. ')
    else:
        print('\tLista de trabajadores: ')
        for t in trabajadores:
            print(f'Nombre: {t[0]}\nCargo:{t[1]}\nBruto: {t[2]}\nSalud {t[3]}\nAFP: {t[4]}\nLiquido: {t[5]}\n')
            

def Exportar_archivo_txt():
    pass

def Salir():
    print('Adioos') 
    exit()

#PUEDES HACER MAS FUNCIONES
