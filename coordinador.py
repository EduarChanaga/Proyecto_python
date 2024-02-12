import os
import json
def coordinador():
    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    with open('datos.json', 'r') as datos:
        # Cargar el contenido del archivo en un diccionario
        inscrip = json.load(datos)

    with open('grupos.json', 'r') as grups:
        # Cargar el contenido del archivo en un diccionario
        grupos = json.load(grups)
    with open('grupos.json', 'r') as gruposs:
        # Cargar el contenido del archivo en un diccionario
        grupos = json.load(gruposs)
    inscritos = inscrip["inscripcion"]["Inscritos"]
    aprobados = inscrip["inscripcion"]["aprobados"]
    reprobados=inscrip["inscripcion"]["reprobados"]
    decision2=0
    print("Porfavor digite la contraseña")
    contraseña=str(input("--> "))
    while decision2!=4:
        #campus2024
        clear()
        if contraseña=="campus2024":
        
            print("Que desea realizar?")
            print("1. Ingresar notas de estudiantes inscritos")
            print("2. Crear nuevo grupo")
            print("3. Asignar grupos a campers aprobados")
            print("4. salir")
            decision2=int(input("--> "))
            
            clear()
            
                        #definir si un estudiante inscrito aprueba o reprueba

            if decision2==1: 
                f="si"
                while f=="si":
                    inscritos_ordenados = sorted(inscritos, key=lambda x: x["n_identificacion"])
                    for inscrito in inscritos_ordenados:
                        print("  N° Identificación:", inscrito["n_identificacion"], "  Nombre:", inscrito["Nombre"] )
                    print("-----")
                    identificacion_nota_inscrito=int(input("N° de identificacion del estudiante a ingresar notas: "))
                    nota_teorica_inscrito=float(input("Nota teorica: "))
                    nota_practica_inscrito=float(input("Nota practica: "))
                    calificacion_inscrito=(nota_practica_inscrito+nota_teorica_inscrito)/2
                    for inscrito in inscritos:
                        if inscrito["n_identificacion"] == identificacion_nota_inscrito:
                            # Actualizar el estado del inscrito si la calificación es mayor o igual a 60
                            if calificacion_inscrito >= 60:
                                inscrito["Estado"] = "Aprobado"
                                    # Mover al estudiante de la lista de inscritos a la lista de aprobados
                                    # Generar una nueva ID única para el estudiante aprobado
                                    
                                aprobados.append(inscrito)
                                inscritos.remove(inscrito)
                            else:
                                inscrito["Estado"] = "Reprobado"
                                reprobados.append(inscrito)
                                inscritos.remove(inscrito)
                            
                            
                    
                            with open('datos.json', 'w') as file:
                                json.dump(inscrip, file, indent=2)
                            print("Desea ingresar notas de un estudiante? (si / no)")
                            f=str(input("--> "))
                            clear()
                            break
            elif decision2==2:
                # Pedir al usuario el nombre de la nueva grupo
                nuevo_grupo = input("Ingrese el nombre del nuevo grupo: ")

                # Verificar si el grupo ya existe
                if nuevo_grupo in grupos["grupos"]:
                    print("¡El grupo ya existe!")
                else:
                    # Agregar la nueva grupo al diccionario
                    grupos["grupos"][nuevo_grupo] = []

                    # Escribir el diccionario actualizado de vuelta al archivo JSON
                    with open('grupos.json', 'w') as grups_file:
                        json.dump(grupos, grups_file, indent=2)

                    print("¡Nuev grupo creada con éxito!")          
            elif decision2 == 3:
                # Obtener la lista de grupos disponibles
                grupos_disponibles = list(grupos["grupos"].keys())

                # Iterar sobre la lista de estudiantes aprobados
                for estudiante in inscrip["inscripcion"]["aprobados"]:
                    # Obtener el nombre del estudiante
                    nombre_estudiante = estudiante["Nombre"]

                    # Verificar si el estudiante está aprobado
                    if estudiante["Estado"] == "Aprobado":
                        # Pedir al usuario que seleccione un grupo para el estudiante
                        print(f"Estudiante aprobado: {nombre_estudiante}")
                        print("Grupos disponibles:")
                        for index, grupo in enumerate(grupos_disponibles, start=1):
                            print(f"{index}. {grupo}")

                        # Solicitar al usuario que seleccione un grupo
                        seleccion = int(input("Seleccione un grupo para el estudiante: ")) - 1

                        # Verificar si la selección del usuario es válida
                        if 0 <= seleccion < len(grupos_disponibles):
                            grupo_seleccionado = grupos_disponibles[seleccion]

                            # Verificar si el grupo no supera los 33 alumnos
                            if len(grupos["grupos"][grupo_seleccionado]) < 33:
                                # Agregar el estudiante al grupo seleccionado
                                grupos["grupos"][grupo_seleccionado].append(estudiante)
                                print(f"El estudiante {nombre_estudiante} ha sido agregado al grupo {grupo_seleccionado}")

                                # Actualizar la información del grupo en el estudiante
                                estudiante["grupo"] = grupo_seleccionado

                                # Eliminar al estudiante de la lista de inscritos
                                inscrip["inscripcion"]["aprobados"].remove(estudiante)

                                # Escribir el diccionario actualizado de vuelta al archivo JSON de grupos
                                with open('grupos.json', 'w') as gruposs:
                                    json.dump(grupos, gruposs, indent=2)

                                # Escribir el diccionario actualizado de vuelta al archivo JSON de estudiantes aprobados
                                with open('datos.json', 'w') as file:
                                    json.dump(inscrip, file, indent=2)
                                print("")
                                print("")
                                clear()
                            else:
                                clear()
                                print()
                                print("El grupo seleccionado ya tiene 33 alumnos. Por favor, seleccione otro grupo.")
                        else:
                            print("Selección inválida. No se ha agregado el estudiante a ningún grupo.")
