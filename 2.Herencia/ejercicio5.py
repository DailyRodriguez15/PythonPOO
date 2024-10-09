class Reloj: 
    # Constructor
    def __init__(self, marca, tipo, material): 
        self.marca = marca 
        self.tipo = tipo
        self.material = material
        self.precio = float(input("Precio del reloj:")) 
        
    # Método público
    def registrar(self): 
        print("-----------------------") 
        print("RELOJ REGISTRADO") 
        print("-----------------------") 
        print("Marca: ", self.marca) 
        print("Tipo: ", self.tipo) 
        print("Material: ", self.material) 
        print("Precio del reloj:", self.precio) 
            
class RelojInteligente(Reloj): 
    # Constructor de la subclase
    def __init__(self, marca, tipo, material,tipo_pantalla):
        # Llamada al constructor de la superclase
        super().__init__(marca, tipo, material)  
        self.tipo_pantalla = tipo_pantalla # atributo privado 
        self.sistema_operativo = input("Sistema operativo del reloj: ")
        self.bateria = int(input("Bateria del reloj: "))
        
    # Método privado
    def encender(self): 
        print("Tipo de pantalla: ", self.tipo_pantalla)  # imprimiendo el tipo de pantalla 
        
        if self.bateria > 0:  
            print("...........") 
            print(f"El Reloj inteligente {self.marca}, con tipo {self.tipo} material {self.material} enciende !!") 
        else: 
             print("-----------------") 
             print(f"El Reloj inteligente {self.marca}, con tipo {self.tipo} material {self.material} no enciende !!")  
             
# Instanciando la subclase Refrigerador
objecto_relojInteligente = RelojInteligente("Samsung", "Galaxi", "plastico", "solido") 
objecto_relojInteligente.registrar()  # Registrando el refrigerador 
objecto_relojInteligente.encender()  # Ajustando la temperatura del refrigerador 