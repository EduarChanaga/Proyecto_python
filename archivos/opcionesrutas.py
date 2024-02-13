import os
import json

def crear_grupo():
    print("")
    def clear():
        if os.name == 'nt':
            os.system('cls')        # Funcion para limpiar la terminal
        else:
            os.system('clear')
    while True:
        with open('info_grupos.json', 'r') as proceso_file:
            info_grupos = json.load(proceso_file) 
        with open('grupos.json', 'r') as proceso_file:
            grupos = json.load(proceso_file)
        with open('trainers.json', 'r') as proceso_file:
            trainers = json.load(proceso_file) # Cargar contenido del archivo JSON a una variable
        clear()
        print(" - Proceso de creacion de grupos - ")
        print("")
        print("Desea crear nuevo grupo? (Si / No)")
        volver = input("-> ")

        if volver.lower() == "no":
            return
        
        clear()
        # Ingreso de datos del entrenador
        grupo_nombre = input("Nombre del grupo: ")
        grupo_horario = int(input("1. (6:00)\n2. (10:00)\n3. (14:00)\n4. (18:00)\n-> "))
        
        # Mostrar la lista de entrenadores con su ID y nombre
        for trainer in trainers["campers"]["trainers"]:
            print("ID:", trainer["n_identificacion"])
            print("Nombre:", trainer["Nombre"])
          
        while True:
            selected_id = input("Ingresa la ID del entrenador que deseas seleccionar: ")

            # Buscar el entrenador por su ID
            selected_trainer = None
            for trainer in trainers["campers"]["trainers"]:
                if str(trainer["n_identificacion"]) == selected_id:
                    selected_trainer = {
                        "ID": selected_id,
                        "Nombre": trainer["Nombre"]
                    }
                    break

            if selected_trainer:
                print("Entrenador seleccionado:", selected_trainer["Nombre"])
                break
            else:
                print("La ID del entrenador ingresada no existe. Intenta de nuevo.")
        
        nuevo_dato = {
            "nombre_grupo": grupo_nombre,
            "Horario 1": grupo_horario,
            "trainer": selected_trainer,
            "ruta": ""
        }
        
        # Agregar el grupo al archivo JSON
        # ...

        print("Ingreso del grupo exitoso!")

        #Agregar trainer al json ( trianers.json)
        info_grupos["campus"]["grupo"].append(nuevo_dato) 

        with open('info_grupos.json', 'w') as file:
            json.dump(info_grupos, file, indent=2)  # Guardar cambios

        print(" ingreso trainer exitoso! ")
