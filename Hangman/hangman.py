import random 
import hang_words
from hang_art import logo, stages


print(logo)
hang_word = random.choice(hang_words.lista_animais)
lives=6
display = ["_" for _ in hang_word]
print(display)

end_game=False
while not end_game:
    guess = input("Escolha uma letra: ").lower()
    if guess in display:
        print(f"\nVocê já escolheu a letra {guess}")
    else:
        for position in range(len(hang_word)):
            letter = hang_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in hang_word:
            lives-=1
            print(f"\nVocê escolheu uma letra {guess}, que não está na palavra. Você perdeu uma vida.")
    
    print(stages[6 - lives])
    print(display)

    if "_" not in display:
        end_game = True
        print("Parabens! Você ganhou")
    elif lives == 0:
        end_game = True
        print(f"\nVocê perdeu! A palavra era '{hang_word}'.")







