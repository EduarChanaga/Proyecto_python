import os
import opcionescampers
import opcionestrainers
import opcionesrutas
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
        print("3. Rutas de entrenamiento")
        print("4. Reportes")
        opciones_cordinador=int(input("--> "))



        if opciones_cordinador==1:  #opciones campers
            clear()
            print("1. Inscripcion") 
            print("2. Matriculas")    
            print("3. Ingreso de notas")    
            opciones_campers=int(input("--> ")) 
            if opciones_campers==1:
                print(opcionescampers.inscripcion())
            elif opciones_campers==2:
                print(opcionescampers.matriculas())
            elif opciones_campers==3:
                print(opcionescampers.ingreso_de_notas())





        elif opciones_cordinador==2:#opciones de los trainers
            print("1. Ingreso de trainer") 
            print("2. Ver rutas segun trainers")    
            print("3. Ver informacion de trainer")    
            opciones_trainers=int(input("--> ")) 
            if opciones_trainers==1:
                print(opcionestrainers.ingreso_trainer())
            elif opciones_trainers==2:
                print()
            elif opciones_trainers==3:
                print(opcionescampers.ingreso_de_notas())()



        elif opciones_cordinador==3:
            print("1. Crear grupo") 
            print("2. Ver grupos")    
            print("3. Ver informacion de trainer")    
            opciones_rutas=int(input("--> ")) 
            if opciones_rutas==1:
                print(opcionesrutas.crear_grupo())
            elif opciones_rutas==2:
                print()
            elif opciones_rutas==3:
                print()



        elif opciones_cordinador==4:
            clear()
