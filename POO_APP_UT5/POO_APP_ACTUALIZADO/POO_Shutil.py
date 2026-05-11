import shutil

# Importamos la librería "shutil" para poder borrar de forma recursiva la carpeta que el usuario indique y todo su contenido.

class Borrar:

    @staticmethod
    def BorrarCarpeta(carpeta):
        try:
            shutil.rmtree(carpeta)
            print("\nLa carpeta '"+carpeta+"' y su contenido ha sido eliminada.")

        except Exception as e:
            print("\nHa ocurrido un error borrando la carpeta: ",e)