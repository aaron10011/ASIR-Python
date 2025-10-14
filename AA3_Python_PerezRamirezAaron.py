try:
    ssid = str(input("\nIntroduzca el SSID (Nombre) de la red Wifi: "))
    ancho = float(input("Introduzca el ancho de banda en MHz: "))
    tiposeg = str(input("Tipo de seguridad de la red (WPA2, WPA3 o abierta): "))
    conectado = str(input("El equipo esta conectado? (Si/No): "))
except ValueError:
    print("\nError: Alguno de los valores no es válido.")
    ssid = "desconocido"
    ancho = 0.0
    tiposeg = "indefinida"
    conectado = "no"

print("\nDatos ingresados:")
print("\nSSID:", ssid)
print("Ancho de Banda:", ancho, "MHz")
print("Tipo de Seguridad:", tiposeg)
print("Conectado:", conectado)
print("\n")