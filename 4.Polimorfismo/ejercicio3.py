'''  Animales con Polimorfismo
Crea tres clases: Perro, Gato, y Pájaro, cada una con un método sonido() que haga el sonido correspondiente '''
# Clase Carro
class Perro:
    def __init__(self, nombre, raza,especie):
        self.nombre = nombre 
        self.raza = raza
        self.especie = especie

    def sonido(self):
        print(f"El perro {self.nombre} hace: ¡Guau guau!")
        print(f"Raza: {self.raza}")
        print(f"Especie: {self.especie}")
        print("--------------------------------------------------")


# Clase Moto
class Gato:
    def __init__(self, nombre, raza,edad):
        self.nombre = nombre 
        self.raza = raza
        self.edad = edad

    def sonido(self):
        print(f"El gato {self.nombre} hace: ¡miau miau!")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print("--------------------------------------------------")

# Clase Bicicleta
class Pajaro:
    def __init__(self, nombre, raza,peso):
        self.nombre = nombre 
        self.raza = raza
        self.peso = peso

    def sonido(self):
        print(f"El pajaro {self.nombre} hace: ¡pio pio!")
        print(f"Raza: {self.raza}")
        print(f"Peso: {self.peso}")
        print("--------------------------------------------------")

# Función que muestra la descripción de cualquier tipo de animal
def mostrar_sonido(animal):
    animal.sonido()

# Instancias de cada clase
perro = Perro("Doki", "Labrador", "Canis")
gato = Gato("Luna", "Persa", "8 años")
pajaro = Pajaro("Kiwi", "Agoponis", 1.111)

# Llamado al método descripcion para cada objeto
mostrar_sonido(perro)
mostrar_sonido(gato)
mostrar_sonido(pajaro)
