import Campers
import trainers
import cordinador
import os
def clear():
    if os.name == 'nt':
        os.system('cls')        # Funcion para limpiar la terminal
    else:
        os.system('clear')
while True:
    clear()
    print("\033[1;30m-----------------------")
    print("       Campuslands     ")
    print(" seguimiento academico ")
    print("-----------------------")
    print("                       ")
    print("  ¿Que tipo de usuario desea ingresar?  ")
    print("1. Camper / 2. Trainer / 3. Coordinacion")
    tipo_de_usuario=int(input("--> "))   #Elegir a que parte del menu desea moverse

    if tipo_de_usuario==1:
        Campers.campers()

    if tipo_de_usuario==2:
        trainers.trainers()

    if tipo_de_usuario==3:
        cordinador.cordinador()
        


