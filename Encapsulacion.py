from random import randint


class CuentaBancaria:
    #Propiedades
    __numero_cuenta = ""
    __saldo = 0
    titular = ""

    #Constructor
    def __init__(self, titular):
        self.__generar_numero_cuenta()
        self.titular = titular

    #Get / Set
    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @property
    def saldo(self):
        return self.__saldo

        
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    #Metodos
    def __generar_numero_cuenta(self):
        self.__numero_cuenta = randint(0, 9999999999999)

    
    def añadir_saldo(self, dinero):
        if dinero > 0 :
            self.__saldo += dinero

    def sacar_dinero(self, dinero):
        if dinero > 0:
            self.__saldo -= dinero


mi_cuenta = CuentaBancaria("Pablo")
print(mi_cuenta.numero_cuenta)
print(mi_cuenta.saldo)
mi_cuenta.saldo = 500
print(mi_cuenta.saldo)


