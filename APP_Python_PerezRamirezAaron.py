import subprocess
try:
    host = input("\nInidica a quién quiere hacer ping: ")
    paquetes = input("Cuantos paquetes quiere enviar: ")

    ping = ["ping", "-n", paquetes, host]

    proceso = subprocess.run(ping, text=True, stdout=subprocess.PIPE)

    print("\n====Resultados====")
    print(proceso.stdout)

    print("\nERROR")
    print(proceso.stderr)

except Exception as e:
    print("Ocurrio un error: ", e)