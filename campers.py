import os
import json
def campers():
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
    Decision2=0
    clear()
    while Decision2!=3:
        print("Que desea realizar?")
        print("1. Inscripcion")
        print("2. Ver datos de campers")
        print("3. salir")
        Decision2=int(input("--> "))
        clear()

            
        if Decision2==1:
            # Obtener el próximo ID disponible
            identificacion_inscripcion=int(input("N° de identificacion: "))
            nombre1_inscrito=str(input("Primer nombre: "))
            nombre2_inscrito=str(input("Segundo nombre: "))
            apellido1_inscrito=str(input("Primero apellido: "))
            apellido2_inscrito=str(input("Segundo apellido: "))
            direccion_inscrito=str(input("Direccion: "))
            acudiente_inscrito=str(input("Nombre acudiente: "))
            celular_inscrito=str(input("Numero celular: "))
            fijo_inscrito=str(input("Numero fijo: "))
            clear()

            nuevo_dato = {
                "n_identificacion": identificacion_inscripcion,
                "Nombre": nombre1_inscrito+" "+nombre2_inscrito+" "+apellido1_inscrito+" "+apellido2_inscrito,
                "Direccion": direccion_inscrito,
                "Acudiente": acudiente_inscrito,
                "Celular": celular_inscrito,
                "FIjo": fijo_inscrito,
                "Estado": "Inscrito",
                "grupo":""
            }

            # Agregar el nuevo dato a la lista de inscritos
            inscrip["inscripcion"]["Inscritos"].append(nuevo_dato)

            # Escribir el JSON actualizado de vuelta al archivo
            with open('datos.json', 'w') as file:
                json.dump(inscrip, file, indent=2)
            
            print("Inscrito correctamente")