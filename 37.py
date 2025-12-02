try:
    calificaciones = {
        "Ana": 8.5,
        "Luis": 7.0,
        "Maria": 9.2,
        "Carlos": 6.8
    }

    sumanota = 0
    totalestudiantes = 0

    print("\n===== ESTUDIANTES =====\n")
    for nombre, nota in calificaciones.items():
            
            print(nombre,"=",nota)

            sumanota += nota
            totalestudiantes += 1

    notamedia = sumanota / totalestudiantes
    print("\nLa nota media de todos los estudiantes es: ",notamedia)

    print("\n===== ESTUDIANTES CON UN 8 O SUPERIOR =====\n")

    for nombre, nota in calificaciones.items():

        if nota >= 8:
            print(nombre,"=",nota) 
    
    print("")

except TypeError:
    print("\nERROR, no se puede operar matematicamente con texto.")

except Exception as e:
    print("\nHa ocurrido un error inesperado: ", e)