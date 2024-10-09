class Dispositivo: 
    # Constructor
    def __init__(self, marca, modelo, año): 
        self.marca = marca 
        self.modelo = modelo
        self.año = año
        self.capacidad_bateria = int(input("Capacidad de la bateria en mAh:")) 
        
    # Método público
    def registrar(self): 
        print("-----------------------") 
        print("DISPOSITIVO REGISTRADO") 
        print("-----------------------") 
        print("Marca: ", self.marca) 
        print("Modelo: ", self.modelo) 
        print("Año: ", self.año) 
        print("Capacidad de la bateria en mAh:", self.capacidad_bateria) 
            
class Smartphone(Dispositivo): 
    # Constructor de la subclase
    def __init__(self, marca, modelo, año, sistema):
        # Llamada al constructor de la superclase
        super().__init__(marca, modelo, año)  
        self.sistema = sistema # atributo privado 
        self.tipo_conectividad = input("Tipo de conectividad: ")
        self.energia = int(input("Cantidad de la bateria: "))
        
    # Método privado
    def encender(self): 
        print("Sistema: ", self.sistema)  # imprimiendo el sistema 
        
        if self.energia > 0:  
            print("...........") 
            print(f"El smartphone {self.marca}, con modelo {self.modelo} año {self.año} enciende !!") 
        else: 
             print("-----------------") 
             print(f"El smartphone {self.marca}, con modelo {self.modelo} y año {self.año} no enciende !!")  
             
# Instanciando la subclase Refrigerador
objecto_smartphone = Smartphone("Samsung", "Galaxi", "2023", "Android") 
objecto_smartphone.registrar()  # Registrando el refrigerador 
objecto_smartphone.encender()  # Ajustando la temperatura del refrigerador 