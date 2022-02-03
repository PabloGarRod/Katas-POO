from mailbox import NoSuchMailboxError
from tkinter import N


class Animal:
    especie = None
    altura = None
    peso = None

    def __init__(self, especie, altura, peso):
        self.especie = especie
        self.altura = altura
        self.peso = peso

    def comer(self):
        print("Estoy comiendo")

    def cazar(self):
        print("Voy a cazar")

    def dormir(self):
        print("Voy a dormir")

class Leon(Animal):

    def __init__(self, altura, peso):
        super().__init__("LEON", altura, peso)

class Mascota():
    nombre = None
    amo = None

    def __init__(self, nombre, amo):
        self.nombre = nombre
        self.amo = amo
    

    def sentarse(self):
        print("Estoy sentado")

    def dar_la_pata(self):
        print("Te doy la pata")

class Perro(Animal, Mascota):

    def __init__(self, nombre, amo, altura, peso):
        Mascota.__init__(self, nombre, amo)
        Animal.__init__(self, "PERRO", altura, peso)

kali = Perro("Kali", "Juan", 0.5, 25)
kali.cazar()
kali.dormir()
kali.sentarse()
print(kali.nombre)
print(kali.especie) 
print(kali.amo)
