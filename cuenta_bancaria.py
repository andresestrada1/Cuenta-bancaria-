class CuentaBancaria:

    def __init__(self, balance,tasa_interes = 0.01,):
        self.tasa_interes = tasa_interes
        self.balance = balance

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if amount > self.balance:
            print("La cuenta no dispone de esa cantidad")
        else:
            self.balance -= amount
        return self

    def informacion_de_retiro(self):   
        saldo = self.balance
        if self.balance != saldo:
            print("Se realizo un retiro")
        return self

    def mostrar_info_cuenta(self):
        print(f"La cuenta dispone de {self.balance}")
        return self

    def generar_interés(self):
        if self.balance > 0:
            self.balance += self.balance *self.tasa_interes
        return self

    def informacion_general_de_cuenta(self):
        print(f"La cuenta tiene un balance {self.balance} y unos intereses del {self.tasa_interes}")
        return self