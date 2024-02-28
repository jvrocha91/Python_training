import os

ultimo = 1
fila = list(range(1, ultimo + 1))
Conta = 0
x = 0
soma = 0
pago = []

cardapio = {
    1: {"item": "Hamburguer", "preco": 20.0},
    2: {"item": "Batata", "preco": 10.0},
    3: {"item": "Batata com cheddar e bacon", "preco": 16.0},
    4: {"item": "Refrigerante", "preco": 8.0},
    5: {"item": "Suco natural", "preco": 7.0},
    6: {"item": "Sorvete", "preco": 11.0}
}

def exibir_menu():
    print("============================================")
    print("Bem vindo a hamburgueria Trem fantasma!")
    print("============================================")
    fantasma = """
         .-.            
        (o o) boo!
         |O|  
         | |
        '~~~'
        """
    print(fantasma)

def adicionar_cliente():
    global ultimo
    os.system('cls')
    ultimo += 1
    fila.append(ultimo)

def atender_cliente():
    global Conta, x, soma
    if len(fila) > 0:
        atendido = fila.pop(0)
        print(f"\nCliente {atendido} sendo atendido:\n")
        while True:
            exibir_cardapio()
            Cod = int(input("\nDigite um código de produto:"))
            if Cod == 0:
                break
            if Cod in cardapio:
                produto = cardapio[Cod]
                print(f"\n{produto['item']} adicionado")
                Conta += produto['preco']
                x += 1
            if not continuar_pedido():
                break
        if confirmar_pedido():
            soma += Conta
            x = 0
            print(f"\nA conta do cliente {atendido} será de {Conta} Reais")
            pago.append(f"{atendido}-{Conta}R$\n")
            Conta = 0
    else:
        print("\nFila vazia! Ninguém para atender")

def exibir_cardapio():
    print("----------------------------------")
    print("\nQual produto deseja adicionar a sua compra:\n")
    for codigo, produto in cardapio.items():
        print(f"{codigo}-{produto['item']}: {produto['preco']} R$")
    print("Digite '0' para encerrar o pedido\n")
    print("----------------------------------")

def continuar_pedido():
    Option = int(input("\nDeseja Continuar o pedido ?\n\n1-Sim\n2-Não\n"))
    return Option == 1

def confirmar_pedido():
    confirm = int(input(f"Sua compra tem {x} produto(s)\nDeseja confirmar pedido ?\n\n1-Sim\n2-Não\n"))
    return confirm == 1

def main():
    exibir_menu()
    Cadastro = int(input("Digite uma senha numérica a ser cadastrada:"))
    Acesso = int(input("\nDigite sua senha:"))
    if Acesso == Cadastro:
        os.system('cls')
        print("\nAcesso permitido")
        while True:
            print(f"\nExistem {len(fila)} clientes na fila")
            print(f"Fila atual: {fila}\n")
            print("-------------")
            print("Digite F para adicionar cliente ao fim da fila\nDigite A para realizar o atendimento\nDigite S para sair")
            operacao = input("Operação (F, A ou S):")
            print("-------------")
            if operacao.lower() == "s":
                os.system('cls')
                Acess = int(input("\nDigite sua senha para checar o lucro do dia:"))
                if Acess == Cadastro:
                    print(f"O lucro do dia foi de {soma} reais\n'Cliente-Conta'\n")
                    for indice, nome in enumerate(pago):
                        print(nome)
                    break
                else:
                    print("Acesso inválido")
                    break
            elif operacao.lower() == "f":
                adicionar_cliente()
            elif operacao.lower() == "a":
                atender_cliente()
            else:
                print("\nOperação inválida, digite apenas F, A ou S")

if __name__ == "__main__":
    main()
