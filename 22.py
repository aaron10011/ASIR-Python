import platform

pregunta = input("\nDesea ver la información del sistema: ")

if pregunta == "sí" or pregunta == "Si" or pregunta == "si":
    print("\n===== MENU DE PLATFORM =====")
    print("\n1. Versión del SO")
    print("2. Nombre de la máquina")
    print("3. Versión de python")
    print("4. Arquitectura del sistema")
    print("5. Toda la información")
    opcion = input("\nSeleccione una opción (1-5): ")

    match opcion:
        case "1": print("\n",platform.version(),"\n")
        case "2": print("\n",platform.node(),"\n")
        case "3": print("\n",platform.python_version(),"\n")
        case "4": print("\n",platform.architecture(),"\n")
        case "5": print("\n",platform.uname(),"\n")
        case _: print("\nOpción no válida\n")
elif pregunta == "No" or pregunta == "no":
    print("\nDe acuerdo, hasta la proxima!!\n")
else:
    print("\nRespuesta errónea\n")