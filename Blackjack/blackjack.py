import random
import os
from art import logo
baralho = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Função calcula score do usuario e computador
def score(user_cards,computer_cards):
        user_score=sum(user_cards)
        computer_score=sum(computer_cards)
        print(f"Suas cartas: {user_cards}---Score atual: {user_score}")
        print(f"Primeira carta do computador: {computer_cards[0]}")
        return(user_score,computer_score)

#Função que determina o ganhador do jogo baseado em se o computador ultrapassou 21 ou quem fez um maior score
def determine_winner(user_score, computer_score,computer_cards):
    #Conferir se o computador ultrapassou 21 e calcular o vencedor
    if computer_score > 21:print(f"O usuario venceu pois o computador ultrapassou o 21!!! Cartas:{computer_cards}")
    else:
        if user_score > computer_score:
            print(f"O usuario venceu com {user_score} contra {computer_score} do computador!{computer_cards}")
        elif computer_score >user_score:
            print(f"O computador venceu com {computer_score} contra {user_score} do usuario!{computer_cards}")
        else:
            print(f"O usario e computador empataram com {user_score} do usuario e {computer_score} do computador{computer_cards}") 

def game():
    user_cards=[]
    computer_cards=[]
    print("Bem-vindo ao Blackjack! Tente chegar o mais próximo possível de 21 sem ultrapassar.\n"
          "Áses valem 11 ou 1, e você começa com duas cartas.\n")

    #Usuario e computador recebem as cartas
    for _ in range(2):
        user_cards.append(random.choice(baralho))
        computer_cards.append(random.choice(baralho))
        
    final_game=False
    while not final_game:
        #Fução que calcula score dos jogadores é chamada
        user_score, computer_score = score(user_cards, computer_cards)
            
        #Checar se um dos jogadores tem um BlackJack (Ace+10)
        all_score = [('Usuario',user_cards),('Computador',computer_cards)]
        for player, card in all_score:
            #Ordenamos as cartas para facilitar a comparação
            if card == [10,11] or card ==[11,10]:
                print(f"{player} fez um Blackjack!")
                final_game=True
        
        #Conferir score do usuário
        if user_score > 21:
            for i in range(len(user_cards)):
                if user_cards[i] == 11:
                    user_cards[i] = 1  # Considera o Ás como 1
                break  # Sai do loop após ajustar o primeiro Ás
            user_score = sum(user_cards)  # Recalcula o score após ajustar o Ás
            user_score, computer_score = score(user_cards, computer_cards)  # Atualiza os scores
            if user_score > 21:
                print(f"\nO usuário perdeu pois ultrapassou o 21, score: {user_score}")
                final_game=True

        #Escolha do usuario entre pegar mais uma carta ou terminar o jogo
        game_choice=input("Digite 'y' para pegar outra carta e 'n' para passar: ")
        if game_choice == "y":
            user_cards += [random.choice(baralho)]
        if game_choice == "n":
            final_game=True
    
    #Conferir se o computador pontuou menos que 17, nesse caso deve pegar mais uam carta
    if computer_score < 17:
        print("\nO computador não atingiu 17 e por isso vai pegar mais uma carta")
        computer_cards += [random.choice(baralho)]
        computer_score=sum(computer_cards)

    #Chama a função que determina o vencedor do jogo
    determine_winner(user_score, computer_score, computer_cards)

#Função principal e incial do codigo
def main():
    while input("\nVocê quer jogar Blackjack? Digite 's' para sim ou 'n' para não: ") == "s":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        game()
   
main()
