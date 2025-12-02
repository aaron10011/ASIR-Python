import os

carpeta = input("\nIndique el nombre de una carpeta que quiera crear: ")

if not os.path.exists(carpeta):
    os.mkdir(carpeta)
    print("\nEl directorio",carpeta,"se ha creado correctamente.")

    os.chdir(carpeta)
    print("\nCambiando al directorio",carpeta,"...")

    subcarpeta = ""

    while subcarpeta != "Salir":
        subcarpeta = input("\nQuiere crear una subcarpeta? (Escriba 'Salir' para cancelar): ")
        if subcarpeta == "Salir":
            print("\nSaliendo...")
            break
        else:
            os.mkdir(subcarpeta)
            os.chdir(subcarpeta)
            print("\nCambiando al directorio",subcarpeta,"...")
    
    opc = ""
    while opc != "4":
        print("\n===== MENU DE OPCIONES =====\n")
        print("1. Crear o añadir archivos\n")
        print("2. Listar archivos y carpetas\n")
        print("3. Renombrar archivos\n")
        print("4. Salir\n")
        opc = input("Elija una de las siguientes opciones: ")

        match opc:
            case "1":
                nombre = input("\nNombre del archivo: ")
                contenido = input("\nContenido a añadir en el archivo: ")
                ruta = "./"+nombre+".txt"

                if not os.path.exists(ruta):
                    modo = "w"
                    print("\nArchivo creado !!")
                    with open(ruta, modo) as archivo:
                        archivo.write(contenido + "\n")
                else:
                    opcion = input("\nEl archivo existe, quiere añadir (a) o sobreescribir (s)?: ")
                    
                    if opcion == "s":
                        modo = "w"
                        print("\nHas seleccionado sobreescribir.")
                        with open(ruta, modo) as archivo:
                            archivo.write(contenido + "\n")
                    elif opcion == "a":
                        modo = "a"
                        print("\nHas seleccionado añadir.")
                        with open(ruta, modo) as archivo:
                            archivo.write(contenido + "\n")
                    else:
                        print("\nOpcion Incorrecta")

            case "2":
                os.system("dir /s")
            case "3":
                viejo = input("\nNombre del archivo a renombrar: ")
                nuevo = input("\nNuevo nombre: ")
                os.rename(viejo, nuevo)
            case "4":
                print("\nSaliendo...")
            case _:
                print("\nOpcion Incorrecta.")

else:
    print("\nError, el directorio",carpeta,"ya existe.")