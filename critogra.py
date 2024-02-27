alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(direction, message, shift):
    result_message = ""
    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = (position + shift) % len(alphabet)
            elif direction == "decode":
                new_position = (position - shift) % len(alphabet)
            result_message += alphabet[new_position]
        else:
            result_message += letter
    return result_message

def main_function():
    while True:
        direction = input("Digite 'encode' para encriptar mensagem, e 'decode' para descriptar:\n")
        message = input("Digite a mensagem que deseja encriptar ou descriptar:\n").lower()
        shift = int(input("Digite o número base para a cifra:\n"))

        result = caesar_cipher(direction, message, shift)
        print(f"A mensagem resultante é: {result}")

        sair = input("Digite 's' para sair ou qualquer outra tecla para continuar: ").lower()
        if sair == 's':
            break

main_function()


