class Persona():
    nombre = None
    edad = None

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, persona):
        pareja = Pareja(self, persona)
        return pareja


class Pareja:
    relacion = []

    def __init__(self, persona1, persona2):
        self.relacion.append(persona1)
        self.relacion.append(persona2)

    def mostrar(self):
        for persona in self.relacion:
            print(persona.nombre)

    def __add__(self, persona):
        familia = Familia()
        familia.añadir_miembro(persona)
        familia.añadir_miembro(self.relacion[0])
        familia.añadir_miembro(self.relacion[1])
        return familia


class Familia:
    miembros = []

    def mostrar(self):
        for persona in self.miembros:
            print(persona.nombre)

    def añadir_miembro(self, persona):
        self.miembros.append(persona)


persona1 = Persona("Manu", 25)
persona2 = Persona("David", 28)
persona3 = Persona("Jorge", 22)

pareja = persona1 + persona2
# pareja.mostrar()

familia = pareja + persona3
familia.mostrar()
