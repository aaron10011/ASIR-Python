import platform

pregunta = input("\nDesea ver la información del sistema (si, no, salir): ")



while pregunta != "salir" and pregunta != "Salir":

    if pregunta == "sí" or pregunta == "Si" or pregunta == "si":
        print("\n===== MENU DE PLATFORM =====")
        print("\n1. Versión del SO")
        print("2. Nombre de la máquina")
        print("3. Versión de python")
        print("4. Arquitectura del sistema")
        print("5. Toda la información")
        print("6. Salir")
        opcion = input("\nSeleccione una opción (1-6): ")

        match opcion:
            case "1": print("\n",platform.version(),"\n")
            case "2": print("\n",platform.node(),"\n")
            case "3": print("\n",platform.python_version(),"\n")
            case "4": print("\n",platform.architecture(),"\n")
            case "5": print("\n",platform.uname(),"\n")
            case "6":
                print("\nHasta la próxima!!\n")
                pregunta = input("Desea ver la información del sistema (si, no, salir): ")
            case _: print("\nOpción no válida, elige entre 1 y 6\n")

    elif pregunta == "No" or pregunta == "no":
        print("\nDe acuerdo, hasta la proxima!!\n")
        pregunta = input("Desea ver la información del sistema (si, no, salir): ")

    else:
        print("\nRespuesta errónea\n")
        pregunta = input("Desea ver la información del sistema (si, no, salir): ")

if pregunta == "salir" or pregunta == "Salir":
    print("\nSaliendo...\n")