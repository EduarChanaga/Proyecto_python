# ********************************************
# ********************************************
# Proyecto campuslands "python" 9 de febrero *
# ********************************************
# ********************************************

import json

# Abrir el archivo JSON
with open('datos.json', 'r') as Lospedidos:
    # Cargar el contenido del archivo en un diccionario
    diccionario = json.load(Lospedidos)
while True:
    inscritos = diccionario["Campus"]["Inscritos"]
    aprobados = diccionario["Campus"]["aprobados"]
    print("###############")
    print("# Campuslands #")
    print("# Bienvenido! #")
    print("###############")
    print("--------------------")
    print("Que tipo de usuario desea ingresar?")
    print("1. Camper")
    print("2. Trainer")
    print("3. Cordinador")
    Decision1=int(input("--> "))
    print("--------------------")


    ######################### Campers #########################
    if Decision1==1:

        print("Que desea realizar?")
        print("1. Inscripcion")
        print("2. Ver datos")
        Decision2=int(input("--> "))
        print("--------------------")

        
        if Decision2==1:
            # Obtener el próximo ID disponible
            next_id = len(diccionario["Campus"]["Inscritos"]) + 1
            identificacion_inscripcion=int(input("N° de identificacion: "))
            nombre1_inscrito=str(input("Primer nombre: "))
            nombre2_inscrito=str(input("Segundo nombre: "))
            apellido1_inscrito=str(input("Primero apellido: "))
            apellido2_inscrito=str(input("Segundo apellido: "))
            direccion_inscrito=str(input("Direccion: "))
            acudiente_inscrito=str(input("Nombre acudiente: "))
            celular_inscrito=str(input("Numero celular: "))
            fijo_inscrito=str(input("Numero fijo: "))
            # Nuevo dato a agregar con el próximo ID disponible
            nuevo_dato = {
                "Id": next_id,
                "n_identificacion": identificacion_inscripcion,
                "Nombre": nombre1_inscrito+" "+nombre2_inscrito+" "+apellido1_inscrito+" "+apellido2_inscrito,
                "Direccion": direccion_inscrito,
                "Acudiente": acudiente_inscrito,
                "Celular": celular_inscrito,
                "FIjo": fijo_inscrito,
                "Estado": "Inscrito"
            }

            # Agregar el nuevo dato a la lista de inscritos
            diccionario["Campus"]["Inscritos"].append(nuevo_dato)

            # Escribir el JSON actualizado de vuelta al archivo
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)

    ######################### Trainers #########################
    if Decision1==2:
        print("")

    ######################### Coordinador #########################
    if Decision1==3:
        print("Porfavor digite la contraseña")
        contraseña=str(input("--> "))  #campus2024
        if contraseña=="campus2024":
            print("-----")
            print("Que desea realizar?")
            print("1. Ingresar notas de estudiantes inscritos")
            decision2=int(input("--> "))
            print("-----")
            if decision2==1:
                inscritos_ordenados = sorted(inscritos, key=lambda x: x["Id"])
                for inscrito in inscritos_ordenados:
                    print("ID:", inscrito["Id"], "  N° Identificación:", inscrito["n_identificacion"], "  Nombre:", inscrito["Nombre"] )
                print("-----")
                id_nota_inscrito=int(input("ID del estudiante a ingresar notas: "))
                nota_teorica_inscrito=float(input("Nota teorica: "))
                nota_practica_inscrito=float(input("Nota practica: "))
                calificacion_inscrito=(nota_practica_inscrito+nota_teorica_inscrito)/2
                for inscrito in inscritos:
                    if inscrito["Id"] == id_nota_inscrito:
                        # Actualizar el estado del inscrito si la calificación es mayor o igual a 60
                        if calificacion_inscrito >= 60:
                            inscrito["Estado"] = "Aprobado"
                            # Mover al estudiante de la lista de inscritos a la lista de aprobados
                            aprobados.append(inscrito)
                            inscritos.remove(inscrito)
                        else:
                            inscrito["Estado"] = "Reprobado"
                        break

                # Escribir el JSON actualizado de vuelta al archivo
                with open('datos.json', 'w') as file:
                    json.dump(diccionario, file, indent=2)
        else:
            print("contraseña incorrecta")
## Desarrollado por Eduar Damian Chanaga Gonzalez - 1095581647