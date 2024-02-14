import os
import json

#crear grupo
######################################################################################################################################
def crear_grupo(): 
    print("")
    def clear():
        if os.name == 'nt':
            os.system('cls')        # Funcion para limpiar la terminal
        else:
            os.system('clear')
    while True:
        with open('info_grupos.json', 'r') as i:
            info_grupos = json.load(i) 
        with open('grupos.json', 'r') as o:
            grupos = json.load(o)
        with open('trainers.json', 'r') as u:
            trainers = json.load(u) # Cargar contenido del archivo JSON a una variable
        
        
        print(" - Proceso de creacion de grupos - ")
        print("")
        print("Desea crear nuevo grupo? (Si / No)")
        volver = input("-> ")

        if volver.lower() == "no":
            return
        
        clear()
        # Ingreso de datos del entrenador
        grupo_nombre = input("Nombre del grupo: ")
        clear()
        print("- Horario del grupo -")
        grupo_horario = int(input("1. (6:00)\n2. (10:00)\n3. (14:00)\n4. (18:00)\n-> "))
        clear()
        # Mostrar la lista de entrenadores con su ID y nombre
        for trainer in trainers["campers"]["trainers"]:
            print("ID:", trainer["n_identificacion"])
            print("Nombre:", trainer["Nombre"])
            print("")
            print("")

######################################################################################################################################
        #Agregar entrenador a nuevo grupo
        while True:
            print("Ingresa la ID del entrenador que deseas seleccionar")
            print("0 = cancelar")
            grupo = int(input("--> "))
            if grupo!=0:
                
                # Buscar el entrenador por su ID
                grupo_trainer = None
                for trainer in trainers["campers"]["trainers"]:
                    if int(trainer["n_identificacion"]) == grupo:
                        grupo_trainer = {
                            "ID": grupo,
                            "Nombre": trainer["Nombre"]
                        }
                        break

                if grupo_trainer:
                    print("Entrenador seleccionado:", grupo_trainer["Nombre"])
                    break
                else:
                    print("La ID del entrenador ingresada no existe. Intenta de nuevo.")
                    print("")
                    print("")
            if grupo ==0:
                clear()
                return
        # Verificar si el entrenador ya está asignado a otro grupo en el mismo horario
        entrenador_existente = False
        for grupo in info_grupos["campus"]["grupo"]:
            if grupo["Horario"] == grupo_horario and grupo.get("trainer") and grupo["trainer"]["ID"] == grupo_trainer["ID"]:
                entrenador_existente = True
                break

        if entrenador_existente:
            print("El entrenador ya está asignado a otro grupo en el mismo horario. Selecciona otro horario o entrenador.")
            continue








######################################################################################################################################
        #definir aula del salon
        print("1. Sputnik")
        print("2. Apolo")
        print("3. Artemis")
        grupo_salon=int(input("Ingrese N° de salon: "))
        #verificar si el grupo ya existe con el mismo horario
        grupo_existente=False
        for grupo in info_grupos["campus"]["grupo"]:
            if grupo["Horario"]==grupo_horario and grupo.get("Salon")==grupo_salon:
                grupo_existente=True
                break
        if grupo_existente:
            print("El grupo ya existe con el mismo salon y horario. Selecciona otro salon u otro horario")
            print("")
            continue
######################################################################################################################################
        
        
        #definir ruta del salon
        print("1. Ruta NodeJS")
        print("2. Ruta Java")
        print("3. Ruta NetCore")
        grupo_ruta=int(input("Ingrese N° de ruta: "))
        
        
        
        #Guardar datos en un diccionario
        nuevo_dato = {
            "nombre_grupo": grupo_nombre,
            "Horario": grupo_horario,
            "trainer": grupo_trainer,
            "Salon":grupo_salon,
            "Ruta":grupo_ruta
        }
        
        # Agregar el grupo al archivo JSON

    
 
        #Agregar trainer al json ( trianers.json)
        info_grupos["campus"]["grupo"].append(nuevo_dato) 
        print("Ingreso del grupo exitoso!")
        nuevo_grupo = grupo_nombre
        grupos["grupos"][nuevo_grupo] = []
        with open('grupos.json', 'w') as file:
            json.dump(grupos, file, indent=2) 

        with open('info_grupos.json', 'w') as file:
            json.dump(info_grupos, file, indent=2)  # Guardar cambios

        print("Creacion de grupo exitosa! ")

#ver grupo
def ver_grupos():
    def clear():
        if os.name == 'nt':
            os.system('cls')        # Funcion para limpiar la terminal
        else:
            os.system('clear')
    with open('grupos.json', 'r') as o:
        grupos = json.load(o)
    clear()
    grupos = grupos["grupos"]
    for grupo in grupos:
        print(grupo)
    print("")
    print("")
    