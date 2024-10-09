'''  Instrumentos Musicales con Polimorfismo
Crea clases: Guitarra, Piano, y Trompeta, cada una con un método tocar() que describa la información técnica del instrumento.'''
# Clase Guitarra
class Guitarra:
    def __init__(self, nombre, color,cuerdas):
        self.nombre = nombre 
        self.color = color
        self.cuerdas = cuerdas
        self.tocar = input("Que cantidad de musica sabes tocar con la guitarra(escribe el numero): ")
        print("--------------------------------------------------")

    def descripcion(self):
        print(f"Nombre del instrumento: {self.nombre}")
        print(f"Color: {self.color}")
        print(f"Cuerdas: {self.cuerdas}")
        print(f"Manejas: {self.tocar} musicas")
        print(f"si su puntaje fue de 7 musicas, usted puede tocar o sabe tocar,mientras debe practicar un poco mas")
        print("--------------------------------------------------")
        
# Clase Piano
class Piano:
    def __init__(self, nombre, color,material):
        self.nombre = nombre 
        self.color = color
        self.material = material
        self.tocar = input("Que cantidad de musica sabes tocar con el piano(escribe el numero): ")
        print("--------------------------------------------------")

    def descripcion(self):
        print(f"Nombre del instrumento: {self.nombre}")
        print(f"Color: {self.color}")
        print(f"Material del piano: {self.material}")
        print(f"Manejas: {self.tocar} musicas")
        print(f"si su puntaje fue de 7 musicas, usted puede tocar o sabe tocar,mientras debe practicar un poco mas")
        print("--------------------------------------------------")

# Clase Trompeta
class Trompeta:
    def __init__(self, nombre, color,modelo):
        self.nombre = nombre 
        self.color = color
        self.modelo = modelo
        self.tocar = input("Que cantidad de musica sabes tocar con la trompeta(escribe el numero): ")
        print("--------------------------------------------------")

    def descripcion(self):
        print(f"Nombre del instrumento: {self.nombre}")
        print(f"Color: {self.color}")
        print(f"Modelo de la trompeta: {self.modelo}")
        print(f"Manejas: {self.tocar} musicas")
        print(f"si su puntaje fue de 7 musicas, usted puede tocar o sabe tocar,mientras debe practicar un poco mas")
        print("--------------------------------------------------")

# Función que muestra la descripción de cualquier tipo de animal
def mostrar_descripcion(instrumento):
    instrumento.descripcion()

# Instancias de cada clase
guitarra = Guitarra("Guitarra", "Marron", "12 cuerdas")
piano = Piano("Piano", "Negro", "Roble")
trompeta = Trompeta("Trompeta", "Gris", "piccolo")

# Llamado al método descripcion para cada objeto
mostrar_descripcion(guitarra)
mostrar_descripcion(piano)
mostrar_descripcion(trompeta)
