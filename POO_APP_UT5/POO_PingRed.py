import subprocess, time

# Importamos la librería "subprocess" para poder ejecutar comandos del sistema (en este caso el comando 'ping'), y capturar la salida de este para mostrarla a continuación (stdout).
# Importamos la librería "time" para poder detener la ejecución del código unos segundos (time.sleep(2)), simulando así la espera de que un proceso termine.

class Ping:

    @staticmethod
    def Red(paquetes, red):

        try:
            print("\nEnviado paquetes a "+red+" ...")

            # Simulamos el tiempo de espera con dos 2 segundos
            time.sleep(2)

            proceso = subprocess.run(["ping", "-n", str(paquetes), str(red)], capture_output=True, text=True, timeout=5, check=True)

            print("\n== RESULTADO ==")
            print(proceso.stdout)

        except subprocess.TimeoutExpired:
            print("\nNo hay conexion con "+red+", ha tardado mas de 5 segundos en responder.")

        except subprocess.CalledProcessError:
            print("\nLa IP introducida no es una direccion valida o ha introducido el nº de paquetes en texto (debe ser numerico: 1, 2, 3...).")