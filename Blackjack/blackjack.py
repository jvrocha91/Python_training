import random
import os
from art import logo
baralho = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Função calcula score do usuario e computador
def score(user_cards,computer_cards):
        user_score=sum(user_cards)
        computer_score=sum(computer_cards)
        print(f"Suas cartas: {user_cards}, score atual: {user_score}")
        print(f"Primeira carta do computador:{computer_cards[0]}")
        return(user_score,computer_score)

def game():
    user_cards=[]
    computer_cards=[]
    cards=0

    #Usuario e computador recebem as cartas
    while cards < 2:
        user_cards += [random.choice(baralho)]
        computer_cards += [random.choice(baralho)]
        cards+=1

    final_game=False
    while final_game != True:
        #Fução que calcula score dos jogadores é chamada
        user_score, computer_score = score(user_cards, computer_cards)
            
        #Checar se um dos jogadores tem um BlackJack (Ace+10)
        all_score = [('Usuario',user_cards),('Computador',computer_cards)]
        for player, card in all_score:
            #Ordenamos as cartas para facilitar a comparação
            card.sort()
            if card == [10,11]:
                print(f"{player} fez um Blackjack!")
        
        #Conferir score do usuario
        if user_score > 21 :
            for card in user_cards:
                if card == 11:
                    ace=int(input("O usuario possui um Ace! Deseja atribuir o valor de 1 ou 11 ?: "))
                    user_cards[card]=user_cards[ace]
                    user_score, computer_score = score(user_cards,computer_cards)
                    if user_score > 21:print(f"O usuario perdeu pois ultrapassou o 21 , score: {user_score}") 
                    break 
                else: print(f"O usuario perdeu pois ultrapassou o 21, score: {user_score}")
                break  

        #Escolha do usuario entre pegar mais uma carta ou terminar o jogo
        game_choice=input("Digite 'y' para pegar outra carta e 'n' para passar: ")
        if game_choice == "y":
            user_cards += [random.choice(baralho)]
        if game_choice == "n":
            final_game=True
    
    #Conferir se o computador pontuou menos que 17, nesse caso deve pegar mais uam carta
    if computer_score < 17:
        print("O computador não atingiu 17 e por isso vai pegar mais uma carta")
        computer_cards += [random.choice(baralho)]
        computer_score=sum(computer_cards)
        if computer_score > 21:print(f"O usuario venceu pois o computador ultrapassou o 21!!! Cartas:{computer_cards}")
        else:
            if user_score > computer_score:
                print(f"O usuario venceu com {user_score} contra {computer_score} do computador!")
                main()
            if computer_score >user_score:
                print(f"O computador venceu com {computer_score} contra {user_score} do usuario!")
                main()
            else:print(f"O usario e computador empataram com {user_score} do usuario e {computer_score} do computador") 
 
def main():
    start=input("Voce quer jogar Blackjack ?\nDigite 's' ou 'n':")
    if start == "s":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        game()
   
main()