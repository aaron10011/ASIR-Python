import os, platform

so = platform.system()

try:
    print("\n===== Información del SO =====")
    print("\nSistema operativo:",so)
    print("Versión:",platform.version(),"\n")

    padre = "./directoriopadre"
    hijo = "directoriohijo"

    if not os.path.exists(padre):
        os.mkdir(padre)
        print("El directorio",padre,"se ha creado correctamente.")
    else:
        print("Error, el directorio",padre,"ya existe.")

    os.chdir(padre)
    print("\nCambiamos de directorio:",os.getcwd())

    if so == "Windows":
        os.system("dir /s")
    elif so == "Linux" or so == "Darwin":
        os.system("ls -lR")

    if not os.path.exists(hijo):
        os.mkdir(hijo)
        print("\nEl directorio",hijo,"se ha creado correctamente.")
    else:
        print("\nError, el directorio",hijo,"ya existe.")
    
    os.chdir(hijo)
    print("\nCambiamos de directorio otra vez:",os.getcwd())

except OSError as e:
    print("Ha ocurrido un error:",e)

except Exception as e:
    print("Ha ocurrido un error inesperado:",e)