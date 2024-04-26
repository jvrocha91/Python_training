from art import logo
import random
import os

def start():
    print(logo)
    print("Bem vindo ao jogo !\nEstou pensando em um numero entre 1 e 100, tente adivinhar.")

def modo_jogo():   
    while True:
        level=input("Escolha a dificulade. Digite 'facil' ou 'dificil':").lower()
        if level=="facil" or level=="dificil":
            print(f"Você escolheu a dificuldade: {level}")
            return level
        else:print("Entrada inválida, tente novamente.")

def chances(level):
    if level=="facil":
        return 10
    if level=="dificil":
        return 6

def random_number():
    numbers = list(range(1,101))
    x_number=random.choice(numbers)
    return(x_number)
          
def game(level):
    lives=chances(level)
    x_number=random_number()
    while lives > 0:
        print(f"Voce tem {lives} chances para acertar o numero")
        guess=int(input("Escolha um numero:"))
        if guess == x_number:
            print(f"VOCE ADIVINHOU O NUMERO {guess}, PARABENS!")
            return
        elif guess > x_number:
            print("Muito alto")
            lives-=1
        elif guess < x_number:
            print("Muito baixo")
            lives-=1    
    print(f"VOCE PERDEU, O NUMERO ERA {x_number}")     

def main():
     while input("\nVocê quer jogar Adivinhe o numero? Digite 's' para sim ou 'n' para não: ") == "s":
        os.system('cls' if os.name == 'nt' else 'clear')
        start()
        level=modo_jogo()
        game(level)
    
main()
