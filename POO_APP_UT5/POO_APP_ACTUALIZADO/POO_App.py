from POO_Platform import SistemaOperativo
from POO_SO import GestorArchivos
from POO_Subprocess import Ping, LimpiarConsola
from POO_Shutil import Borrar
from POO_Time import Tiempo

def menu():

    objeto = GestorArchivos()
    ping = Ping()
    consola = LimpiarConsola()
    sistema = SistemaOperativo()
    borrado = Borrar()
    tiempo = Tiempo()

    opc = -1
    while opc != "0":
        print("\n===== MENU PRINCIPAL DE OPCIONES =====\n")
        print("1. Info. del Sistema")
        print("2. Gestion de Archivos")
        print("3. Prueba Conexion (Ping)")
        print("4. Limpiar consola")
        print("0. Salir\n")
        opc = input("Seleccione una opcion: ")

        match opc:
            case "1":

                opc_infosistema = -1
                while opc_infosistema != "0":
                    print("\n=== INFORMACION DEL SISTEMA ===\n")
                    print("1. Ver el tipo de su sistema")
                    print("2. Ver el nombre de su equipo")
                    print("3. Ver la arquitectura de su sistema")
                    print("4. Ver la version de Python instalada")
                    print("0. Cancelar\n")
                    opc_infosistema = input("Seleccione una opción: ")

                    match opc_infosistema:
                        case "1": sistema.TipoSistema()
                        case "2": sistema.HostName()
                        case "3": sistema.ArquitecturaSistema()
                        case "4": sistema.VersionPython()
                        case "0": print("\nCancelando...")
                        case _: print("\nOpcion incorrecta")

            case "2":

                opc_archivos = -1
                while opc_archivos != "0":
                    print("\n=== GESTION DE ARCHIVOS ===\n")
                    print("1. Crear nueva carpeta")
                    print("2. Cambiar de carpeta")
                    print("3. Listar carpeta")
                    print("4. Crear Archivo")
                    print("5. Ver info. archivo")
                    print("6. Eliminar Carpeta / Archivo")
                    print("0. Cancelar\n")
                    print("RUTA ACTUAL: "+objeto.ObtenerRuta()+"\n")
                    opc_archivos = input("Seleccione una opción: ")

                    match opc_archivos:
                        case "1": objeto.CrearCarpeta()
                        case "2": objeto.CambiarCarpeta()
                        case "3": objeto.ListarCarpeta()
                        case "4": objeto.CrearArchivo()
                        case "5":
                            
                            informacion = objeto.InformacionArchivo()

                            if informacion:
                                tiempo.Formato(informacion[0], informacion[1], informacion[2])

                        case "6":
                            
                            resultado = objeto.EliminarArchivo()

                            if resultado:
                                borrado.BorrarCarpeta(resultado)

                        case "0": print("\nCancelando...")
                        case _: print("\nOpcion incorrecta")
                
            case "3":
                print("\n=== PRUEBA DE CONEXION (PING) ===\n")
                red = input("A que le desea hacer ping?: ")
                paquetes = input("Indique el numero de paquetes que quiere enviar (por defecto 4): ")

                if not red:
                    print("\nNo puede dejar el destinatario vacio, vuelva a intentarlo.")
                    
                elif not paquetes:
                    print("\nEnviado paquetes a "+red+" ...")
                    tiempo.Espera(2)

                    paquetes = 4
                    ping.Red(sistema.DevolverTipoSistema(), paquetes, red)

                else:
                    print("\nEnviado paquetes a "+red+" ...")
                    tiempo.Espera(2)

                    ping.Red(sistema.DevolverTipoSistema(), paquetes, red)

            case "4": consola.Limpiar(sistema.DevolverTipoSistema())

            case "0": print("\nSaliendo...")
            case _: print("\nOpcion incorrecta, seleccione una opción del 0 al 4.")


def main():
    try:
        menu()

    except PermissionError as e:
        print("\nHa ocurrido un error por la falta de permisos durante la ejecucion del programa: ",e)

    except ValueError as e:
        print("\nHa ocurrido un error con los valores introducidos: ",e)
    
    except Exception as e:
        print("\nHa ocurrido un error inesperado: ",e)

if __name__ == "__main__":
    main()