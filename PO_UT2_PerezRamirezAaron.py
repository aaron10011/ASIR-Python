import os, shutil

opcion = ""
carpeta = ""
try:
    while opcion != "5":
        print("\n===== MENU DE OPCIONES =====\n")
        print("1. Crear carpeta principal y subniveles")
        print("2. Crear o añadir archivo (muestra información del archivo)")
        print("3. Renombrar archivo")
        print("4. Eliminar carpeta principal y subniveles")
        print("5. Salir\n")

        opcion = input("Elija una de las siguientes opciones(1,2,3...): ")

        match opcion:
            case "1":
                rutaentera = ""
                carpeta = input("\nNombre de la carpeta a crear: ")
                os.mkdir(carpeta)
                os.chdir(carpeta)
                rutaentera += carpeta

                subcarpeta = ""
                while subcarpeta != "salir":
                    subcarpeta = input("\nQuiere crear una subcarpeta? (Escriba 'salir' para cancelar): ")

                    if subcarpeta == "salir":
                        print("\nSaliendo...")
                        break
                    else:
                        os.mkdir(subcarpeta)
                        os.chdir(subcarpeta)
                        rutaentera += "/" + subcarpeta
            case "2": 
                archivo = input("\nNombre del archivo a crear/modificar: ")
                contenido = input("\nContenido a añadir en el archivo: ")
                ruta = "./"+archivo

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
                
                print("\nTamaño en bytes: ",os.path.getsize(ruta))
                print("Ultima fecha de modificacion: ",os.path.getmtime(ruta))
                print("Ultima fecha de acceso: ",os.path.getatime(ruta))

                if os.path.isfile(ruta):
                    print("Es un archivo\n")
                elif os.path.isdir(ruta):
                    print("Es un directorio\n")

            case "3":
                viejo = input("\nNombre del archivo a renombrar: ")
                if os.path.exists(viejo):
                    nuevo = input("\nNuevo nombre: ")
                    os.rename(viejo, nuevo)
                else:
                    print("\nEl archivo no existe")

            case "4":
                confirmacion = input("\nEsta seguro de eliminar la carpeta y su contenido? (si/no): ")

                if confirmacion == "no":
                    print("\nCancelando operacion...")
                elif confirmacion == "si":
                    shutil.rmtree(carpeta)
                    print("\nCarpetas borradas")
                else:
                    print("\nOpcion Invalida, cancelando operacion...")
            case "5": print("\nSaliendo...")
            case _: print("\nOpcion Incorrecta")

except Exception as e:
    print("\nHa ocurrido un error inesperado: ",e)