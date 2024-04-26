from art import logo
import random
import os

def start():
    # Mostra o logo do jogo e uma mensagem de boas-vindas, introduzindo o jogo.
    print(logo)
    print("Bem vindo ao jogo !\nEstou pensando em um número entre 1 e 100, tente adivinhar.")

def modo_jogo():
    # Permite ao usuário escolher o nível de dificuldade do jogo e valida a entrada.
    while True:
        level = input("Escolha a dificuldade. Digite 'facil' ou 'dificil':").lower()
        if level == "facil" or level == "dificil":
            print(f"Você escolheu a dificuldade: {level}")
            return level
        else:
            print("Entrada inválida, tente novamente.")

def chances(level):
    # Retorna o número de tentativas que o jogador terá com base na dificuldade escolhida.
    if level == "facil":
        return 10
    elif level == "dificil":
        return 6

def random_number():
    # Gera um número aleatório entre 1 e 100 para ser o número alvo do jogo.
    numbers = list(range(1, 101))
    x_number = random.choice(numbers)
    return x_number

def game(level):
    # Executa o loop principal do jogo, onde o usuário tenta adivinhar o número gerado.
    lives = chances(level)
    x_number = random_number()
    while lives > 0:
        print(f"Você tem {lives} chances para acertar o número")
        guess = int(input("Escolha um número:"))
        if guess == x_number:
            print(f"VOCÊ ADIVINHOU O NÚMERO {guess}, PARABÉNS!")
            return
        elif guess > x_number:
            print("Muito alto")
            lives -= 1
        elif guess < x_number:
            print("Muito baixo")
            lives -= 1    
    print(f"VOCÊ PERDEU, O NÚMERO ERA {x_number}")

def main():
    # Executa o jogo. Continua jogando enquanto o usuário desejar começar uma nova partida.
    while input("\nVocê quer jogar Adivinhe o número? Digite 's' para sim ou 'n' para não: ") == "s":
        os.system('cls' if os.name == 'nt' else 'clear')
        start()
        level = modo_jogo()
        game(level)
