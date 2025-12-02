import subprocess

print("\n========== MENÚ DE OPCIONES ==========")
print("1. Windows")
print("2. Linux")
print("2. macOS")
print("======================================")

opcion = input ("\nElija una opción: ")

match opcion:
    case "1":
        try:
            comando = input ("\nComando que desea ejecutar (Si es de powershell introduzca 'powershell (comando)'): ")
            proceso = subprocess.run(comando, text=True, shell=True, check=True, capture_output=True)

            print("\n==== RESULTADO ====")
            print(proceso.stdout)

        except subprocess.CalledProcessError as e:
            print("Ha ocurrido un error:",e)

        except Exception as e:
            print("Ha ocurrido un error inesperado:",e)
        
        finally:
            print("\nTodo ha salido correctamente\n")
            
    case "2":
        comando = input ("\nComando a ejecutar: ")
        print("\nHa seleccionado el sistema Linux y el comando",comando,"\n")
    case "3":
        comando = input ("\nComando a ejecutar: ")
        print("\nHa seleccionado el sistema macOS y el comando",comando,"\n")
    case _:
        print("\nSeleccione una opción válida (1,2,3)\n")