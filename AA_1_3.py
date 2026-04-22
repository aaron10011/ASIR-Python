class Libro:
    def __init__(self,titulo,autor,prestado):
        self.titulo = titulo
        self.autor = autor
        self.prestado = prestado

    def cambiar_autor(self,nuevo_autor):
        self.autor = nuevo_autor
        print("\nSe ha cambiado el autor a: " + nuevo_autor)

    def prestar(self):
        if self.prestado == True:
            print("\nEl libro ya está prestado.")
        else:
            self.prestado = True
            print("\nSe ha prestado el libro.")
    
    def devolver(self):
        if self.prestado == False:
            print("\nEl libro ya está disponible.")
        else:
            self.prestado = False
            print("\nSe ha devuelto el libro.")

    def mostrar_info(self):
        print("\nTitulo: " + self.titulo)
        print("Autor: " + self.autor)
        if self.prestado == True:
            print("Estado: El libro está prestado.\n")
        else:
            print("Estado: El libro está disponible.\n")

libro1 = Libro("Prueba","Prueba",False)

libro1.prestar()
libro1.devolver()
libro1.cambiar_autor("Aaron")
libro1.mostrar_info()