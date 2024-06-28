import json

def eliminar_categ(CategoriaID):
    with open("biblioteca.json", "r") as jsonLect:
        leer_json = json.pop(jsonLect)
        eliminar_categoria = {
            "CategoriaID"
        }


def agregar_categ(Nombre):
    with open("biblioteca.json", "r") as jsonLect:
        leer_json = json.load(jsonLect)
        agregar_categoria = {
            "CategoriaID": len(leer_json["Categoria"])+1,
            "Nombre": Nombre
        }
    leer_json["Categoria"].append(agregar_categoria)
    with open("biblioteca.json", "w") as jsonEscritura:
        json.dump(leer_json, jsonEscritura, indent=4)
        print("La categoria ha sido agregadada exitosamente")


def editar_categ(id):
    contador = 0
    with open("biblioteca.json", "r") as jsonLect:
        leer_json = json.load(jsonLect)
        for i in leer_json["Categoria"]:
            if i ["CategoriaID"] == id:
                print("Se ha encontrado")
                break
            elif contador == range(leer_json(["Categoria"]))