"""Crea una clase abstracta Empleado con un método abstracto calcular_salario(). Luego, crea dos clases concretas EmpleadoTiempoCompleto y EmpleadoPorHoras que implementen calcular_salario() de manera distinta."""

from abc import ABC, abstractmethod

class TareaEmpleado(ABC):
    @abstractmethod
    def __init__(self, nombre):
        self.nombre = nombre
    
    def realizar_tarea(self):
        pass

class Ingeniero(TareaEmpleado):
    def __init__(self, nombre, tarea):
        self.nombre = nombre
        self.tarea = tarea

    def realizar_tarea(self):
        return f"{self.nombre} esta realizando una tarea de {self.tarea} como ingeniero"

class Doctor(TareaEmpleado):
    def __init__(self, nombre, tarea):
        self.nombre = nombre
        self.tarea = tarea

    def realizar_tarea(self):
        return f"{self.nombre} esta realizando una tarea de {self.tarea} como doctor"

# Uso de las clases
ingeniero = Ingeniero("Angel", "construyen y mantienen sistemas")
print(ingeniero.realizar_tarea())
doctor = Doctor("Miguel", "diagnostica, trata y ayuda a prevenir dolencias")
print(doctor.realizar_tarea())
