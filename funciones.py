#Funciones
import time
desc_salud=0
desc_afp= 0
sueldo_liquido = 0
descuentos = 0 
def menu():
    while True:
        print('''SUELDOS\n 1. Registrar tarabajdor\n 2. Listar los trabajadores\n 3. imprimir plantilla de sueldos\n 4. Salir ''')
        while True:
            try:
                opc=int(input('Ingrese una opción:  '))
                if opc in(1,2,3,4):
                    break
                else:
                    print('ERROR esa opcion no esta en las opciones')
            except:
                    print('INGRESE UN NÚMERO.')   
        if opc==1:
            opcion_1()
        elif opc==2:
            opcion_2()
        elif opc==3:
            opcion_3()
        else:
            opcion_4()
            break

        
def opcion_1(trabajador,matriz):
        print('Registrar trabajador. ')
        nombre=input('Ingrese su nombre: ')
        apellido=input('Ingrese su apellido: ')
        cargo=input('Ingrese su cargo (ceo, desarrollador, analista de datos): ')
        sueldo_bruto=int(input('Ingrese el sueldo bruto: '))
        trabajador= {'nombre':nombre,
                     'apellido':apellido,
                    'cargo':cargo,
                    'sueldo_bruto':sueldo_bruto}
        desc_salud = sueldo_bruto * 0.07
        desc_afp= sueldo_bruto * 0.12
        print('El descuento por la salud es: $',desc_salud)
        print('El descuento por la afp es: $',desc_afp)
        descuentos = desc_afp + desc_salud
        sueldo_liquido = sueldo_bruto - descuentos
        matriz.append([desc_salud,desc_afp,sueldo_liquido])
        time.sleep(2)
        print('Trabajador agregado con exito...')
def opcion_2(p_trabajador):
            print('Listar trabajadores ')
            print(p_trabajador['nombre'],' tiene el cargo de: ',p_trabajador['cargo'],', sueldo bruto :',p_trabajador['sueldo_bruto'], 'el descuento de salud es: $',desc_salud,', el descuento de la afp es: $',desc_afp,' ,el sueldo liquido es: $',sueldo_liquido,'. ')
            time.sleep(3)

def opcion_3(p_trabajador,p_cargo):
        print('Mostrar cargos. ')
        cargo_solicitado = input('Ingrese el cargo que desee buscar: ')
        cargo_solicitado == p_trabajador.values(p_cargo)
        print(cargo_solicitado)
def opcion_4():
    print('Addioos')
    