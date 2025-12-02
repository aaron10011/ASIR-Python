import os, platform

def info_sistema():

    nombre_so = platform.system()
    version = platform.version()
    ruta_inicial = os.getcwd()

    print("\nNombre del SO: ", nombre_so)
    print("Version: ", version)
    print("Ruta de trabajo actual: ", ruta_inicial,"\n")

    return ruta_inicial

#def ruta_inicial():

    #ruta_inicial = os.getcwd()
    #return ruta_inicial

def crear_directorios():

    if os.path.exists("./proyecto"):
        print("El directorio 'proyecto' ya existe.")
        os.chdir("proyecto")
        print("\nAhora estas en el directorio proyecto, Ruta actual: ",os.getcwd())
    else:
        print("El directorio 'proyecto' no existe, creando...")
        os.mkdir("proyecto")
        os.chdir("proyecto")
        print("\nAhora estas en el directorio proyecto, Ruta actual: ",os.getcwd())

    os.mkdir("docs")
    os.mkdir("src")

    os.chdir("src")
    os.mkdir("modulos")

def cambiar_directorio(directorio_original):

    os.chdir(directorio_original)
    print("\nHas vuelto al directorio donde ejecutaste el programa: ",os.getcwd())

def listar_recursivo(directorio_original):

    ruta_principal = os.path.join(directorio_original, "proyecto")
    os.chdir(ruta_principal)

    so = platform.system()
    if so == "Windows":
        os.system("dir /s")
    elif so == "Linux" or so == "Darwin":
        os.system("ls -lR")

def main():
    
    directorio_principal = info_sistema()
    crear_directorios()

    cambiar_directorio(directorio_principal)
    listar_recursivo(directorio_principal)

if __name__ == "__main__":
    main()