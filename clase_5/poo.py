# Clase
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    def hablar(self, sonido):
        print(sonido)
    


class Perro(Animal):
     # Atributos de clase == variable global
    especie = "mamiferos"

    def __init__(self, nombre, raza, especie, edad):
        # Atributos de instancia == variables locales
        self.nombre = nombre
        self.raza = raza

        super().__init__(especie, edad)

      # Metodos
    # def jugar(self, objeto):
    #     print("El perro esta jugando con ", objeto)

    def saludar(self):
        print(f'{self.nombre} dio la pata')

class Gato(Animal):
     # Atributos de clase == variable global
    especie = "mamiferos"

    def __init__(self, nombre, raza, especie, edad):
        # Atributos de instancia == variables locales
        self.nombre = nombre
        self.raza = raza

        super().__init__(especie, edad)

      # Metodos
    # def jugar(self, objeto):
    #     print("El perro esta jugando con ", objeto)

    def saludar(self):
        print(f'{self.nombre} ronronea')


perro1 = Perro("Firulais", "Salchicha", "Perro", 5)
print(f'Perro1 -> {perro1.nombre}, {perro1.raza}, {perro1.especie}')
perro1.saludar()

gato1 = Gato("Tito", "Calico", "Felino", 3)
print(f'Gato1 -> {gato1.nombre}, {gato1.raza}, {gato1.especie}, {gato1.edad}')
gato1.saludar()

# PRACTICANDO
# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad

# class Alumno(Persona):
#     def __init__(self, carrera, cursando, nombre, apellido, edad):
#         self.carrera = carrera
#         self.cursando = cursando

#         super().__init__(nombre, apellido, edad)

#     def enClase(self):
#             if(cursando == True):
#                 print(f'El alumno {self.nombre} esta cursando actualmente')
#             else:
#                 print(f'El alumno {self.nombre} no esta cursando actualmente')
    


# alumno1 = Alumno("Medicina", True, "Juan", "Medina", 22)
# print(f'Alumno1: {alumno1.nombre}, {alumno1.apellido}, {alumno1.carrera}, {alumno1.cursando}')






