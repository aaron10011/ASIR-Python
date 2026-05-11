import time

# Importamos la librería "time" para convertir la salida de "os.path.getmtime()" y "os.path.getatime()" a un formato legible para el usuario, usando para ello "time.ctime()".
# También para simular un tiempo de espera durante la ejecución del comando "ping".

class Tiempo:

    @staticmethod
    def Espera(segundos):
    
        time.sleep(segundos)

    @staticmethod
    def Formato(tamanio, modificacion, acceso):

        print("\n=== INFO. DEL ARCHIVO ===")

        print("\nTamaño en bytes: " + str(tamanio))
        print("Ultima fecha de modificacion: " + str(time.ctime(modificacion)))
        print("Ultima fecha de acceso: " + str(time.ctime(acceso)))