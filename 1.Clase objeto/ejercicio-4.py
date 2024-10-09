#Defino la clase
class Empleado:
    #Metodo constructor
    def __init__(self, nombre, id ,puesto ,salario ,departamento):
        #Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.id = id
        self.puesto = puesto
        self.salario = salario
        self.departamento = departamento
        
#Metodos para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion del empleado")
        print("Nombre: "+self.nombre)
        print("Id: "+self.id) 
        print("Puesto: "+self.puesto)
        print("Salario: "+self.salario)
        print("Departamento: "+self.departamento)
        print("--------------------------------")
        
#Metodo para enceder el celular
    def registrarse(self): 
       registrar = input("Digite su rol (enfermera, analista, bombero): ")
       if registrar == "bombero, analista":
        print("Emplead@ : " + self.nombre + " tiene horario de 7:00AM y finaliza a las 11:00PM")
        print("----------------------------------------------")
       else:
        print("Emplead@: " +self.nombre+ " tiene horario de 6:00Am y finaliza a las 1:00AM") 
        print("--------------------------------")     
           
    
            
#Creamos los objetos a partir de instanciar la clase celular        
empleado1 = Empleado("carlos","EMp5658", "analisista", "3,000","tecnologia de la informacion")
empleado2 = Empleado("luis","EMp12245", "bombero", "2,200","recursos humanos")
empleado3 = Empleado("laura","EMp6789", "enfermera", "5,500","centro de la salud y vida")

#Mostrar los detalles de cada objeto
empleado1.mostrar_detalles()
empleado1.registrarse()
empleado2.mostrar_detalles()
empleado2.registrarse()
empleado3.mostrar_detalles()
empleado3.registrarse()




        
    