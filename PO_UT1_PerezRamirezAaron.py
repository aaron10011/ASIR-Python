import subprocess

try:
    comando = input("\nComando que desea ejecutar (Si es de powershell introduzca 'powershell (comando)'): ")

    proceso = subprocess.run(comando, text=True, shell=True, check=True, capture_output=True)

    print ("\nCOMPLETADO!!")
    print(proceso.stdout)

except subprocess.CalledProcessError as e:

    print("\nHa ocurrido un error: ", e)

except Exception as e:

    print("\nHa ocurrido un error insperado: ", e)
