def sumar(a, b):

    suma = a + b
    return suma

def restar(a, b):

    resta = a - b
    return resta

def multiplicar(a, b):

    multiplicacion = a * b
    return multiplicacion

def dividir(a, b):

    if b == 0:
        print("\nERROR, no se puede dividir entre 0.")
        return
    else:
        dividicion = a / b
        return dividicion
    
def menu(n1, n2):

    operacion = int(input("\nQue operación desea hacer? (1 - Sumar, 2 - Restar, 3 - Multiplicar, 4 - Dividir): "))
    
    if operacion == 1:
        resultado = sumar(n1,n2)
        print("\nEl resultado ha sido: ",resultado)
    elif operacion == 2:
        resultado = restar(n1,n2)
        print("\nEl resultado ha sido: ",resultado)
    elif operacion == 3:
        resultado = multiplicar(n1,n2)
        print("\nEl resultado ha sido: ",resultado)
    elif operacion == 4:
        resultado = dividir(n1,n2)
        print("\nEl resultado ha sido: ",resultado)
    else:
        print("\nOpcion erronea, elija un numero del 1 al 4 en función de la operacion que quiere realizar.")
        exit()

def main():
    
    try:
        primer_numero = int(input("\nIngrese un numero: "))
        segundo_numero = int(input("\nIngrese otro numero: "))

        menu(primer_numero, segundo_numero)

    except ValueError:
        print("\nIgresa un numero por favor (1, 2, 3...)")

if __name__ == "__main__":
    main()