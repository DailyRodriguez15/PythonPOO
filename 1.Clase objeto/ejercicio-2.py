#Defino la clase
class Animal:
    #Metodo constructor
    def __init__(self, nombre, especie ,edad ,peso ,color):
        #Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso
        self.color = color
        
#Metodos para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion del animal")
        print("Nombre: "+self.nombre)
        print("Especie: "+self.especie) 
        print("Edad: "+self.edad)
        print("Peso: "+self.peso)
        print("Color: "+self.color)
        print("--------------------------------")
        
#Metodo para enceder el celular
    def comer(self): 
       comida = int(input("Digite cuantas horas lleva el animal sin comer: "))
       if comida > 4:
        print("El animal: " + self.nombre + " tiene que comer")
        print(f"|||||||||cada 4 horas se le debe dar la comida al animal")
        print("----------------------------------------------")
       else:
        print("El animal: " +self.nombre+ " no puede comer")
        print(f"|||||||||despues de 4 horas podra comer") 
        print("--------------------------------")    
    
            
#Creamos los objetos a partir de instanciar la clase celular        
animal1 = Animal("max","perro", "5 años", "25kg","marron con blanco")
animal2 = Animal("luna","gata", "3 años", "4kg","gris")
animal3 = Animal("kiwi","canario", "2 años", "30g","amarillo")

#Mostrar los detalles de cada objeto
animal1.mostrar_detalles()
animal1.comer()
animal2.mostrar_detalles()
animal2.comer()
animal3.mostrar_detalles()
animal3.comer()



        
    