import json
import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def ingreso_notas():
    with open("grupos.json", "r") as file:
        grupos = json.load(file)

    print("Grupos disponibles:")
    for grupo in grupos["grupos"]:
        print(grupo)

    grupo_seleccionado = input("Ingrese el nombre del grupo que desea seleccionar: ")

    if grupo_seleccionado in grupos["grupos"]:
        alumnos = grupos["grupos"][grupo_seleccionado]
        print("\nAlumnos en el grupo:")
        for alumno in alumnos:
            print(f"ID: {alumno['n_identificacion']} - Nombre: {alumno['Nombre']}")

        id_alumno = int(input("\nIngrese el ID del alumno para ingresar la nota: "))
        for alumno in alumnos:
            if alumno['n_identificacion'] == id_alumno:
                print("\nModulos del alumno:")
                for i, modulo in enumerate(alumno["modulos"], 1):
                    print(f"{i}. {modulo}")

                modulo_seleccionado = int(input("\nIngrese el número del modulo al que desea ingresar la nota: "))
                if 1 <= modulo_seleccionado <= len(alumno["modulos"]):
                    modulo = list(alumno["modulos"].keys())[modulo_seleccionado - 1]
                    clear()
                    print(f"--> {modulo} <--")
                    teorica = float(input(f"Ingrese la nota de la prueba teorica: "))
                    practica = float(input(f"Ingrese la nota de la prueba practica': "))
                    quizes = float(input(f"Ingrese la nota de quizes y tareas: "))
                    nota=(teorica*0.3)+(practica*0.6)+(quizes*0.1)
                    if nota <60:
                        alumno["Riesgo"] = "Riesgo alto"
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