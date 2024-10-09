''' Crea tres clases: Carro, Moto y Bicicleta, cada una con un método descripcion() 
    que describa el tipo de vehículo y una función para mostrar el polimorfismo mostrar_descripcion() '''
# Clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = input("En que año la compraste: ")
        self.region = input("En que region la compraste: ")
        print("--------------------------------------------------")

    def descripcion(self):
        print("Este es un vehiculo.")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.placa}")
        print(f"El vehiculo fue comprado en el año: {self.ano} de la Region de: {self.region}")
        print("--------------------------------------------------")


# Clase Carro
class Carro:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def descripcion(self):
        print("Este es un carro.")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print("--------------------------------------------------")

# Clase Moto
class Moto:
    def __init__(self, marca, modelo, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada

    def descripcion(self):
        print("Esta es una moto.")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cilindrada: {self.cilindrada}cc")
        print("--------------------------------------------------")

# Clase Bicicleta
class Bicicleta:
    def __init__(self, marca, tipo, velocidad):
        self.marca = marca
        self.tipo = tipo
        self.velocidad = velocidad

    def descripcion(self):
        print("Esta es una bicicleta.")
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Velocidades: {self.velocidad}")
        print("--------------------------------------------------")

# Función que muestra la descripción de cualquier tipo de vehículo
def mostrar_descripcion(vehiculo):
    vehiculo.descripcion()

# Instancias de cada clase
objeto_vehiculo = Vehiculo("lamborhini", "Rax", "XL213")
objeto_carro = Carro("Toyota", "Corolla", "Rojo")
objeto_moto = Moto("Yamaha", "YZF-R3", 321)
objeto_bicicleta = Bicicleta("Giant", "Montaña", 21)

# Llamado al método descripcion para cada objeto
mostrar_descripcion(objeto_carro)
mostrar_descripcion(objeto_moto)
mostrar_descripcion(objeto_bicicleta)
mostrar_descripcion(objeto_vehiculo)
