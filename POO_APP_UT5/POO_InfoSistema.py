import platform, subprocess

# Importamos la librería "platform" para obtener información sobre el entorno donde se ejecuta, como el sistema operativo, el nombre del equipo, el intérprete de Python y la arquitectura del procesador.
# Importamos la librería "subprocess" para poder ejecutar un comando del sistema, en este caso para poder limpiar la terminal.

class SistemaOperativo:

    @staticmethod
    def TipoSistema():
        so = platform.system()
        print("\nSu sistema operativo es: " + so)

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

    @staticmethod
    def LimpiarConsola():
        if platform.system() == "Windows":
            subprocess.run(["cls"], shell=True)
            
        elif platform.system() == "Linux":
            subprocess.run(["clear"], shell=True)