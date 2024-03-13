import os
def menu_mensage():
    print("============")
    print("Bem vindo ao leilão do João!\n")

def bid_winner(players):
    maior_valor = 0
    winner=""
    for nome in players:
        valor_atual = players[nome]
        if valor_atual > maior_valor:
            maior_valor = valor_atual
            winner = nome
    print(f"O ganhador do leilão foi {winner} com a aposta de {maior_valor} Reais!")
          
def main():
    menu_mensage()
    players={}
    while True:
        nome=input("Digite o nome do comprador:")
        bid=int(input("Qual valor vai apostar: R$"))
        players[nome]=bid
        final_bid=(input("Existe algum outro apostador ?:Digite 'sim ou 'nao':"))
        if final_bid == "sim":
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        if final_bid == "nao":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    bid_winner(players)
    
main()



