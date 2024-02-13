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
        trainer_horario=int(input(" 1.(6:00)\n 2.(10:00)\n 3.(14:00) \n 4.(18:00)\n 5.(mixto) \n -> "))
        horario2=0
        clear()
        if trainer_horario==5:
            print("Escoge los horarios")
            print(" 1.(6:00)\n 2.(10:00)\n 3.(14:00) \n 4.(18:00)")
            trainer_horario=int(input("Horario 1: "))
            horario2=int(input("Horario 2: "))
        nuevo_dato = {
            "n_identificacion": trainer_n_ident,
            "Nombre": trainer_nombre,
            "Direccion": trainer_direccion,
            "Celular": trainer_celular,
            "Fijo": trainer_fijo,
            "Horario 1":trainer_horario,
            "horario 2":horario2
        }
        

        #Agregar trainer al json ( trianers.json)
        trainers["campers"]["trainers"].append(nuevo_dato) 

        with open('trainers.json', 'w') as file:
            json.dump(trainers, file, indent=2)  # Guardar cambios

        print(" ingreso trainer exitoso! ")

