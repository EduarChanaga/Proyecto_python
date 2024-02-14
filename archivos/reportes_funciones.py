import json
import os
def clear():
    if os.name == 'nt':
        os.system('cls')  # Funcion para limpiar la terminal
    else:
        os.system('clear')

def inscritos():
    clear()
    # Cargar el archivo JSON
    with open('inscritos.json', 'r') as file:
        inscritos = json.load(file)

    # Acceder a la lista de campers inscritos
    campers_inscritos = inscritos['campers']['campers_inscritos']

    # Imprimir nombre e identificación de cada camper inscrito
    for camper in campers_inscritos:
        print(f"Nombre: {camper['Nombre']}, ID: {camper['n_identificacion']}")
    print()
    cl=str(input("Enter para continuar"))
    clear()

def aprobados_ingreso():
    clear()
    # Cargar el archivo JSON
    with open('aprobaron_examen_ingreso.json', 'r') as file:
        data = json.load(file)

    campers = data["campers"]["aprobaron_examen_ingreso"]

    for camper in campers:
        print(f"Nombre: {camper['Nombre']}, ID: {camper['n_identificacion']}")
    print()
    cl=str(input("Enter para continuar"))
    clear()

def trainers():
    clear()
    # Cargar el archivo JSON
    with open('trainers.json', 'r') as file:
        trainers = json.load(file)

    trainerss = trainers["campers"]["trainers"]
    print("Trainers:")
    print("")
    for trainer in trainerss:
        print(f"Nombre: {trainer['Nombre']}, ID: {trainer['n_identificacion']}")
    print()
    cl=str(input("Enter para continuar"))
    clear()

def bajo_rendimiento():
    # Cargar los datos JSON
    with open('grupos.json', 'r') as archivo:
        datos = json.load(archivo)

    # Definir una función para verificar el riesgo alto
    def riesgo_alto(camper):
        # Verificar si el campo 'Riesgo' es igual a 'Alto'
        return camper.get("Riesgo") == "Alto"

    # Iterar sobre cada grupo y campero
    for grupo, campers in datos["grupos"].items():
        print(f"Grupo: {grupo}")
        for camper in campers:
            if riesgo_alto(camper):
                print(f"Nombre: {camper['Nombre']}, ID: {camper['n_identificacion']}")

    print()
    cl=str(input("Enter para continuar"))
    clear()

def rutas_campers_trainer():
    
# Cargar los datos de los archivos JSON
    with open('grupos.json', 'r') as file:
        grupos_data = json.load(file)

    with open('info_grupos.json', 'r') as file:
        info_grupos_data = json.load(file)

    # Obtener la ruta elegida por el usuario
    print("1. Ruta NodeJS")
    print("2. Ruta Java")
    print("3. Ruta NetCore")
    ruta_elegida = input("Ingrese la ruta a buscar: ")
    clear()
    # Buscar los grupos con la ruta elegida
    grupos_con_ruta = [grupo for grupo in info_grupos_data["campus"]["grupo"] if str(grupo["Ruta"]) == ruta_elegida]

    # Imprimir los campers de los grupos con la ruta elegida
    for grupo in grupos_con_ruta:
        grupo_id = grupo["nombre_grupo"]
        print("")
        print("---------------")
        print("Trainer:")
        print(f"- {grupo['trainer']['Nombre']}")
        print()
        print(f"Campers en el grupo {grupo_id}:")
        for camper in grupos_data["grupos"][grupo_id]:
            print(f"Nombre: {camper['Nombre']}, ID: {camper['n_identificacion']}")
    print("")    
    cl=str(input("Enter para continuar"))
    clear()

def perdieron_aprobaron_modulo():
    print()