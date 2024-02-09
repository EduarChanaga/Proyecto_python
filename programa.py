# ********************************************
# ********************************************
# ** Desde mi ordenador no funciona con ( ' )*
# ********************************************
# ********************************************

import json

# Abrir el archivo JSON
with open('datos.json', 'r') as Lospedidos:
    # Cargar el contenido del archivo en un diccionario
    diccionario = json.load(Lospedidos)


####################################### Funciones de eliminado y agregado de datos #############################################
def eliminar_cliente_por_id(id_cliente):
    # Eliminar el cliente de la lista de clientes
    diccionario['ventas']['clientes'] = [cliente for cliente in diccionario['ventas']['clientes'] if cliente['id'] != id_cliente]
    # Eliminar todos los pedidos relacionados con este cliente
    diccionario['ventas']['pedidos'] = [pedido for pedido in diccionario['ventas']['pedidos'] if pedido['id_cliente'] != id_cliente]

def agregar_nuevo_cliente(nuevo_cliente):
    # Obtener la lista de clientes y agregar el nuevo cliente
    diccionario['ventas']['clientes'].append(nuevo_cliente)

def eliminar_pedido_por_id(id_pedido):
    # Filtrar los pedidos que no tengan el ID proporcionado
    diccionario['ventas']['pedidos'] = [pedido for pedido in diccionario['ventas']['pedidos'] if pedido['id'] != id_pedido]

def agregar_pedido_para_cliente_existente(id_cliente, nuevo_pedido):
    # Buscar al cliente por su ID
    cliente_existente = next((cliente for cliente in diccionario['ventas']['clientes'] if cliente['id'] == id_cliente), None)
    if cliente_existente:
        # Verificar si la ID del comercial en el nuevo pedido es válida
        id_comercial_nuevo_pedido = nuevo_pedido.get('id_comercial', None)
        if id_comercial_nuevo_pedido is not None:
            comercial_existente = next((comercial for comercial in diccionario['ventas']['comerciales'] if comercial['id'] == id_comercial_nuevo_pedido), None)
            if comercial_existente:
                # Agregar el nuevo pedido al final de la lista de pedidos
                nuevo_pedido['id_cliente'] = id_cliente
                diccionario['ventas']['pedidos'].append(nuevo_pedido)
            else:
                print(f"No se encontró ningún comercial con el ID {id_comercial_nuevo_pedido}")
        else:
            print("La ID del comercial en el nuevo pedido no está especificada.")
    else:
        print(f"No se encontró ningún cliente con el ID {id_cliente}")

# Función para agregar un nuevo comercial
def agregar_nuevo_comercial(nuevo_comercial):
    # Obtener la lista de comerciales y agregar el nuevo comercial
    diccionario['ventas']['comerciales'].append(nuevo_comercial)

def eliminar_comercial_por_id(id_comercial):
    # Filtrar los comerciales que no tengan el ID proporcionado
    diccionario['ventas']['comerciales'] = [comercial for comercial in diccionario['ventas']['comerciales'] if comercial['id'] != id_comercial]

pedidos = diccionario["ventas"]["pedidos"]
comerciales = diccionario["ventas"]["comerciales"]
clientes = diccionario["ventas"]["clientes"]

while True:
    print("")
    print("\033[1;90mQue desea realizar?")
    print("1. Mostrar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Agregar")
    decision3=int(input("--> "))
    if decision3 == 1:
        print("")
    elif decision3==2:






######################### MODIFICAR clientes #########################
        print("\033[93m1. Modificar datos de cliente ( Nombre/ Apellido/ Apellido2/ ciudad )")
        print("2. Modificar pedidos ( Total / fecha )")
        print("3. Modificar datos de comerciales ( nombre / apellido1 / apellido2 / comision )")
        print("4. Salir")
        decision4=int(input("--> "))
        if decision4==1:
            for i in clientes:
                            print(i)
            print("")
            id_cliente_mod=int(input("Id del usuario a modificar: "))
            nombre_cliente_mod=str(input("Nombre: "))
            apellido_cliente_mod=str(input("Apellido: "))
            apellido2_cliente_mod=str(input("Apellido 2: "))
            ciudad_cliente_mod=str(input("Ciudad: "))
    # Iterar sobre la lista de clientes y modificar los nombres
            for cliente in diccionario['ventas']['clientes']:
                if cliente['id'] == id_cliente_mod:  # Modificar el nombre del cliente con ID 4
                    cliente['nombre'] = nombre_cliente_mod
                    cliente['apellido1'] = apellido_cliente_mod
                    cliente['apellido2'] = apellido2_cliente_mod
                    cliente["ciudad"]=ciudad_cliente_mod
            # Guardar los cambios en el mismo JSON (sobreescribir)
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)



######################### MODIFICAR pedidos #########################
        if decision4==2:
            for i in pedidos:
                            print(i)
            print("")
            id_cliente_mod=int(input("Id del pedido a modificar: "))
            
            total_pedido_mod=float(input("Total: "))
            print("fecha = año-mes-dia Ej: (2018-10-06)")
            fecha_pedido_mod=str(input("Fecha: "))

            
    # Iterar sobre la lista de clientes y modificar los nombres
            for pedido in diccionario['ventas']['pedidos']:
                if pedido['id'] == id_cliente_mod:  # Modificar el nombre del cliente con ID 4
                    pedido['total'] = total_pedido_mod
                    pedido["fecha"]=fecha_pedido_mod
  
            # Guardar los cambios en el mismo JSON (sobreescribir)
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)




######################### MODIFICAR comerciales #########################
        if decision4==3:
            for i in comerciales:
                            print(i)
            print("")
            id_comercial_mod=int(input("Id del comercial: "))
            
            nombre_comercial_mod=str(input("Nombre del comercial: "))
            apellido1_comercial_mod=str(input("Apellido del comercial: "))
            apellido2_comercial_mod=str(input("Apellido2 del comercial: "))

            while True:
                try: #Comprobar que el numero este entre el rango 1-1000 y que no tenga decimales.
                    comision_comercial_mod=float(input("Comision < 1: "))
                    if comision_comercial_mod < 1 :
                        break  
                    else:
                        print("Por favor digite una comision menor a 1")
                except ValueError:
                    print(" ")            
    # Iterar sobre la lista de clientes y modificar los nombres
            for comercial in diccionario['ventas']['comerciales']:
                if comercial['id'] == id_comercial_mod:  # Modificar el nombre del cliente con ID 4
                    comercial['nombre'] = nombre_comercial_mod
                    comercial["apellido1"]=apellido1_comercial_mod
                    comercial["apellido2"]=apellido2_comercial_mod
                    comercial["comision"]=comision_comercial_mod
  
            # Guardar los cambios en el mismo JSON (sobreescribir)
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)
        if decision4==4:
            print("")





############################################ ELIMINAR ############################################
    elif decision3==3:
        print("\033[91m1. Eliminar datos de cliente segun id")
        print("2. Eliminar pedido")
        print("3. Eliminar comercial")
        print("4. Salir")
        decision5=int(input("--> "))
        if decision5==1:
            for i in clientes:
                print(i)
            print("")
            id_cliente_a_eliminar=int(input("Id del cliente a eliminar: "))
            eliminar_cliente_por_id(id_cliente_a_eliminar)
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)

        if decision5==2:
            # ID del pedido que deseas eliminar
            for i in pedidos:
                print(i)
            print("")
            id_pedido_a_eliminar = int(input("ID del pedido que desea eliminar: "))

            # Eliminar el pedido por su ID
            eliminar_pedido_por_id(id_pedido_a_eliminar)

            # Guardar los cambios en el archivo JSON
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)
        if decision5==3:
            # ID del comercial que deseas eliminar
            for i in comerciales:
                print(i)
            print("")
            id_comercial_a_eliminar = int(input("Ingrese la ID del comercial que desea eliminar: "))

            # Eliminar el comercial por su ID
            eliminar_comercial_por_id(id_comercial_a_eliminar)

            # Guardar los cambios en el archivo JSON
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)


        if decision5==4:
            print("")




############################################ AGREGAR ############################################
    elif decision3==4: 
        print("\033[92m1. Agregar nuevo cliente")
        print("2. Agregar nuevo pedido")
        print("3. Agregar nuevo comercial")
        print("4. Salir")
        decision5=int(input("---> "))
        if decision5==1:
            for i in clientes:
                print(i)
            print("")
            id=int(input("Nueva id: "))
            name=str(input("Nombre cliente: "))
            ape1=str(input("Apellido cliente: "))
            ape2=str(input("Apellido 2 cliente: "))
            ciudad=str(input("Ciudad cliente: "))
            categoria=int(input("Categoria cliente: "))
            nuevo_cliente = {
                "id": id,
                "nombre": name,
                "apellido1": ape1,
                "apellido2": ape2,
                "ciudad": ciudad,
                "categoría": categoria
            }

            # Agregar el nuevo cliente
            agregar_nuevo_cliente(nuevo_cliente)

            # Guardar los cambios en el archivo JSON
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)

        if decision5==2:
            for i in pedidos:
                print(i)
            print("")
            # ID del cliente existente para el cual deseas agregar el pedido
            id_cliente_existente = int(input("ID cliente que realiza el pedido:"))
            # Crear un nuevo pedido
            id_cliente_pedido=int(input("Id del nuevo pedido: "))
            total_cliente_pedido=float(input("Total del nuevo pedido: "))
            año=str(input("Año del pedido: "))
            mes=str(input("Mes del pedido: "))
            dia=str(input("Dia del pedido: "))
            id_comercial_pedido=int(input("Id del comercial: "))
            gion=str("-")
            nuevo_pedido = {
                "id": id_cliente_pedido,
                "total": total_cliente_pedido,
                "fecha": año+gion+mes+gion+dia,
                "id_comercial": id_comercial_pedido
            }


            # Agregar el nuevo pedido para el cliente existente
            agregar_pedido_para_cliente_existente(id_cliente_existente, nuevo_pedido)

            # Guardar los cambios en el archivo JSON
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)

        if decision5==3:
            for i in comerciales:
                print(i)
            print("")
            id_new_comercial=int(input("Nueva id comercial: "))
            name_new_comercial=str(input("Nombre comercial: "))
            ap1_new_comercial=str(input("Apellido comercial: "))
            ap2_new_comercial=str(input("Apellido 2 comercial: "))
            while True:
                try: #Comprobar que el numero este entre el rango 1-1000 y que no tenga decimales.
                    comision_new_comercial=float(input("Comision comercial: "))
                    if comision_new_comercial < 1 :
                        break  
                    else:
                        print("Por favor digite una comision menor a 1")
                except ValueError:
                    print(" ")    
            # Crear un nuevo comercial
            nuevo_comercial = {
                "id": id_new_comercial,
                "nombre": name_new_comercial,
                "apellido1": ap1_new_comercial,
                "apellido2": ap2_new_comercial,
                "comision": comision_new_comercial
            }

            # Agregar el nuevo comercial
            agregar_nuevo_comercial(nuevo_comercial)

            # Guardar los cambios en el archivo JSON
            with open('datos.json', 'w') as file:
                json.dump(diccionario, file, indent=2)
        if decision5==4:
            print("")
## Desarrollado por Eduar Damian Chanaga Gonzalez - 1095581647