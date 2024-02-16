import Campers
import trainers
import cordinador
import os
import reportes
def clear():
    if os.name == 'nt':
        os.system('cls')        # Funcion para limpiar la terminal
    else:
        os.system('clear')
while True:
    clear()
    print("\033[1;30m" + "-" * 25)
    print("\033[1;30m" + "|      \033[1;37mCampuslands     \033[1;30m|")
    print("\033[1;30m" + "| \033[1;37mSeguimiento Académico \033[1;30m|")
    print("\033[1;30m" + "-" * 25)


    print("                       ")
    print("¿A que modulo desea ingresar? ")
    print("1. Camper       / 2. Trainer ")
    print("3. Coordinacion / 4. Reportes")
    print("5. Cerrar")
    tipo_de_usuario=str(input("--> "))   #Elegir a que parte del menu desea moverse
    clear()
    if tipo_de_usuario=="1":
        Campers.campers()

    if tipo_de_usuario=="2":
        trainers.trainers()

    if tipo_de_usuario=="3":
        cordinador.cordinador()
    if tipo_de_usuario=="4":
        print(reportes.reportes())
    if tipo_de_usuario=="5":
        break
        

#hola campers


