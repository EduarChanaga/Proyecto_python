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
    import json

    # Cargar datos desde los archivos JSON
    with open('info_grupos.json', 'r') as file:
        info_grupos = json.load(file)

    with open('grupos.json', 'r') as file:
        grupos = json.load(file)

    # Función para calcular el estado de los módulos
    def calcular_estado(modulos):
        for modulo, nota in modulos.items():
            if nota == "":
                modulos[modulo] = "Perdido"
            elif float(nota) >= 60.0:
                modulos[modulo] = "Aprobado"
            else:
                modulos[modulo] = "Perdido"

    # Diccionario para contar los campers que perdieron y aprobaron cada módulo
    contadores_modulos = {}

    # Iterar sobre cada grupo
    for grupo_info in info_grupos['campus']['grupo']:
        grupo_nombre = grupo_info['nombre_grupo']
        trainer_nombre = grupo_info['trainer']['Nombre']

        # Obtener los campers del grupo
        campers = grupos['grupos'][grupo_nombre]

        # Iterar sobre cada camper del grupo
        for camper in campers:
            calcular_estado(camper['modulos'])  # Calcular el estado de los módulos
            for modulo, estado in camper['modulos'].items():
                # Incrementar el contador para el módulo correspondiente
                contador_key = (grupo_nombre, trainer_nombre, modulo, estado)
                contadores_modulos[contador_key] = contadores_modulos.get(contador_key, 0) + 1
    
     # Agrupar los resultados por grupo y por entrenador
    resultados_por_grupo_trainer = {}
    for (grupo, entrenador, modulo, estado), cantidad in contadores_modulos.items():
        if grupo not in resultados_por_grupo_trainer:
            resultados_por_grupo_trainer[grupo] = {}
        if entrenador not in resultados_por_grupo_trainer[grupo]:
            resultados_por_grupo_trainer[grupo][entrenador] = []
        resultados_por_grupo_trainer[grupo][entrenador].append((grupo, entrenador, modulo, estado, cantidad))

    # Mostrar los resultados por grupo y por entrenador
    for grupo, entrenadores in resultados_por_grupo_trainer.items():
        print(f"Grupo: {grupo}")
        for entrenador, resultados in entrenadores.items():
            print(f"Entrenador: {entrenador}")
            for (grupo, entrenador, modulo, estado, cantidad) in resultados:
                print(f"Módulo: {modulo}, Estado: {estado}, Cantidad: {cantidad}")
            print()
    print("")    
    cl=str(input("Enter para continuar"))
    clear()