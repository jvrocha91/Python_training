from banco import Conta

class Cliente():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.conta = None

    def criar_conta(self):
        print("Criar nova conta:\n")
        id_conta = int(input("Escolha um id para a conta:\n"))
        self.conta = Conta(id_conta)
        print("Conta criada com sucesso!")

    def mostrar_info(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}")
        if self.conta:
            print(f"ID da Conta: {self.conta.id_conta}\nSaldo: R${self.conta.saldo}")
