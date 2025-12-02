import os, platform

so = platform.system()

print("\n===== Información del SO =====")
print("\nSistema operativo:",so)
print("Versión:",platform.version(),"\n")

if not os.path.exists("./proyecto"):
    os.mkdir("./proyecto")
    print("El directorio proyecto se ha creado correctamente.")
else:
    print("Error, el directorio proyecto ya existe.")

os.chdir("proyecto")
print("\nCambiamos de directorio:",os.getcwd(),"\n")

if not os.path.exists("docs"):
    os.mkdir("docs")
    print("El directorio docs se ha creado correctamente.")
else:
    print("Error, el directorio docs ya existe.")

if not os.path.exists("src"):
    os.mkdir("src")
    print("El directorio src se ha creado correctamente.")
else:
    print("Error, el directorio src ya existe.")

os.chdir("src")
print("\nCambiamos de directorio:",os.getcwd(),"\n")

if not os.path.exists("modulos"):
    os.mkdir("modulos")
    print("El directorio modulos se ha creado correctamente.")
else:
    print("Error, el directorio modulos ya existe.")

os.chdir("..")
print("\nVolvemos al directorio proyecto:",os.getcwd())

print("\n===== Listado Recursivo =====\n")
if so == "Windows":
    os.system("dir /s")
elif so == "Linux" or so == "Darwin":
    os.system("ls -lR")