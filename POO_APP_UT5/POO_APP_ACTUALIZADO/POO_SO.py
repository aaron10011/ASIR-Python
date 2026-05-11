import os

# Importamos la librería "os" para poder interactuar con el sistema operativo a nivel de rutas de archivos, creación de carpetas y obtención de información (sobre un archivo o de nuestra localización en el sistemas (os.getcwd()))


class GestorArchivos:

    def __init__(self):
        # Lo hacemos privado con "__" para que no se pueda modificar desde fuera de la clase.
        self.__ruta_actual = os.getcwd()
    
    def ObtenerRuta(self):
        return self.__ruta_actual

    @staticmethod
    def CrearCarpeta():

        nueva_carpeta = input("\nNombre de la carpeta a crear (se creara en la carpeta actual si no se especifica ruta), escriba 'cancelar' para cancelar: ")

        if nueva_carpeta.lower() == "cancelar":
            print("\nCancelando operacion...")

        elif not nueva_carpeta:
            print("\nNo se pueden crear carpetas sin nombre en Windows, intentelo de nuevo.")

        elif os.path.exists(nueva_carpeta):
            print("\nYa existe un objeto con ese nombre, vuelva a intentarlo.")

        else:
            os.mkdir(nueva_carpeta)
            print("\nLa carpeta "+nueva_carpeta+" se ha creado correctamente.")

    def CambiarCarpeta(self):
    
        chdir_carpeta = input("\nRuta hacia la carpeta a la que se quiere mover: ")
        
        if os.path.isdir(chdir_carpeta):
            os.chdir(chdir_carpeta)
            self.__ruta_actual = os.getcwd()
            print("\nRuta cambiada con exito.")

        else:
            print("\nLa carpeta no existe o no ha introducido nada.")

    def ListarCarpeta(self):

        listar_carpeta = input("\nIntroduzca la ruta completa de la carpeta que quiere listar (no introduzca nada para listar la carpeta actual): ")

        if not listar_carpeta:
            print("\n== CONTENIDO DE '"+self.__ruta_actual+"' ==\n")
            for objeto in os.listdir(self.__ruta_actual):
                print("- ", objeto)

        elif os.path.isdir(listar_carpeta):
            print("\n== CONTENIDO DE '"+listar_carpeta+"' ==\n")
            for objeto in os.listdir(listar_carpeta):
                print("- ", objeto)

        else:
            print("\nNo se ha encontrado la carpeta introducida, intentelo de nuevo.")

    @staticmethod      
    def CrearArchivo():

        nombre_archivo = input("\nNombre del archivo a crear (se creara en el directorio actual si no se especifica la ruta), escriba 'cancelar' para cancelar: ")

        if nombre_archivo.lower() == "cancelar":
            print("\nCancelando operacion...")
        
        elif not nombre_archivo:
            print("\nNo se puede crear un archivo sin nombre en Windows.")

        else:
            contenido_archivo = input("\nContenido a añadir en el archivo: ")

            if os.path.exists(nombre_archivo):
                print("\nYa existe un objeto con ese nombre, vuelva a intentarlo.")

            else:
                modo = "w"
                with open(nombre_archivo, modo) as archivo:
                    archivo.write(contenido_archivo + "\n")

                print("\nArchivo creado !!")

    @staticmethod
    def InformacionArchivo():

        info_archivo = input("\nIntroduzca la ruta del archivo que desea ver su informacion: ")

        if os.path.isfile(info_archivo):

            tamanio = os.path.getsize(info_archivo)
            fecha_mod = os.path.getmtime(info_archivo)
            fecha_acceso = os.path.getatime(info_archivo)
            
            return tamanio, fecha_mod, fecha_acceso

        elif not info_archivo:
            print("\nNo ha introducido ningun valor...")
            return None

        else:
            print("\nNo se ha encontrado el archivo introducido, asegurece de introducir la extension tambien (.txt, .pdf, .py).")
            return None

    @staticmethod
    def EliminarArchivo():

        nombre_objeto = input("\nRuta hacia el archivo a eliminar: ")

        if os.path.isfile(nombre_objeto):

            confirmacion = input("\nEsta seguro de eliminar el archivo '"+nombre_objeto+"'? (si/no): ")
            if confirmacion.lower() == "si":
                os.remove(nombre_objeto)
                print("\nEl archivo '"+nombre_objeto+"' ha sido eliminado")

            else:
                print("\nCancelando operacion...")

            return None

        elif os.path.isdir(nombre_objeto):

            confirmacion = input("\nEsta seguro de eliminar la carpeta '"+nombre_objeto+"' y todo su contenido? (si/no): ")
            if confirmacion.lower() == "si":
                return nombre_objeto

            else:
                print("\nCancelando operacion...")
                return None

        elif not nombre_objeto:
            print("\nNo ha introducido ningun valor...")
            return None

        else:
            print("\nNo se ha encontrado el objeto introducido, vuelva a intentarlo.")
            return None