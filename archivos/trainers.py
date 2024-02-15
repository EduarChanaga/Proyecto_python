import os
import json
import ingresonotas
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


###########################################################################################
def trainers():
    clear()
    def cargar_datos():
        with open("info_grupos.json", "r") as file:
            info_grupos = json.load(file)
        with open("trainers.json", "r") as file:
            trainers = json.load(file)
        return info_grupos, trainers

    def obtener_entrenadores(trainers):
        print("Entrenadores disponibles:")
        for trainer in trainers["campers"]["trainers"]:
            print("Nombre:", trainer["Nombre"], "- ID:", trainer["n_identificacion"])

    def obtener_grupos_por_trainer(id_trainer, info_grupos):
        grupos_asignados = []
        for campus, grupos in info_grupos["campus"].items():
            for grupo in grupos:
                if grupo["trainer"]["ID"] == id_trainer:
                    grupos_asignados.append(grupo)
        return grupos_asignados

    def imprimir_grupos(grupos):
        if not grupos:
            print("No se encontraron grupos para este entrenador.")
        else:
            print("Grupos asignados al entrenador:")
            for grupo in grupos:
                print("Nombre del grupo:", grupo["nombre_grupo"])
                print("Horario:", grupo["Horario"])
                print("Salon:", grupo["Salon"])
                print("Ruta:", grupo["Ruta"])
                print("-----")
    info_grupos, trainers = cargar_datos()
###########################################################################################
    

    while True:
        print("¿Qué desea realizar?")
        print("1. Ver grupos según entrenador aignado")
        print("2. Ingresar notas de campers")
        print("3. Salir")

        opcion =str(input("--> "))

        if opcion == "1":
            clear()
            obtener_entrenadores(trainers)
            id_trainer = input("Ingrese el ID del entrenador: ")
            id_trainer = int(id_trainer)  # Convertir a entero
            grupos = obtener_grupos_por_trainer(id_trainer, info_grupos)
            imprimir_grupos(grupos)
        elif opcion=="2":
            print(ingresonotas.ingreso_notas())
        elif opcion == "3":
            break
        else:
            print("")
   
