import os

def carpeta_principal():

    carpeta = input("\nIndique el nombre de una carpeta que quiera crear: ")
    if not os.path.exists(carpeta):
        os.mkdir(carpeta)
        print("\nEl directorio",carpeta,"se ha creado correctamente.")
        return carpeta
    else:
        print("\nError, el directorio",carpeta,"ya existe.\n")
        exit()

def crear_subcarpetas(carpeta):

    subcarpeta = ""
    ruta_act = carpeta

    while subcarpeta != "Salir":
        subcarpeta = input("\nQuiere crear una subcarpeta? (Escriba 'Salir' para cancelar): ")
        if subcarpeta == "Salir":
            print("\nSaliendo...")
            break
        else:
            ruta_act = os.path.join(ruta_act, subcarpeta)
            os.makedirs(ruta_act)
    print("\nRuta final creada: ",ruta_act)
    return ruta_act

def editar_archivo(ruta_final):

    nombre_archivo = input("\nNombre del archivo que desea crear: ")
    ruta_archivo = os.path.join(ruta_final, nombre_archivo)

    if os.path.exists(ruta_archivo):
        opcion = input("Su archivo ya existe, escriba 'w' para sobreescribir o 'a' para añadir: ")
                    
        if opcion == "w":
            modo = "w"
        
        elif opcion == "a":
            modo = "a"
           
        else:
            print("\nOpcion Incorrecta")
            exit()
    else:
        print("El archivo no existe, se creará uno nuevo")
        modo = "w"
    
    with open(ruta_archivo, modo) as archivo:
        contenido = input("\nContenido a añadir en el archivo: ")
        archivo.write(contenido + "\n")
    print("\nArchivo editado correctamente")

def listar_ultimo_nivel(ruta_final):
    print("\nContenido del último nivel: ", os.listdir(ruta_final),"\n")

def renombrar_archivo():
    nombre_anterior = input("\nIngrese la ruta completa del archivo que quiere renombrar: ")

    if not os.path.exists(nombre_anterior):
        print("\nEl archivo no existe.")
        exit()
    else:
        nombre_nuevo = input("Nuevo nombre (Escriba la ruta completa): ")
        os.rename(nombre_anterior, nombre_nuevo)
        print("\nCambio de nombre completado")

def menu(ruta_final):

    opc = ""
    while opc != "4":
        print("\n===== MENU DE OPCIONES =====\n")
        print("1. Crear o añadir archivos")
        print("2. Listar archivos y carpetas")
        print("3. Renombrar archivos")
        print("4. Salir\n")
        opc = input("Elija una de las siguientes opciones: ")

        match opc:
            case "1":
                editar_archivo(ruta_final)
            case "2":
                listar_ultimo_nivel(ruta_final)
            case "3":
                renombrar_archivo()
            case "4":
                print("\nSaliendo...")
            case _:
                print("\nOpción incorrecta")

def main():
    
    carpeta_inicial = carpeta_principal()
    ruta_final = crear_subcarpetas(carpeta_inicial)
    menu(ruta_final)

if __name__ == "__main__":
    main()