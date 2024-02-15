import os
import json

def clear():
    if os.name == 'nt':
        os.system('cls')  # Funcion para limpiar la terminal
    else:
        os.system('clear')


############### Pasar un camper de pre inscrito a inscrito ######################
def inscripcion():
    clear()
    
    # Leer el archivo JSON
    with open('proceso_de_inscripcion.json', 'r') as file:
        datos = json.load(file)
    with open("inscritos.json", "r") as file:
        inscritos = json.load(file)
    

    # Buscar al pre_inscrito por su número de identificación
    pre_inscritos = datos['campers']['campers_pre_inscritos']
    inscritos = inscritos['campers']['campers_inscritos']

    for pre_inscrito in pre_inscritos:
        print("Numero de identificacion:", pre_inscrito["n_identificacion"], "   Nombre: ",pre_inscrito["Nombre"])
    print("")
    while True:
        try:
            numero_identidad = int(input("Ingrese la identificacion del camper que desea declarar como inscrito: "))
            break  # Si la conversión a entero tiene éxito, salimos del bucle
        except ValueError:
            print("Por favor, ingrese un número de identificación válido (entero).")

    for pre_inscrito in pre_inscritos:
        if pre_inscrito['n_identificacion'] == (numero_identidad):  # Convertir a int
            # Cambiar el estado de proceso de inscripción a inscritos
            pre_inscrito['Estado'] = 'inscritos'
            # Mover el pre_inscrito al nuevo arreglo campers_inscritos
            inscritos.append(pre_inscrito)
            # Remover el pre_inscrito del arreglo campers_pre_inscritos
            pre_inscritos.remove(pre_inscrito)

    # Escribir los cambios de vuelta al archivo JSON
    with open('proceso_de_inscripcion.json', 'w') as file:
        json.dump(datos, file, indent=2)
    with open('inscritos.json', 'w') as file:
        json.dump({"campers": {"campers_inscritos": inscritos}}, file, indent=2)
#########################################################################################################################################################################
#expulzar a un camper (asignar grupo)
def matriculas():
    with open("aprobados.json", "r") as file:
        aprobados = json.load(file)
    with open("grupos.json", "r") as file:
        grupos = json.load(file)
    with open("info_grupos.json","r") as file:
        info_grupos=json.load(file)

    aprobados = aprobados["campers"]["campers_aprobados"]
    grupos = grupos["grupos"]
    for i in aprobados:
        print("ID:", i["n_identificacion"])
        print("Nombre:", i["Nombre"])
        print("\n")

    print("Grupos:")
    for grupo in grupos:
        print(grupo)

    while True:
        try:
            camper_a_mover_a_grupo = int(input("Ingrese el ID del camper que desea asignar a un grupo: "))
            break  # Si la conversión a entero tiene éxito, salimos del bucle
        except ValueError:
            print("Por favor, ingrese un ID de camper válido (entero).")

    
    for i in range(len(aprobados)):
        if aprobados[i]['n_identificacion'] == camper_a_mover_a_grupo:
            camper = aprobados.pop(i)
            camper['Estado'] = 'Cursando'
            camper["modulos"]={"Fundamentos de programacion":0,
                       "programacion web":0,
                       "programacion formal":0,
                       "bases de datos":0,
                       "backend":0    
                    }

            grupo = input("Ingrese el nombre del grupo al que desea asignar al camper: ")

        if grupo in grupos:
            if len(grupos[grupo]) >= 33:
                print("No hay disponibilidad para este grupo.")
                break
            grupos[grupo].append(camper)

            # Agregar el entrenador al camper
            for g in info_grupos["campus"]["grupo"]:
                if g["nombre_grupo"] == grupo:
                    camper["trainer"] = g["trainer"]
                    break

            break
        else:
            print("El grupo ingresado no existe.")
            break


    with open('aprobados.json', 'w') as file:
        json.dump({"campers": {"campers_aprobados": aprobados}}, file, indent=2)

    with open('grupos.json', 'w') as file:
        json.dump({"grupos": grupos}, file, indent=2)

#########################################################################################################################################################################
def ingreso_de_notas():
    with open("inscritos.json", "r") as file:
        inscritos = json.load(file)
    with open("aprobados.json","r") as file:
        aprobados=json.load(file)
    with open("reprobados.json","r") as file:
        reprobados=json.load(file)
    with open("aprobaron_examen_ingreso.json","r") as i:
        aprobaron_examen_ingreso=json.load(i)
    for camper in inscritos['campers']['campers_inscritos']:  # Iterar sobre la lista de campers inscritos
        print("Numero de identificacion:", camper["n_identificacion"], "   Nombre: ",camper["Nombre"])
    while True:
        try:
            identificacion = int(input("Ingrese la identificacion del camper: "))
            break  # Si la conversión a entero tiene éxito, salimos del bucle
        except ValueError:
            print("Por favor, ingrese una identificación válida (entero).")

    for camper in inscritos['campers']['campers_inscritos']:  # Iterar sobre la lista de campers inscritos
        if camper["n_identificacion"] == identificacion:  # Acceder al diccionario de cada camper
            while True:
                try:
                    nota_teorica = float(input("Ingrese la nota teorica del camper: "))
                    nota_practica = float(input("Ingrese la nota practica del camper: "))
                    break  # Si la conversión a flotante tiene éxito, salimos del bucle
                except ValueError:
                    print("Por favor, ingrese una nota válida (número).")
            promedio = (nota_teorica + nota_practica) / 2
            if promedio >=60:
                camper["Estado"]="aprobado"
                aprobaron_examen_ingreso["campers"]["aprobaron_examen_ingreso"].append(camper)
                aprobados["campers"]["campers_aprobados"].append(camper)
                inscritos['campers']['campers_inscritos'].remove(camper)
            else:
                camper["Estado"]="reprobado"
                reprobados["campers"]["campers_reprobados"].append(camper)
                inscritos['campers']['campers_inscritos'].remove(camper)
            break
    else:
        print("Camper no encontrado")

    with open("inscritos.json", "w") as file:
        json.dump(inscritos, file, indent=4)

    with open("aprobados.json", "w") as file:
        json.dump(aprobados, file, indent=4)
    with open("reprobados.json", "w") as file:
        json.dump(reprobados, file, indent=4)
    with open("aprobaron_examen_ingreso.json", "w") as file:
        json.dump(aprobaron_examen_ingreso, file, indent=4)

def expulsar_camper():
    # Cargar datos de grupos y expulsados desde los archivos JSON
    with open('grupos.json', 'r') as file:
        grupos = json.load(file)

    with open('expulsados.json', 'r') as file:
        expulsados = json.load(file)
    while True:
        # Preguntar si se quiere expulsar un camper
        expulsar = str(input("¿Desea expulsar un camper? (si/no): "))
        clear()
        if expulsar.lower() == 'si':
            # Mostrar grupos disponibles
            print("Grupos disponibles:")
            for grupo in grupos['grupos']:
                print(grupo)

            # Elegir un grupo
            grupo_elegido = str(input("Elija un grupo: "))
            clear()
            # Mostrar campers en el grupo elegido
            print("Campers en el grupo:")
            for camper in grupos['grupos'][grupo_elegido]:
                print(f"Nombre: {camper['Nombre']}, ID: {camper['n_identificacion']}")

            # Elegir un camper para expulsar
            while True:
                try:
                    id_camper_expulsar = int(input("Elija el ID del camper para expulsar: "))
                    break  # Si la conversión a entero tiene éxito, salimos del bucle
                except ValueError:
                    print("Por favor, ingrese un ID de camper válido (entero).")

            # Buscar el camper en el grupo
            for camper in grupos['grupos'][grupo_elegido]:
                if camper['n_identificacion'] == id_camper_expulsar:
                    # Cambiar el estado del camper a "expulsado"
                    camper['Estado'] = 'Expulsado'
                    # Mover el camper al archivo de expulsados
                    expulsados["campers"]['campers_expulsados'].append(camper)
                    grupos['grupos'][grupo_elegido].remove(camper)
                    clear()
                    print(f"El camper {camper['Nombre']} ha sido expulsado.")
                    input("Presione Enter para continuar...")
                    break
            else:
                clear()
                print("Camper no encontrado.")
                input("Presione Enter para continuar...")
        if expulsar.lower() == 'no':
            break
        clear()
        # Guardar los cambios en los archivos JSON
        with open('grupos.json', 'w') as file:
            json.dump(grupos, file, indent=4)

        with open('expulsados.json', 'w') as file:
            json.dump(expulsados, file, indent=4)

def modificar_notas():
    with open("grupos.json", "r") as file:
        grupos = json.load(file)

    print("Grupos disponibles:")
    for grupo in grupos["grupos"]:
        print(grupo)

    grupo_seleccionado = str(input("Ingrese el nombre del grupo que desea seleccionar: "))

    if grupo_seleccionado in grupos["grupos"]:
        alumnos = grupos["grupos"][grupo_seleccionado]
        print("\nAlumnos en el grupo:")
        for alumno in alumnos:
            print(f"ID: {alumno['n_identificacion']} - Nombre: {alumno['Nombre']}")

        while True:
            try:
                id_alumno = int(input("\nIngrese el ID del alumno para modificar la nota: "))
                break  # Si la conversión a entero tiene éxito, salimos del bucle
            except ValueError:
                print("Por favor, ingrese un ID de alumno válido (entero).")
        for alumno in alumnos:
            if alumno['n_identificacion'] == id_alumno:
                print("\nModulos del alumno:")
                for i, modulo in enumerate(alumno["modulos"], 1):
                    print(f"{i}. {modulo}")

                while True:
                    try:
                        modulo_seleccionado = int(input("\nIngrese el número del módulo al que desea ingresar la nota: "))
                        break  # Si la conversión a entero tiene éxito, salimos del bucle
                    except ValueError:
                        print("Por favor, ingrese un número de módulo válido (entero).")
                if 1 <= modulo_seleccionado <= len(alumno["modulos"]):
                    modulo = list(alumno["modulos"].keys())[modulo_seleccionado - 1]
                    clear()
                    print(f"--> {modulo} <--")
                    while True:
                        try:
                            teorica = float(input("Ingrese la nota de la prueba teórica: "))
                            practica = float(input("Ingrese la nota de la prueba práctica: "))
                            quizes = float(input("Ingrese la nota de quices y tareas: "))
                            break  # Si la conversión a flotante tiene éxito para todas las entradas, salimos del bucle
                        except ValueError:
                            print("Por favor, ingrese un valor numérico válido para las notas.")

                    nota=(teorica*0.3)+(practica*0.6)+(quizes*0.1)
                    if nota <60:
                        alumno["Riesgo"] = "alto"
                    elif nota >=60 and nota<=85:
                        print("")
                        alumno["Riesgo"] = "Bajo"
                        print(f"El camper aprobo el modulo {modulo}")
                        print("")
                    elif nota >85:
                        print("")
                        alumno["Riesgo"] = "Nulo"
                        print(f"El camper aprobo el modulo {modulo}")
                        print("")
                    alumno["modulos"][modulo] = nota
                    print("Nota ingresada correctamente.")
                else:
                    print("El número de módulo ingresado no es válido.")
                break
        else:
            print("Alumno no encontrado en el grupo.")
    else:
        print("El grupo ingresado no existe.")

    with open("grupos.json", "w") as file:
        json.dump(grupos, file, indent=4)