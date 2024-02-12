import json
import os
import campers
import coordinador
# ********************************************
# ********************************************
# Proyecto campuslands "python" 9 de febrero *
# ********************************************
# ********************************************
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
# Abrir el archivo JSON
with open('datos.json', 'r') as datos:
    # Cargar el contenido del archivo en un diccionario
    inscrip = json.load(datos)

with open('grupos.json', 'r') as grups:
    # Cargar el contenido del archivo en un diccionario
    grupos = json.load(grups)
with open('grupos.json', 'r') as gruposs:
    # Cargar el contenido del archivo en un diccionario
    grupos = json.load(gruposs)
print("\033[1;37m##############################")
print("# Bienvenido a Campuslands   #")
print("#  (Centro de formacion)     #")
print("##############################")
input("---> Enter para entrar <---")
while True:
    clear()
    inscritos = inscrip["inscripcion"]["Inscritos"]
    aprobados = inscrip["inscripcion"]["aprobados"]
    reprobados=inscrip["inscripcion"]["reprobados"]

    print("Que tipo de usuario desea ingresar?")
    print("1. Camper\t2. Trainer\t3. Cordinador")

    Decision1=int(input("--> "))



    ######################### Campers #########################
    if Decision1==1:
        print(campers.campers())
        ######################### Trainers #########################
    elif Decision1==2:
        clear()
        print("")


        ######################### Coordinador #########################
    elif Decision1==3:
        print(coordinador.coordinador())
        
## Desarrollado por: 
##Eduar Damian Chanaga Gonzalez - 1095581647
##Andres Pedraza Peña - 1005331114
                

