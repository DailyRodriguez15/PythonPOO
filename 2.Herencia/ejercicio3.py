class Instrumento:
    # Constructor
    def __init__(self, tipo, marca, material):
        self.tipo = tipo
        self.marca = marca
        self.material = material
        self.precio = float(input("Precio del Instrumento: "))

    # Método público
    def registrar(self):
        print("-----------------------")
        print("INSTRUMENTO REGISTRADO")
        print("-----------------------")
        print("Tipo: ", self.tipo)
        print("Marca: ", self.marca)
        print("Material: ", self.material)
        print("Precio: ", self.precio)

class Guitarra(Instrumento):
    # Constructor de la subclase
    def __init__(self, tipo, marca, material, numero_de_cuerdas):
        # Llamada al constructor de la superclase
        super().__init__(tipo, marca, material)
        self.numero_de_cuerdas = numero_de_cuerdas
        self.acordes_basicos = input("¿Qué acordes básicos conoces? (separados por comas): ")

    # Método para mostrar información y evaluar los acordes conocidos
    def conocimiento(self):
        # Imprimir el número de cuerdas
        print("Número de cuerdas: ", self.numero_de_cuerdas)
        
        # Procesar los acordes básicos
        acordes = [acorde.strip() for acorde in self.acordes_basicos.split(",")]

        # Evaluar el número de acordes conocidos
        if len(acordes) > 5:
            print("¡Excelente! Conoces una gran cantidad de acordes.")
        else:
            print("Sigue practicando para aprender más acordes, despues de 5 minimo tocaras la guitarra.")
        
        # Mostrar los acordes conocidos
        print("Acordes conocidos: ", ", ".join(acordes))

# Instanciando la subclase Guitarra
objecto_guitarra = Guitarra("acústica", "Fender", "spruce", 6)
objecto_guitarra.registrar()  # Registrando la guitarra
objecto_guitarra.conocimiento()  # Evaluando y mostrando los acordes conocidos
