#Preguntar al usuario la informacion con control de la conversión con try/except
try:
    ip = str(input("\nIntroduzca la dirección IP: "))
    puerto = int(input("Introduzca el numero del puerto: "))
    masc = str(input("Introduzca la máscara de red: "))
    latencia = float(input("Introduzca la latencia (en ms): "))
    servidor = str(input("El equipo es un servidor? (si/no): "))
except ValueError:
    print("\nError: Ha introducido valores no válidos")
    ip = "desconocido"
    puerto = 0
    masc = "desconocido"
    latencia = 0.0
    servidor = "desconocido"

#Mostramos por pantalla los datos introducidos
print("\nDatos ingresados:")
print("\nDirección IP:", ip)
print("Puerto:", puerto)
print("Máscara de red:", masc)
print("Latencia:", latencia, "ms")
print("Servidor:", servidor)
print("\n")