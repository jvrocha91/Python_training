from cliente import Cliente
from banco import Conta

def main():
    print("Bem vindo ao banco OOP:\n")
    while True:
        menu=int(input("'1' para acesar conta,'2' para criar conta:"))
        if menu == 2 :
            nome = input("Digite seu nome:")
            idade = int(input("Digite sua idade:"))
            user = Cliente(nome, idade)
            user.criar_conta()
        elif menu == 1:
            if user:
                menu_user=int(input("'1' para mostrar informacoes da conta,'2' para deposito,'3' para saque,'4'para mostrar saldo: "))
                if menu_user == 1:
                    user.mostrar_info()
                elif menu_user == 2:
                    user.conta.depositar()
                elif menu_user == 3:
                    user.conta.sacar()
                elif menu_user == 4:
                    user.conta.mostrar_saldo()
            else:
                print("Voce ainda nao criou sua conta")
        else:
            print("Opcao invalida")

main()

