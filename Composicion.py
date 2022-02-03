class Jugador():
    nombre = " "
    edad = 0
    rol =""

    def __init__(self, nombre, edad, rol):
        self.nombre = nombre
        self.edad = edad
        self.rol = rol

class Equipo():
    escudo = "image.png"
    jugadores = []

    def mostrar_equipo(self):
        for jugador in self.jugadores:
            print(jugador.nombre)

    def añadir_jugador(self, jugador):
        self.jugadores.append(jugador)


j1 = Jugador("Manuel", 25, "Porteto")
j2 = Jugador("Ana", 23, "Portero")
j3 = Jugador("David", 28, "Defensa")

equipo = Equipo()
equipo.añadir_jugador(j1)
equipo.añadir_jugador(j2)
equipo.añadir_jugador(j3)


equipo.mostrar_equipo()