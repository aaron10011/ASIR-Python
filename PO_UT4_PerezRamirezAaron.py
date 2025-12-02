def mb_a_bytes(mb):

    bytes = mb * 1000000
    return bytes

def mb_a_kb(mb):

    kilobytes = mb * 1000
    return kilobytes

def mb_a_gb(mb):

    gigabytes = mb * 0.001
    return gigabytes

def mb_a_tb(mb):

    terabytes = mb * 0.000001
    return terabytes

def menu(mb):

    conversion = 0
    while conversion != 5:
        print("\n===== OPCIONES DE CONVERSION =====\n")
        print("1. Convertir Megabytes a Bytes")
        print("2. Convertir Megabytes a Kilobytes")
        print("3. Convertir Megabytes a Gigabytes")
        print("4. Convertir Megabytes a Terabytes")
        print("5. Cancelar")

        conversion = float(input("\nQue conversión desea hacer? (1 - MB a Bytes, 2 - MB a KB, 3 - MB a GB, 4 - MB a TB): "))
    
        if conversion == 1:
            resultado = mb_a_bytes(mb)
            print("\nEl resultado ha sido: ",resultado)
            break
        elif conversion == 2:
            resultado = mb_a_kb(mb)
            print("\nEl resultado ha sido: ",resultado)
            break
        elif conversion == 3:
            resultado = mb_a_gb(mb)
            print("\nEl resultado ha sido: ",resultado)
            break
        elif conversion == 4:
            resultado = mb_a_tb(mb)
            print("\nEl resultado ha sido: ",resultado)
            break
        elif conversion == 5:
            print("\nCancelando...")
            exit()
        else:
            print("\nOpcion erronea, elija un numero del 1 al 4 en función de la conversión que quiere realizar.")

def main():
    megabytes = None
    
    while megabytes is None:
        entrada = input("\nIngrese los MB: ")
        
        try:
            megabytes = float(entrada)
        except ValueError:
            print("\nPor favor, introduzca un valor válido. (1, 2, 3, 4.5...)")
            megabytes = None
    
    menu(megabytes)
            
if __name__ == "__main__":
    main()