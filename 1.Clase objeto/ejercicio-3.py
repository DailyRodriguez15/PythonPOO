#Defino la clase
class Carro:
    #Metodo constructor
    def __init__(self, marca ,modelo ,año ,color, kilometraje):
        #Defino los atributos de instancia de la clase
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.kilometraje = kilometraje
        
#Metodos para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion del carro")
        print("Marca: "+self.marca)
        print("Modelo: "+self.modelo) 
        print("Año: "+self.año)
        print("Color: "+self.color)
        print("Kilometraje: "+self.kilometraje)
        print("--------------------------------")
        
#Metodo para enceder el celular
    def encender(self): 
       gasolina = float(input("Digite la cantidad de su tanque combustible: "))
       if gasolina > 1:
        print("El carro " + self.marca + " si se puede encender")
        print(f"|||||||||{gasolina} % de gasolina")
        print("----------------------------------------------")
       else:
        print("El carro " +self.marca+ " no se puede encender")
        print(f"|||||||||{gasolina} % digite gasolina")
        print("--------------------------------")      
    
            
#Creamos los objetos a partir de instanciar la clase celular        
carro1 = Carro("toyota","corolla", "2022", "rojo","30,000km")
carro2 = Carro("ford","mustang", "2021", "azul","15,000km")
carro3 = Carro("tesla","model s", "2023", "negro","10,000km")

#Mostrar los detalles de cada objeto
carro1.mostrar_detalles()
carro1.encender()
carro2.mostrar_detalles()
carro2.encender()
carro3.mostrar_detalles()
carro3.encender()



        
    