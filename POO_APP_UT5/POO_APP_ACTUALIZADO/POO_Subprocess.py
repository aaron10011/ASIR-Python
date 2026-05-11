import subprocess

# Importamos la librería "subprocess" para poder ejecutar comandos del sistema (en este caso el comando 'ping' y 'cls'), y capturar la salida de este para mostrarla a continuación (stdout).

class Ping:

    @staticmethod
    def Red(sistema, paquetes, red):

        try:
            if sistema == "Windows":
                proceso = subprocess.run(["ping", "-n", str(paquetes), str(red)], capture_output=True, text=True, timeout=5, check=True)

                print("\n== RESULTADO ==")
                print(proceso.stdout)

            elif sistema == "Linux" or sistema == "Darwin":
                proceso = subprocess.run(["ping", "-c", str(paquetes), str(red)], capture_output=True, text=True, timeout=5, check=True)

                print("\n== RESULTADO ==")
                print(proceso.stdout)

            else:
                print("\nNo se ha podido detectar su sistema operativo, esta función no esta disponible.")

        except subprocess.TimeoutExpired:
            print("\nNo hay conexion con "+red+", ha tardado mas de 5 segundos en responder.")

        except subprocess.CalledProcessError:
            print("\nLa IP introducida no es una direccion valida o ha introducido el nº de paquetes en texto (debe ser numerico: 1, 2, 3...).")

class LimpiarConsola:

    @staticmethod
    def Limpiar(sistema):
        if sistema == "Windows":
            subprocess.run(["cls"], shell=True)
            
        elif sistema == "Linux" or sistema == "Darwin":
            subprocess.run(["clear"], shell=True)

        else:
            print("\nNo se ha podido detectar su sistema operativo, esta función no esta disponible.")