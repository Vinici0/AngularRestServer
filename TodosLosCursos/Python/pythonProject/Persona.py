class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"¡Hola! Mi nombre es {self.nombre} y tengo {self.edad} años.")

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def presentarse(self):
        super().presentarse()
        print(f"Soy un empleado y mi salario es {self.salario}.")