import os
import opcionescampers
import opcionestrainers
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
                print()
            elif opciones_campers==3:
                print(opcionescampers.ingreso_de_notas())





        elif opciones_cordinador==2:#opciones de los trainers
            print("1. Ingreso de trainer") 
            print("2. Ver rutas segun trainers")    
            print("3. Ver informacion de trainer")    
            opciones_campers=int(input("--> ")) 
            if opciones_campers==1:
                print(opcionestrainers.ingreso_trainer())
            elif opciones_campers==2:
                print()
            elif opciones_campers==3:
                print(opcionescampers.ingreso_de_notas())()



        elif opciones_cordinador==3:
            clear()



        elif opciones_cordinador==4:
            clear()
