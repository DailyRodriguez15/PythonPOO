#Clase Personas con atributos encapsulados o privados
class Productos:
    #metodo constructor
    def __init__(self,nombre,precio,cantidad,categoria):
        self.__nombre=nombre #privado
        self.__precio=precio #privado
        self.cantidad=cantidad #publico
        self.categoria=categoria#público

    #metodo getter
    def obtener_nombre(self):
        return self.__nombre
    
    #metodo getter
    def obtener_precio(self):
        return self.__precio
    
    #metodo setter
    def establecer_nombre(self, nuevo_nombre):
        self.__nombre=nuevo_nombre

    #metodo setter
    def establecer_precio(self, nuevo_precio):
        self.__precio=nuevo_precio
    
    #metodo mostrar detalles del objeto
    def mostrar_detalles(self):
        print(f"\nNombre: {self.__nombre}")
        print(f"Precio: {self.__precio}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Categoria: {self.categoria}")

#objeto
producto=Productos("Jorge",152000,21,"lex")

#imprimir atributos publicos y privados
producto.mostrar_detalles()

print("---------------------------")

#imprimir el atributo encapsulado modificando su acceso con getter y setter
producto.establecer_nombre("Luiss") #setter
print(f"Nombres: { producto.obtener_nombre() }") #getter
producto.establecer_precio(826000) #setter
print(f"Precio: { producto.obtener_precio() }") #getter
print(f"Cantidad: { producto.cantidad }") #público
print(f"Categoria: { producto.categoria }") #público
