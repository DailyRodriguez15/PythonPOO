#Defino la clase
class Celular:
    #Metodo constructor
    def __init__(self, nombre, marca ,imei ,bateria ,camara):
        #Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.marca = marca
        self.imei = imei
        self.bateria = bateria
        self.camara = camara
        
#Metodos para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion del celular")
        print("Nombre: "+self.nombre)
        print("Marca: "+self.marca) 
        print("Imei: "+self.imei)
        print("Bateria: "+self.bateria)
        print("Camara: "+self.camara)
        print("--------------------------------")
        
#Metodo para enceder el celular
    def encender(self): 
       energia = int(input("Digite el valor de la carga: "))
       if energia > 0:
        print("El celular: " + self.nombre + " se puede encender")
        print(f"|||||||||{energia} % de carga")
        print("----------------------------------------------")
       else:
        print("El celular: " +self.nombre+ " no se puede encender")  
        print("--------------------------------")  
    
            
#Creamos los objetos a partir de instanciar la clase celular        
celular1 = Celular("samsung","galaxy 521", "36578", "400mAh","64mp")
celular2 = Celular("phone","apple", "3567811", "3095mAh","12mp")
celular3 = Celular("xiomi","mi 11", "344576", "4600mAh","108mp")

#Mostrar los detalles de cada objeto
celular1.mostrar_detalles()
celular1.encender()
celular2.mostrar_detalles()
celular2.encender()
celular3.mostrar_detalles()
celular3.encender()



        
    