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
        print("\033[1;30m" + "-" * 17)
        print("\033[1;30m" + "|      \033[1;37mCamper   \033[1;30m|")
        print("\033[1;30m" + "-" * 17)
  
        print("")
        print("Desea realizar el pre registro a campus? (Si / No)")
        volver = input("-> ")
        clear()
        if volver.lower() == "no":
            break
        if volver.lower()=="si":
            while True:
                try:
                    n_identificacion = int(input("Numero de identificacion: "))
                    break  # Si la conversión a entero tiene éxito, salimos del bucle
                except ValueError:
                    print("Por favor, ingrese un número de identificación válido (entero).")

            nuevo_dato = {
                "n_identificacion": n_identificacion,
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

