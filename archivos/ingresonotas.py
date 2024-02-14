import json
with open("grupos.json", "r") as grups:
    grupos = json.load(grups)
with open("trainers.json", "r") as file:
    trainers = json.load(file)
        
def ingreso_notas():
    print("Bienvenido trainer ")