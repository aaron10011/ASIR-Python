print("\n========== MENÚ DE NAVEGADORES ==========")
print("\n1. Google Chrome")
print("2. Mozilla Firefox")
print("3. Microsoft Edge")
print("4. Safari\n")
print("===========================================")

try:
    opcionusu = input("\nElija una opción: ")

    if opcionusu.isdigit():
        opcion = int(opcionusu)

        match opcion:
            case 1:
                buscar = input("\nQue desea buscar?: ")
                print("\nHa seleccionado Google Chrome, buscando",buscar)
            case 2:
                buscar = input("\nQue desea buscar?: ")
                print("\nHa seleccionado Mozilla Firefox buscando",buscar)
            case 3:
                buscar = input("\nQue desea buscar?: ")
                print("\nHa seleccionado Microsoft Edge buscando",buscar)
            case 4:
                buscar = input("\nQue desea buscar?: ")
                print("\nHa seleccionado Safari buscando",buscar)
            case _:
                print("\nNavegado no valido (Elija 1, 2, 3 o 4)")
    else:
        print("\nDebes de escribir un numero")

except Exception as e:

    print("\nHa ocurrido un error:",e)

finally:

    print("\nLa ejecucion ha salido correctamente\n")