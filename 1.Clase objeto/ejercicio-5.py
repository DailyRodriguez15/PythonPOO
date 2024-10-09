#Defino la clase
class Figuras:
    #Metodo constructor
    def __init__(self, nombre, numero ,area ,perimetro):
        #Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.numero = numero
        self.area = area
        self.perimetro = perimetro
        
#Metodos para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion de las figuras")
        print("Nombre: "+self.nombre)
        print("Numero: "+self.numero) 
        print("Area: "+self.area)
        print("Perimetro: "+self.perimetro)
        print("--------------------------------")
        
 # Método para calcular el perímetro de un cuadrado
    def calcular_perimetro(self): 
        if self.nombre.lower() == "cuadrado":
            lado = float(input("Digite la longitud de un lado del cuadrado: "))
            if lado > 0:
                self.perimetro = 4 * lado
                print(f"El perímetro del {self.nombre} es {self.perimetro} unidades.")
                print("----------------------------------------------")
            else:
                print("El valor ingresado no es válido.")
        else:
            print(f"El cálculo del perímetro no está implementado para {self.nombre}.")
           
    
            
#Creamos los objetos a partir de instanciar la clase celular        
figura1 = Figuras("cuadrado","4", "25(5 cada lado)", "20 unidades")
figura2 = Figuras("triangulo","3", "18.8(6 cada lado)", "18 unidades")
figura3 =Figuras("circulo","0", "78.5(5 cada lado)", "31.4")

#Mostrar los detalles de cada objeto
figura1.mostrar_detalles()
figura1.calcular_perimetro()
figura2.mostrar_detalles()
figura2.calcular_perimetro()
figura3.mostrar_detalles()
figura3.calcular_perimetro()




        
    