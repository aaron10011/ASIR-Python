import platform

# Importamos la librería "platform" para obtener información sobre el entorno donde se ejecuta, como el sistema operativo, el nombre del equipo, el intérprete de Python y la arquitectura del procesador.

class SistemaOperativo:

    def __init__(self):
        self.so = platform.system()

    def TipoSistema(self):
        print("\nSu sistema operativo es: " + self.so)

    @staticmethod
    def HostName():
        nombre = platform.node()
        print("\nNombre de su equipo: " + nombre)
    
    @staticmethod
    def ArquitecturaSistema():
        arquitectura = platform.architecture()[0]
        print("\nArquitectura de su sistema: " + str(arquitectura))

    @staticmethod
    def VersionPython():
        version = platform.python_version()
        print("\nVersión de Python: " + str(version))
    
    def DevolverTipoSistema(self):
        return self.so