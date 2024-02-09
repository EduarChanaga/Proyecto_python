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

print("Bienvenido")
print("Que tipo de usuario desea ingresar?")
print("1. Camper")
print("2. Trainar")
print("3. COrdinador")
Decision1=int(input("--> "))
## Desarrollado por Eduar Damian Chanaga Gonzalez - 1095581647