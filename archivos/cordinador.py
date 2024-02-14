import os
import opcionescampers
import opcionestrainers
import opcionesrutas
import reportes
def clear():
    if os.name == 'nt':
        os.system('cls')        # Funcion para limpiar la terminal
    else:
        os.system('clear')



def cordinador():
    clear()
    while True:
        print(" ¿Que desea realizar? ")
        print("1. Ver opciones sobre los campers")
        print("2. Ver opciones sobre los trainers")
        print("3. Grupos (creacion, vista...)")
        print("4. Reportes")
        print("5. salir")
        opciones_cordinador=int(input("--> "))
        clear()



        if opciones_cordinador==1:  #opciones campers
            clear()
            print("1. Inscripcion ( Autorizar campers para realizar la prueba de ingreso)")    
            print("2. Ingresar la nota de los campers que se han registrado")   
            print("3. Matriculas ( Asignar grupo a camper Aprobado)")  
            print("4. salir")
            opciones_campers=int(input("--> ")) 
            if opciones_campers==1:
                print(opcionescampers.inscripcion())
            elif opciones_campers==2:
                print(opcionescampers.ingreso_de_notas())
            elif opciones_campers==3:
                print(opcionescampers.matriculas())
            elif opciones_campers==4:
                print()
                clear()





        elif opciones_cordinador==2:#opciones de los trainers
            print("1. Ingreso de trainer") 
            print("2. Ver rutas segun trainers")    
            print("3. Ver informacion de trainer")    
            print("4. salir")
            opciones_trainers=int(input("--> ")) 
            clear()
            if opciones_trainers==1:
                print(opcionestrainers.ingreso_trainer())
            elif opciones_trainers==2:
                print()
            elif opciones_trainers==3:
                print(opcionescampers.ingreso_de_notas())()
            elif opciones_trainers==4:
                print()
                clear()



        elif opciones_cordinador==3:
            print("1. Crear grupo") 
            print("2. Ver grupos")    
            print("3. Ver informacion de trainer")    
            print("4. salir")
            opciones_rutas=int(input("--> ")) 
            clear()
            if opciones_rutas==1:
                print(opcionesrutas.crear_grupo())
            elif opciones_rutas==2:
                print(opcionesrutas.ver_grupos())
            elif opciones_rutas==3:
                print()
            elif opciones_rutas==4:
                clear()



        elif opciones_cordinador==4:
            print(reportes.reportes())
        elif opciones_cordinador==5:
            clear()
            return