'''  Clases de Profesiones con Polimorfismo
Crea tres clases: Médico, Ingeniero, y Docente, cada una con un método trabajar() que describa la información técnica del profesional.'''
# Clase Guitarra
class Medico:  
    def __init__(self, profesion, nombre,edad):
        self.profesion = profesion 
        self.nombre = nombre
        self.edad = edad
        self.trabajar = input("Hace cuantas horas no ingresa a trabajr(escribe el numero de horas): ")
        print("--------------------------------------------------")

    def descripcion(self):
        print(f"Profesion: {self.profesion}")
        print(f"Nombre del medico: {self.nombre}")
        print(f"Edad del medico: {self.edad}")
        print(f"Horas sin trabajar: {self.trabajar} horas")
        print(f"si usted no ha ingresado a trabajar despues de 8 horas,usted debe de ir a trabajar!! de lo contrario no.")
        print("--------------------------------------------------")
        
# Clase Piano
class Ingeniero:
    def __init__(self, profesion, nombre,sexo):
        self.profesion = profesion 
        self.nombre = nombre
        self.sexo = sexo
        self.trabajar = input("Hace cuantas horas no ingresa a trabajr(escribe el numero de horas): ")
        print("--------------------------------------------------")

    def descripcion(self):
        print(f"Profesion: {self.profesion}")
        print(f"Nombre del ingeniero: {self.nombre}")
        print(f"Sexo del ingeniero: {self.sexo}")
        print(f"Horas sin trabajar: {self.trabajar} horas")
        print(f"si usted no ha ingresado a trabajar despues de 8 horas,usted debe de ir a trabajar!! de lo contrario no.")
        print("--------------------------------------------------")

# Clase Trompeta
class Docente:
    def __init__(self, profesion, nombre,documento):
        self.profesion = profesion 
        self.nombre = nombre
        self.documento = documento
        self.trabajar = input("Hace cuantas horas no ingresa a trabajr(escribe el numero de horas): ")
        print("--------------------------------------------------")

    def descripcion(self):
        print(f"Profesion: {self.profesion}")
        print(f"Nombre del docente: {self.nombre}")
        print(f"Documento de indentidad de el docente: {self.documento}")
        print(f"Horas sin trabajar: {self.trabajar} horas")
        print(f"si usted no ha ingresado a trabajar despues de 8 horas,usted debe de ir a trabajar!! de lo contrario no.")
        print("--------------------------------------------------")

# Función que muestra la descripción de cualquier tipo de animal
def mostrar_descripcion(instrumento):
    instrumento.descripcion()

# Instancias de cada clase
medico = Medico("Medico", "Carlos", 38)
ingeniero = Ingeniero("Ingeniero", "Julian", "Masculino")
docente = Docente("Docente", "Marcos", 11028945829)

# Llamado al método descripcion para cada objeto
mostrar_descripcion(medico)
mostrar_descripcion(ingeniero)
mostrar_descripcion(docente)