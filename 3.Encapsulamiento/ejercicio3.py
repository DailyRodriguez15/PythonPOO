#Clase Personas con atributos encapsulados o privados
class Libros:
    #metodo constructor
    def __init__(self,titulo,autor,isbn,categoria):
        self.__titulo=titulo #privado
        self.__autor=autor #privado
        self.__isbn=isbn #privado
        self.editorial=categoria#público

    #metodo getter
    def obtener_titulo(self):
        return self.__titulo
    
    #metodo getter
    def obtener_autor(self):
        return self.__autor
    
    #metodo getter
    def obtener_isbn(self):
        return self.__isbn
    
    #metodo setter
    def establecer_titulo(self, nuevo_titulo):
        self.__titulo=nuevo_titulo

    #metodo setter
    def establecer_autor(self, nuevo_autor):
        self.__autor=nuevo_autor
        
    #metodo setter
    def establecer_isbn(self, nuevo_isbn):
        self.__isbn=nuevo_isbn
    
    #metodo mostrar detalles del objeto
    def mostrar_detalles(self):
        print(f"Titulo: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Isbn: {self.__isbn}")
        print(f"Editorial: {self.editorial}")

#objeto
libro=Libros("La piragua","Davenci",345,"lenin")

#imprimir atributos publicos y privados
libro.mostrar_detalles()

print("---------------------------")

#imprimir el atributo encapsulado modificando su acceso con getter y setter
libro.establecer_titulo("El paraiso") #setter
print(f"Titulo: { libro.obtener_titulo() }") #getter
libro.establecer_autor("Omar") #setter
print(f"Autor: { libro.obtener_autor() }") #getter
libro.establecer_isbn(960) #setter
print(f"Isbn: { libro.obtener_isbn() }") #getter
print(f"Editorial: { libro.editorial }") #público

