import os
import json

def campers():
    def clear():
        if os.name == 'nt':
            os.system('cls')        # Funcion para limpiar la terminal
        else:
            os.system('clear')
    while True:
        with open('proceso_de_inscripcion.json', 'r') as proceso_file:
            proceso_de_inscripcion = json.load(proceso_file)  # Cargar contenido del archivo JSON a una variable
        clear()
        print(" - Proceso de ingreso - ")
        print("")
        print("Desea realizar el pree registro a campus? (Si / No)")
        volver = input("-> ")

        if volver.lower() == "no":
            return

        nuevo_dato = {
            "n_identificacion": int(input("Numero de identificacion: ")),
            "Nombre": str(input("Nombre completo: ")),
            "Direccion": str(input("Direccion: ")),
            "Acudiente": str(input("Nombre acudiente: ")),
            "Celular": str(input("Numero celular: ")),
            "Fijo": str(input("Numero fijo: ")), 
            "Estado": "proceso_de_inscripcion",
            "Riesgo": ""
        }

        proceso_de_inscripcion["campers"]["campers_pre_inscritos"].append(nuevo_dato)  # Agregar datos al archivo JSON

        with open('proceso_de_inscripcion.json', 'w') as file:
            json.dump(proceso_de_inscripcion, file, indent=2)  # Guardar cambios

        print("Pre ingreso exitoso! ")

