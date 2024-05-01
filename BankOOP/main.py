from cliente import Cliente
from banco import Conta

def main():
    print("Bem vindo ao banco OOP:\n")
    user = None  # Inicializa o usuário como None
    while True:
        menu = int(input("\n'1' para acessar conta, '2' para criar conta, '3' para sair:\n"))
        if menu == 2:
            nome = input("Digite seu nome: ")
            idade = int(input("Digite sua idade: "))
              # Supondo que o usuário escolha o ID da conta
            user = Cliente(nome, idade)
            user.criar_conta()
        elif menu == 1:
            if user and user.conta:
                menu_user = int(input("'1' para mostrar informações da conta, '2' para depósito, '3' para saque, '4' para mostrar saldo: "))
                if menu_user == 1:
                    user.mostrar_info()
                elif menu_user == 2:
                    user.conta.depositar()
                elif menu_user == 3:
                    user.conta.sacar()
                elif menu_user == 4:
                    user.conta.mostrar_saldo()
            else:
                print("Você ainda não criou sua conta")
        elif menu == 3:
            print("Obrigado por usar o banco OOP.")
            break
        else:
            print("Opção inválida")

main()
