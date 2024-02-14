import json

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
                    nota = float(input(f"Ingrese la nota para el modulo '{modulo}': "))
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