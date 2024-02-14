import os
import json

def ingreso_trainer():
    def clear():
        if os.name == 'nt':
            os.system('cls')        # Funcion para limpiar la terminal
        else:
            os.system('clear')
    while True:
        with open('trainers.json', 'r') as proceso_file:
            trainers = json.load(proceso_file)  # Cargar contenido del archivo JSON a una variable
        clear()
        print(" - Proceso de ingreso de trainers - ")
        print("")
        print("Desea realizar el registro de un trainer a campus? (Si / No)")
        volver = input("-> ")

        if volver.lower() == "no":
            return
        
        clear()
        #Ingreso de datos del tainer
        trainer_n_ident=int(input("Numero de identificacion: "))
        trainer_nombre=str(input("Nombre completo: "))
        trainer_direccion=str(input("Direccion: "))
        trainer_celular=str(input("Numero celular: "))
        trainer_fijo=str(input("Numero fijo: "))
        nuevo_dato = {
            "n_identificacion": trainer_n_ident,
            "Nombre": trainer_nombre,
            "Direccion": trainer_direccion,
            "Celular": trainer_celular,
            "Fijo": trainer_fijo
        }
        

        #Agregar trainer al json ( trianers.json)
        trainers["campers"]["trainers"].append(nuevo_dato) 

        with open('trainers.json', 'w') as file:
            json.dump(trainers, file, indent=2)  # Guardar cambios
            
        print(" ingreso trainer exitoso! ")

