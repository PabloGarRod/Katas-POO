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
        print("Hola, me llamo " + self.nombre)

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


class Clase:
    profesor = None
    alumnos = []
    asignaturas = []

    def __init__(self, alumnos, asignaturas):
        self.cargar_alumnos(alumnos)
        self.cargar_asignaturas(asignaturas)

    def mostrar(self):
        for alumno in self.alumnos:
            print(alumno.nombre)
        for asignatura in self.asignaturas:
            print(asignatura.nombre)

    def cargar_asignaturas(self, asignaturas):
        for nombre in asignaturas:
            nueva_asignatura = Asignatura(nombre)
            self.añadir_asignatura(nueva_asignatura)

    def cargar_alumnos(self, alumnos):
        for nombre in alumnos:
            nuevo_alumno = Alumno(nombre, "", "", 18)
            self.añadir_alumnos(nuevo_alumno)

    def añadir_alumnos(self, alumno):
        if alumno.edad >= 18:
            self.alumnos.append(alumno)

    def borrar_alumnos(self, alumno):
        self.alumnos.remove(alumno)

    def añadir_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def borrar_asignatura(self, asignatura):
        self.asignaturas.remove(asignatura)


alumnos = ["Manuel", "Ana", "Jorge"]
asignaturas = ["Matematicas", "Lengua", "Sociales"]

aula = Clase(alumnos, asignaturas)
aula.mostrar()
