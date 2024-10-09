class Electronico: 
    # Constructor
    def __init__(self, marca, modelo, tipo_procesador): 
        self.marca = marca 
        self.modelo = modelo
        self.tipo_procesador = tipo_procesador
        self.memoria_ram = int(input("Cantidad de memoria RAM en gb:")) 
        
    # Método público
    def registrar(self): 
        print("-----------------------") 
        print("ELECTRONICO REGISTRADO") 
        print("-----------------------") 
        print("Marca: ", self.marca) 
        print("Modelo: ", self.modelo) 
        print("Tipo De Procesador: ", self.tipo_procesador) 
        print("Cantidad de memoria RAM en gb:", self.memoria_ram) 
            
class Laptop(Electronico): 
    # Constructor de la subclase
    def __init__(self, marca, modelo, tipo_procesador,tipo_discoduro):
        # Llamada al constructor de la superclase
        super().__init__(marca, modelo, tipo_procesador)  
        self.tipo_discoduro = tipo_discoduro # atributo privado 
        self.duracion_bateria = input("Duracion de bateria en horas: ")
        self.nivel_bateria = int(input("Nivel de bateria: "))
        
    # Método privado
    def encender(self): 
        print("Tipo de disco duro: ", self.tipo_discoduro)  # imprimiendo el sistema 
        
        if self.nivel_bateria > 0:  
            print("...........") 
            print(f"El laptop {self.marca}, con modelo {self.modelo} tipo de procesador {self.tipo_procesador} enciende !!") 
        else: 
             print("-----------------") 
             print(f"El laptop {self.marca}, con modelo {self.modelo} tipo de procesador {self.tipo_procesador} no enciende !!")  
             
# Instanciando la subclase Refrigerador
objecto_laptop = Laptop("Samsung", "Galaxi", "Raince", "solido") 
objecto_laptop.registrar()  # Registrando el refrigerador 
objecto_laptop.encender()  # Ajustando la temperatura del refrigerador 