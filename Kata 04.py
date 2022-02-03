class Alumno:
    nombre = ""
    apellidos = ""
    __dni = ""
    __edad = 0
    asignaturas = []

    def __init__(self, nombre, apellidos, dni, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__dni = dni
        self.__edad = edad

    #Get / Set
    @property
    def dni(self):
        return self.__dni

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if 0 < edad < 100 :
            self.__edad = edad
        else:
            raise TypeError ("Edad fuera del rango")

    #Metodos
    def saludar(self):
        print("Hola, me llamo " + self.nombre)

    def cumpleaños(self):
        self.__edad += 1

    def añadir_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)


class Asignatura:
    __id = 0
    nombre = ""
    __nota = 0

    def __init__(self, nombre):
        self.nombre = nombre
    
    #Get / Set
    @property
    def nota(self):
        return self.__nota
    
    @property
    def id(self):
        return self.__id

    
    #Metodos
    def añadir_nota(self, nota):
        if 0 <= nota <= 10:
            self._nota = nota


class Aula:
    
    __id = 0
    profesor = None
    alumnos = []
    asignaturas = []

    def __init__(self, alumnos, asignaturas):
        self.__cargar_alumnos(alumnos)
        self.__cargar_asignaturas(asignaturas)

    #Get / Set
    @property
    def id(self):
        return self.__id

    #Metodos
    def mostrar(self):
        for alumno in self.alumnos:
            print(alumno.nombre)
        for asignatura in self.asignaturas:
            print(asignatura.nombre)

    def __cargar_asignaturas(self, asignaturas):
        for nombre in asignaturas:
            nueva_asignatura = Asignatura(nombre)
            self.añadir_asignatura(nueva_asignatura)

    def __cargar_alumnos(self, alumnos):
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


manu = Alumno("Manu", "Garcia", 50211333, 32)
print(manu.dni)
print(manu.edad)
#manu.dni = 0000000
manu.edad = 50
print(manu.edad)
manu.edad = 101
print(manu.edad)
