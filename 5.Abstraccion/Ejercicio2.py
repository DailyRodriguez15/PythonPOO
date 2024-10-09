"""Crea una clase abstracta Empleado con un método abstracto calcular_salario(). Luego, crea dos clases concretas EmpleadoTiempoCompleto y EmpleadoPorHoras que implementen calcular_salario() de manera distinta."""

from abc import ABC, abstractmethod
import math

class Empleado(ABC):
    @abstractmethod
    def __init__(self, nombre):
        self.nombre = nombre
    
    def calcular_salario(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_mensual):
        self.nombre = nombre
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora

# Uso de las clases
empleado_tiempo_completo = EmpleadoTiempoCompleto("Sara", 4500)
print(f"Salario de {empleado_tiempo_completo.nombre}: {empleado_tiempo_completo.calcular_salario()}")

empleado_por_horas = EmpleadoPorHoras("Luis", 125, 11)
print(f"Salario de {empleado_por_horas.nombre}: {empleado_por_horas.calcular_salario()}")