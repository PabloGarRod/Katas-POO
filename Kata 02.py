class Alumno:
    nombre = ""
    apellidos = ""
    dni = ""
    edad = 0
    asignaturas = []

    def __init__(self, nombre, apellidos, dni, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre}")

    def cumpleaños(self):
        self.edad += 1

    def añadir_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)


class Asignatura:
    nombre = ""
    nota = 0

    def __init__(self, nombre):
        self.nombre = nombre



    def añadir_nota(self, nota):
        if 0 <= nota <= 10:
            self.nota = nota
