import random

Pedra = 0
Papel = 1
Tesoura = 2

while True:
    Computador = int(random.randint(0, 2))
    print("\nHora de jogar Jokenpô !\n\nDigite a opcao deseja escolher ?\n\n0-Pedra\n1-Papel\n2-Tesoura")
    game = int(input("Digite sua escolha:"))

    if game == 0:
        print("\nVoce escolheu Pedra!")
        if Computador == 0:
            print("\nO computador tambem escolheu Pedra, voces empataram !")
        elif Computador == 1:
            print("\nO computador escolheu Papel, Computador ganhou !")
        elif Computador == 2:
            print("\nO computador escolheu Tesoura, voce ganhou !")

    elif game == 1:
        print("\nVoce escolheu Papel!")
        if Computador == 0:
            print("\nO computador escolheu Pedra, voce ganhou !")
        elif Computador == 1:
            print("\nO computador escolheu Papel, voces empataram !")
        elif Computador == 2:
            print("\nO computador escolheu Tesoura, Computador ganhou !")

    elif game == 2:
        print("\nVoce escolheu Tesoura!")
        if Computador == 0:
            print("\nO computador escolheu Pedra, Computador ganhou !")
        elif Computador == 1:
            print("\nO computador escolheu Papel, Voce ganhou !")
        elif Computador == 2:
            print("\nO computador escolheu Tesoura, Voces empataram !")


    else:
         print("\nOpcao invalida")
    
