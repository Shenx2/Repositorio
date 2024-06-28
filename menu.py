import os
import time
import funciones

while True:

    print("*******************************")
    print("****     MUNDO LIBRO :)    ****")
    print("*******************************")
    print("[1] - Mantenedor de categorias")
    print("[2] - Reportes")
    print("[3] - Salir")
    print("*******************************")
    print("*******************************")
    print("*******************************")

    opc = input("Ingrese una opción: ")
    
    os.system("cls")
    time.sleep(1)

    if opc == "1":
            
            print("*******************************")
            print("**** MANTENEDOR CATEGORIAS ****")
            print("*******************************")
            print("[1] Agregar categoria")
            print("[2] Editar categoria")
            print("[3] Eliminar categoria")
            print("[4] Buscar categoria")
            print("[5] Volver")
            opc2 = input("Ingrese una opción: ")

    elif opc == "2":
          print("**** Reportes ****")
          print("[1] Escribir reporte")
          print("[2] Volver")
    
    elif opc == "3":
          break



