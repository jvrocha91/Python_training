class Conta():
    def __init__(self, id_conta, saldo=0):
        self.id_conta = id_conta
        self.saldo = saldo

    def depositar(self):
        deposito=int(input("Valor a depositar:"))
        self.saldo+=deposito

    def sacar(self):
        saque=int(input("Valor a sacar:"))
        self.saldo-=saque

    def mostrar_saldo(self):
        print(f"Saldo atual:{self.saldo}")
