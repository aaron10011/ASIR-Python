calificaciones = {
    "Ana": 8.5,
    "Luis": 7.0,
    "Maria": 9.2,
    "Carlos": 6.8
}

sumanota = 0
totalestudiantes = 0

print("")
for nombre, nota in calificaciones.items():

    if nota >= 8:
        print(nombre,"=",nota)

    sumanota += nota
    totalestudiantes += 1


notamedia = sumanota / totalestudiantes
print("\nLa nota media es:",notamedia)