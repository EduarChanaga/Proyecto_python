import reportes_funciones
import os
def clear():
    if os.name == 'nt':
        os.system('cls')  # Funcion para limpiar la terminal
    else:
        os.system('clear')

def reportes():
    while True:
        print("\033[1;30m" + "-" * 21)
        print("\033[1;30m" + "|      \033[1;37mReportes     \033[1;30m|")
        print("\033[1;30m" + "-" * 21)
        print("1. Listar los campers que se encuentren en estado de inscrito.")
        print("2. Listar los campers que aprobaron el examen inicial.")
        print("3. Listar los entrenadores que se encuentran trabajando con CampusLands.")
        print("4. Listar los campers que cuentan con bajo rendimiento.")
        print("5. Listar los campers y trainers que se encuentren asociados a una ruta de entrenamiento.")
        print("6. Mostrar cuantos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.")
        print("7. Salir")
        reportes=int(input("--> "))
        clear()
        if reportes==1:
            print(reportes_funciones.inscritos())
        elif reportes==2:
            print(reportes_funciones.aprobados_ingreso())
        elif reportes==3:
            print(reportes_funciones.trainers())
        elif reportes==4:
            print(reportes_funciones.bajo_rendimiento())
        elif reportes==5:
            print(reportes_funciones.rutas_campers_trainer())
        elif reportes==6:
            print(reportes_funciones.perdieron_aprobaron_modulo())
        elif reportes==7:
            print()
            break
