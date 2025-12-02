import platform, subprocess

SO = platform.system()

try:
    if SO == "Linux":
        print("\n\nSu sistema operativo es: ",SO)
        comando = input("\nComando a ejecutar: ")
        proceso = subprocess.run(comando, text=True, shell=True, check=True, capture_output=True)
        print("\===== RESULTADO =====")
        print(proceso.stdout)
    elif SO == "Darwin":
        print("\n\nSu sistema operativo es: ",SO)
        comando = input("\nComando a ejecutar: ")
        proceso = subprocess.run(comando, text=True, shell=True, check=True, capture_output=True)
        print("\===== RESULTADO =====")
        print(proceso.stdout)
    elif SO == "Windows":
        print("\n\nSu sistema operativo es: ",SO)
        comando = input("\nComando a ejecutar (Si es de PowerShell introduzca 'powershel comando'): ")
        proceso = subprocess.run(comando, text=True, shell=True, check=True, capture_output=True)
        print("\===== RESULTADO =====")
        print(proceso.stdout)
    else:
        print("\n\nNo se ha podido detectar su sistema operativo")
except subprocess.CalledProcessError as e:
    print("\nHa ocurrido un error: ",e)
except Exception as e:
    print("\nHa ocurrido un error inesperado: ",e)