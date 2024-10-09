#Defino la clase
class Moto:
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
        print("Informacion del la moto")
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
moto1 = Moto("yamaha","mt-07", "2021", "negra","12,000km")
moto2 = Moto("ducati","muster 821", "2020", "azul","5,000km")
moto3 = Moto("honja","pex 125", "2022", "blanco","8,000km")

#Mostrar los detalles de cada objeto
moto1.mostrar_detalles()
moto1.encender()
moto2.mostrar_detalles()
moto2.encender()
moto3.mostrar_detalles()
moto3.encender()



        
    