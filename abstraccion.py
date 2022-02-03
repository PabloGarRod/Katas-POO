class Calculadora:
    memoria = []

    def __init__(self, num1, num2):
        print(self.memoria)
        print(self.suma(num1, num2))
        print(self.memoria)
        print(self.resta(num1, num2))
        print(self.memoria)
        print(self.multi(num1, num2))
        print(self.memoria)
        print(self.div(num1, num2))
        print(self.memoria)

    def suma(self, num1, num2):
        resultado = num1 + num2
        self.memoria.append(resultado)
        return resultado

    def resta(self, num1, num2):
        resultado = num1 - num2
        self.memoria.append(resultado)
        return resultado

    def multi(self, num1, num2):
        resultado = num1 * num2
        self.memoria.append(resultado)
        return resultado

    def div(self, num1, num2):
        resultado = num1 / num2
        self.memoria.append(resultado)
        return resultado


cal = Calculadora(10, 5)
