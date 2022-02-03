class Alumno:
    nombre = ""
    apellidos = ""
    dni = ""
    edad = 0
    nota = 0

    def __init__(self, nombre, apellidos, dni, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre}")

    def cumpleaños(self):
        self.edad += 1

    def añadir(self, nota):
        if 0 <= nota <= 10:
            self.nota = nota


class Asignatura:
    nombre = ""
    nota = ""

    def añadir_nota(self, nota):
        pass

