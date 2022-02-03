class Persona():
    name = None

    def __init__(self, name):
        self.name = name

    def __add__(self, persona):
        familia = Familia(self, persona)
        return familia

    def __sub__(self, persona):
        if self == persona:
            return None

    def __str__(self):
        return self.name


class Familia:
    members = []

    def __init__(self, persona1, persona2):
        self.members.append(persona1)
        self.members.append(persona2)

    def __add__(self, persona):
        self.members.append(persona)
        return self

    def __sub__(self, persona):
        self.members.remove(persona)
        if len(self.members) == 1:
            return self.members[0]
        elif len(self.members) == 0:
            return None
        else:
            return self

    def show(self):
        for people in self.members:
            print(people.name)


p1 = Persona("Juan")
p2 = Persona("Sara")
p3 = Persona("Ibai")
p4 = Persona("Raul")

familia1 = p1 + p2 + p3
familia1.show()
familia1 = familia1 - p1 -p2
print("La resta de de la familia es:")
print(familia1.name)
print(familia1-p3)
