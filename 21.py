import platform

pregunta = input("\nDesea ver la información del sistema: ")
SO = platform.system()
Bits = platform.architecture()

if pregunta == "sí" or pregunta == "Si" or pregunta == "si":
    print("\n===== INFORMACIÓN SISTEMA =====")
    print("\nVersion del SO: ",platform.version())
    print("Nombre de la máquina: ",platform.node())
    print("Versión de python: ",platform.python_version())
    print("Arquitectura del sistema: ",platform.architecture())
    print ("Más información: ",platform.uname(),"\n")

    if SO == "Linux":
        print("Tienes un Linux !!")
    elif SO == "Darwin":
        print("Tienes un macOS !!")
    elif SO == "Windows":
        print("Tienes un Windows !!\n")

    if Bits[0] == "64bit":
        print("Tines una arquitectura de 64 bits !!\n")
    elif Bits[0] == "32bit":
        print("Tines una arquitectura de 32 bits !!\n")
        
elif pregunta == "No" or pregunta == "no":
    print("\nDe acuerdo, hasta la proxima!!\n")
else:
    print("\nRespuesta errónea\n")
