def menu_mensage():
    print("============")
    print("Bem vindo ao leilão do João!\n")

def main():
    menu_mensage()
    players={}
    while True:
        nome=input("Digite o nome do comprador:")
        bid=int(input("Qual valor vai apostar:"))
        players[nome]=bid
        final_bid=int(input("Existe algum outro apostador ?:\nDigite '1' ou '2':"))
        if final_bid == 1:
            continue
        if final_bid == 2:
            break
    
    print( {players.keys()}+"---"+{players.values()})

main()



